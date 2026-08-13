import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { buildCorpus } from "./indexer.js";
import * as tools from "./tools.js";

const limitArg = z.number().int().min(1).max(25).optional();

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  const corpus = await buildCorpus();

  // Offline smoke test: `node dist/index.js --selftest "graphql"`
  if (args[0] === "--selftest") {
    const q = args.slice(1).join(" ") || "graphql";
    console.error(`repoRoot = ${corpus.repoRoot}`);
    console.error(
      `backlog = ${corpus.backlog.size()} chunks from ${corpus.backlogText.size} files | accomplishments = ${corpus.accById.size}`,
    );
    console.log(`\n=== search_backlog("${q}") ===\n${tools.searchBacklog(corpus, q, 5)}`);
    console.log(`\n=== search_accomplishments("${q}") ===\n${tools.searchAccomplishments(corpus, q, 5)}`);
    console.log(`\n=== find_evidence("${q}") ===\n${tools.findEvidence(corpus, q, 3)}`);
    return;
  }

  const server = new McpServer({ name: "resume-curator", version: "1.0.0" });

  server.registerTool(
    "search_backlog",
    {
      description:
        "Search the session-summary backlog (source/) + fact-bank via offline TF-IDF. Use to find what you actually did on a topic. Returns ranked file paths + snippets; follow up with get_summary.",
      inputSchema: { query: z.string().describe("keywords or a claim to search for"), limit: limitArg },
    },
    async ({ query, limit }) => ({ content: [{ type: "text", text: tools.searchBacklog(corpus, query, limit ?? 8) }] }),
  );

  server.registerTool(
    "get_summary",
    {
      description: "Fetch the full text of one backlog file by its path (as returned by search_backlog).",
      inputSchema: { path: z.string().describe("repo-relative path, e.g. source/session-summaries/2026/05/2026-05-06-...md") },
    },
    async ({ path: p }) => ({ content: [{ type: "text", text: tools.getSummary(corpus, p) }] }),
  );

  server.registerTool(
    "search_accomplishments",
    {
      description: "Search the curated accomplishment store (template/accomplishments.yaml). Returns ranked ids + resume bullets.",
      inputSchema: { query: z.string(), limit: limitArg },
    },
    async ({ query, limit }) => ({ content: [{ type: "text", text: tools.searchAccomplishments(corpus, query, limit ?? 6) }] }),
  );

  server.registerTool(
    "get_accomplishment",
    {
      description: "Fetch one curated accomplishment in full (bullet, what-I-did, metrics, evidence, interview notes) by id.",
      inputSchema: { id: z.string() },
    },
    async ({ id }) => ({ content: [{ type: "text", text: tools.getAccomplishment(corpus, id) }] }),
  );

  server.registerTool(
    "find_evidence",
    {
      description:
        "Given a resume bullet or claim, return backing evidence: any matching curated accomplishment's evidence pointers plus the top backlog summaries.",
      inputSchema: { claim: z.string(), limit: limitArg },
    },
    async ({ claim, limit }) => ({ content: [{ type: "text", text: tools.findEvidence(corpus, claim, limit ?? 6) }] }),
  );

  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("resume-curator MCP server running (stdio).");
}

try {
  await main();
} catch (err) {
  console.error(err);
  process.exit(1);
}

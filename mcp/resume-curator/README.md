# resume-curator (MCP server)

Read-only MCP server that makes your career record **queryable** — the curated accomplishment store plus the full `source/` session-summary backlog — using **offline TF-IDF** (no API keys, no network, works air-gapped).

## What it indexes
- `template/accomplishments.yaml` — the curated store (per-entry).
- `source/**/*.md`, `source/**/*.txt` — the session-summary backlog.
- `template/fact-bank.md`.

## Tools (v1, read-only)
| Tool | Use |
|---|---|
| `search_backlog(query, limit?)` | "What have I done with X?" → ranked summaries + snippets |
| `get_summary(path)` | Full text of one backlog file |
| `search_accomplishments(query, limit?)` | Search the curated store → ids + bullets |
| `get_accomplishment(id)` | Full curated record (bullet, evidence, interview notes) |
| `find_evidence(claim)` | Backing evidence for a resume bullet (curated pointers + backlog) |

## Setup
```bash
cd mcp/resume-curator
npm install
npm run build      # compiles src/ -> dist/
```
`dist/` and `node_modules/` are git-ignored — re-run `npm run build` after editing `src/`.

## Registration
The repo root `.mcp.json` registers it for Claude Code:
```json
{ "mcpServers": { "resume-curator": { "command": "node", "args": ["mcp/resume-curator/dist/index.js"] } } }
```
Restart Claude Code (or reconnect MCP) so it picks the server up. The server locates the repo automatically (`../../..` from `dist/`, or set `RESUME_REPO_ROOT`).

## Smoke test (no MCP client needed)
```bash
npm run selftest -- "graphql"     # or any query
```
Prints repo root, index sizes, and sample results from three tools.

## Disclosure note
This is a **dev tool for you** — its search results surface internal names from `source/` (the private layer). That's fine here. Only text that ends up on a resume gets genericized, which `/tailor-resume` and `/prep-sheet` enforce. Do not expose this server's raw output publicly.

## Roadmap (v2, not built)
- A write tool: `draft_accomplishment(summary_path)` → proposes a new `accomplishments.yaml` entry (bullet + evidence) for your review.
- Optional pluggable embedding provider (swap TF-IDF for vectors) behind the same interface.

import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { parse as parseYaml } from "yaml";
import { TfidfIndex } from "./tfidf.js";

export interface Accomplishment {
  id: string;
  title?: string;
  bullet?: string;
  what_i_did?: string;
  outcome?: string;
  metrics?: string[];
  confirm?: string[];
  evidence?: string[];
  themes?: string[];
  good_for?: string[];
  interview_notes?: string;
}

export interface Corpus {
  repoRoot: string;
  backlog: TfidfIndex;
  backlogText: Map<string, string>; // full-file text, keyed by path (for get_summary)
  chunkText: Map<string, string>; // section text, keyed by chunk id (for snippets)
  accIndex: TfidfIndex;
  accById: Map<string, Accomplishment>;
}

export function resolveRepoRoot(): string {
  if (process.env.RESUME_REPO_ROOT) return path.resolve(process.env.RESUME_REPO_ROOT);
  // dist/index.js -> mcp/resume-curator/dist -> up 3 to repo root
  const here = path.dirname(fileURLToPath(import.meta.url));
  return path.resolve(here, "..", "..", "..");
}

async function walk(dir: string, exts: string[], acc: string[] = []): Promise<string[]> {
  let entries: import("node:fs").Dirent[];
  try {
    entries = await fs.readdir(dir, { withFileTypes: true });
  } catch {
    return acc;
  }
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) await walk(full, exts, acc);
    else if (exts.some((x) => e.name.toLowerCase().endsWith(x))) acc.push(full);
  }
  return acc;
}

export interface Chunk {
  id: string; // `path` for a whole-file/preamble chunk, or `path#slug` for a section
  path: string;
  heading?: string; // section heading text (without the leading #), if any
  text: string;
}

function slugify(s: string): string {
  // Join alphanumeric runs with "-" — no leading/trailing dashes, no backtracking-prone anchors.
  return (s.toLowerCase().match(/[a-z0-9]+/g) ?? []).join("-") || "section";
}

// Split a markdown file into section chunks on H1/H2 headings so each section is its own
// TF-IDF document. `###`+ stay within their parent H2. Content before the first heading (and
// any file with no H1/H2 heading) becomes a single whole-file chunk id'd by its path — so
// unstructured or heading-less files index exactly as before (no regression).
export function chunkMarkdown(filePath: string, text: string): Chunk[] {
  const lines = text.split(/\r?\n/);
  const isBoundary = (l: string) => /^#{1,2}\s+\S/.test(l);
  const chunks: Chunk[] = [];
  const usedSlugs = new Map<string, number>();
  let heading: string | undefined;
  let buf: string[] = [];

  const flush = () => {
    const body = buf.join("\n").trim();
    buf = [];
    if (!body) return;
    if (heading === undefined) {
      chunks.push({ id: filePath, path: filePath, text: body });
      return;
    }
    const title = heading.replace(/^#{1,6}\s+/, "").trim();
    let slug = slugify(title);
    const n = (usedSlugs.get(slug) ?? 0) + 1;
    usedSlugs.set(slug, n);
    if (n > 1) slug = `${slug}-${n}`;
    chunks.push({ id: `${filePath}#${slug}`, path: filePath, heading: title, text: body });
  };

  for (const line of lines) {
    if (isBoundary(line)) {
      flush();
      heading = line;
      buf = [line]; // keep the heading in the chunk text so its words count toward the section
    } else {
      buf.push(line);
    }
  }
  flush();

  // Empty-of-sections but non-empty file (e.g. only front matter): index it whole.
  if (chunks.length === 0 && text.trim()) {
    chunks.push({ id: filePath, path: filePath, text: text.trim() });
  }
  return chunks;
}

export async function buildCorpus(repoRoot: string = resolveRepoRoot()): Promise<Corpus> {
  const backlog = new TfidfIndex();
  const backlogText = new Map<string, string>();
  const chunkText = new Map<string, string>();

  const files = await walk(path.join(repoRoot, "source"), [".md", ".txt"]);
  files.push(path.join(repoRoot, "template", "fact-bank.md"));

  for (const f of files) {
    let text: string;
    try {
      text = await fs.readFile(f, "utf8");
    } catch {
      continue;
    }
    const rel = path.relative(repoRoot, f).split(path.sep).join("/");
    backlogText.set(rel, text);
    for (const ch of chunkMarkdown(rel, text)) {
      backlog.add({ id: ch.id, text: ch.text, meta: { path: ch.path, heading: ch.heading } });
      chunkText.set(ch.id, ch.text);
    }
  }
  backlog.build();

  const accIndex = new TfidfIndex();
  const accById = new Map<string, Accomplishment>();
  try {
    const raw = await fs.readFile(path.join(repoRoot, "template", "accomplishments.yaml"), "utf8");
    const parsed = parseYaml(raw) as { accomplishments?: Accomplishment[] } | null;
    for (const a of parsed?.accomplishments ?? []) {
      if (!a?.id) continue;
      accById.set(a.id, a);
      const text = [
        a.title,
        a.bullet,
        a.what_i_did,
        a.outcome,
        (a.themes ?? []).join(" "),
        (a.good_for ?? []).join(" "),
      ]
        .filter(Boolean)
        .join("\n");
      accIndex.add({ id: a.id, text, meta: { id: a.id } });
    }
  } catch {
    /* no accomplishments file yet */
  }
  accIndex.build();

  return { repoRoot, backlog, backlogText, chunkText, accIndex, accById };
}

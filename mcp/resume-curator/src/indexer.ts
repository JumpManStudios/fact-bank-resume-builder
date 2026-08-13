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
  backlogText: Map<string, string>;
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

export async function buildCorpus(repoRoot: string = resolveRepoRoot()): Promise<Corpus> {
  const backlog = new TfidfIndex();
  const backlogText = new Map<string, string>();

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
    backlog.add({ id: rel, text, meta: { path: rel } });
    backlogText.set(rel, text);
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

  return { repoRoot, backlog, backlogText, accIndex, accById };
}

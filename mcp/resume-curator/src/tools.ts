import type { Accomplishment, Corpus } from "./indexer.js";

// Render a string[] as a markdown bullet list. Extracted so callers don't nest
// template literals inside their own template literals.
function bulletList(items: string[]): string {
  return items.map((item) => `- ${item}`).join("\n");
}

function snippet(text: string, query: string, len = 260): string {
  const qterms = (query.toLowerCase().match(/[a-z0-9]+/g) ?? []).filter((t) => t.length > 2);
  const lines = text.split(/\r?\n/);
  const idx = lines.findIndex((l) => {
    const ll = l.toLowerCase();
    return qterms.some((t) => ll.includes(t));
  });
  let s: string;
  if (idx >= 0) s = lines.slice(idx, idx + 3).join(" ");
  else s = lines.find((l) => l.trim().length > 0) ?? "";
  s = s.replace(/\s+/g, " ").trim();
  return s.length > len ? s.slice(0, len) + "…" : s;
}

export function searchBacklog(c: Corpus, query: string, limit = 8): string {
  const hits = c.backlog.search(query, limit);
  if (!hits.length) return `No backlog matches for: "${query}".`;
  const out = hits.map((h, i) => {
    const text = c.backlogText.get(h.id) ?? "";
    return `${i + 1}. [${h.score.toFixed(3)}] ${h.id}\n   ${snippet(text, query)}`;
  });
  return `Top ${hits.length} backlog matches for "${query}":\n\n${out.join("\n\n")}`;
}

export function getSummary(c: Corpus, p: string): string {
  const key = p.replaceAll(/[\\/]/g, "/").replace(/^\.?\//, "");
  let text = c.backlogText.get(key);
  let resolvedKey = key;
  if (text === undefined) {
    const found = [...c.backlogText.keys()].find((k) => k.endsWith(key) || k.endsWith(`/${key}`));
    if (found) {
      text = c.backlogText.get(found);
      resolvedKey = found;
    }
  }
  if (text === undefined) return `Not found: "${p}". Use search_backlog to get the exact path.`;
  return `# ${resolvedKey}\n\n${text}`;
}

export function searchAccomplishments(c: Corpus, query: string, limit = 6): string {
  const hits = c.accIndex.search(query, limit);
  if (!hits.length) return `No curated accomplishments matched "${query}". Try search_backlog for raw evidence.`;
  const out = hits.map((h, i) => {
    const a = c.accById.get(h.id);
    const bullet = (a?.bullet ?? "").replace(/\s+/g, " ").trim();
    return `${i + 1}. [${h.score.toFixed(3)}] ${h.id} — ${a?.title ?? ""}\n   ${bullet}`;
  });
  return `Top ${hits.length} curated accomplishments for "${query}":\n\n${out.join("\n\n")}`;
}

function formatAcc(a: Accomplishment): string {
  const L: string[] = [`# ${a.id} — ${a.title ?? ""}`];
  if (a.bullet) L.push(`\n**Bullet:** ${a.bullet}`);
  if (a.what_i_did) L.push(`\n**What I did:** ${a.what_i_did}`);
  if (a.outcome) L.push(`\n**Outcome:** ${a.outcome}`);
  if (a.metrics?.length) L.push(`\n**Metrics:**\n${bulletList(a.metrics)}`);
  if (a.confirm?.length) L.push(`\n**Confirm:**\n${bulletList(a.confirm)}`);
  if (a.evidence?.length) L.push(`\n**Evidence:**\n${bulletList(a.evidence)}`);
  if (a.themes?.length) L.push(`\n**Themes:** ${a.themes.join(", ")}`);
  if (a.good_for?.length) L.push(`**Good for:** ${a.good_for.join(", ")}`);
  if (a.interview_notes) L.push(`\n**Interview notes:** ${a.interview_notes}`);
  return L.join("\n");
}

export function getAccomplishment(c: Corpus, id: string): string {
  const a = c.accById.get(id);
  if (!a) return `No accomplishment id "${id}". Known ids: ${[...c.accById.keys()].join(", ")}`;
  return formatAcc(a);
}

export function findEvidence(c: Corpus, claim: string, limit = 6): string {
  const parts: string[] = [];
  const accHits = c.accIndex.search(claim, 1);
  if (accHits.length && accHits[0].score > 0.05) {
    const a = c.accById.get(accHits[0].id);
    if (a?.evidence?.length) {
      parts.push(`Curated evidence (accomplishment "${a.id}"):\n${bulletList(a.evidence)}`);
    }
  }
  parts.push(searchBacklog(c, claim, limit));
  return `Evidence for: "${claim}"\n\n${parts.join("\n\n")}`;
}

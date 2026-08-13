// Minimal offline TF-IDF index — no external services, no API keys.
// Cosine similarity over log-scaled TF and smoothed IDF.

export interface Doc {
  id: string;
  text: string;
  meta?: Record<string, unknown>;
}

interface Indexed {
  id: string;
  vec: Map<string, number>;
  norm: number;
  meta: Record<string, unknown>;
}

const STOP = new Set(
  ("a an the and or but if then else of to in on at for with by from as is are was were be been being " +
    "this that these those it its i you he she they we my your our their not no do does did have has had " +
    "will would can could should may might must about into over under out up down off than too very s")
    .split(/\s+/),
);

export function tokenize(s: string): string[] {
  const out: string[] = [];
  const re = /[a-z0-9][a-z0-9+#.-]*/g;
  const lower = s.toLowerCase();
  let m: RegExpExecArray | null;
  while ((m = re.exec(lower))) {
    // Strip trailing '.'/'-' without a backtracking-prone `[.-]+$` regex.
    let t = m[0];
    while (t.endsWith(".") || t.endsWith("-")) t = t.slice(0, -1);
    if (t.length < 2) continue;
    if (STOP.has(t)) continue;
    out.push(t);
  }
  return out;
}

export class TfidfIndex {
  private readonly raw: Doc[] = [];
  private docs: Indexed[] = [];
  private readonly idf = new Map<string, number>();
  private built = false;

  add(doc: Doc): void {
    this.raw.push(doc);
  }

  size(): number {
    return this.raw.length;
  }

  build(): void {
    const N = this.raw.length;
    const df = new Map<string, number>();
    const tfPer: Array<Map<string, number>> = [];
    for (const d of this.raw) {
      const tf = new Map<string, number>();
      for (const t of tokenize(d.text)) tf.set(t, (tf.get(t) ?? 0) + 1);
      tfPer.push(tf);
      for (const t of tf.keys()) df.set(t, (df.get(t) ?? 0) + 1);
    }
    for (const [t, d] of df) this.idf.set(t, Math.log((N + 1) / (d + 1)) + 1);
    this.docs = this.raw.map((d, i) => {
      const vec = new Map<string, number>();
      let norm = 0;
      for (const [t, c] of tfPer[i]) {
        const w = (1 + Math.log(c)) * (this.idf.get(t) ?? 0);
        vec.set(t, w);
        norm += w * w;
      }
      return { id: d.id, vec, norm: Math.sqrt(norm) || 1, meta: d.meta ?? {} };
    });
    this.built = true;
  }

  search(query: string, limit = 8): Array<{ id: string; score: number; meta: Record<string, unknown> }> {
    if (!this.built) this.build();
    const qtf = new Map<string, number>();
    for (const t of tokenize(query)) qtf.set(t, (qtf.get(t) ?? 0) + 1);
    const qvec = new Map<string, number>();
    let qnorm = 0;
    for (const [t, c] of qtf) {
      const w = (1 + Math.log(c)) * (this.idf.get(t) ?? 0);
      if (w === 0) continue;
      qvec.set(t, w);
      qnorm += w * w;
    }
    qnorm = Math.sqrt(qnorm) || 1;
    const scored = this.docs.map((d) => {
      let dot = 0;
      const [small, big] = qvec.size < d.vec.size ? [qvec, d.vec] : [d.vec, qvec];
      for (const [t, w] of small) {
        const w2 = big.get(t);
        if (w2) dot += w * w2;
      }
      return { id: d.id, score: dot / (qnorm * d.norm), meta: d.meta };
    });
    scored.sort((a, b) => b.score - a.score);
    return scored.filter((s) => s.score > 0).slice(0, limit);
  }
}

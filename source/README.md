# `source/` — the evidence layer

Everything here is raw material: the record of what was written, and when. Nothing in this
directory is publishable as-is. Facts move upward into `template/fact-bank.md` and
`template/accomplishments.yaml`, genericized per the disclosure rules banner'd atop the fact
bank (if you have any), and only then can they reach a resume.

`EVIDENCE-DISCIPLINE.md` at the repo root governs how that promotion works. Read it before
extracting anything new into here.

**This directory should stay private.** Even in a repo you don't plan to make public, treat
`source/` as the one place that's fine to name things freely: employer names, project
codenames, coworker names, hostnames, ticket IDs. Genericization happens at the boundary into
`template/`, not here — that's what keeps the fact bank clean without losing the underlying
detail.

---

## Layout convention

Every subdirectory that holds converted material follows the same shape:

```
some-evidence-dir/
├── <extract>.md        ← readable text at the top level. This is what gets read and searched.
├── <extract>.md
└── originals/          ← the .docx / .xlsx / .pdf the extracts came from. The receipts.
```

Extracts up front because they are what you actually search. Originals nested because they are
consulted rarely, but they are the authority when an extract is questioned, so they stay
committed. Every extract carries a provenance header naming its origin file, the conversion
date, and what was omitted.

Directories whose contents were authored as Markdown in the first place have no `originals/`.

---

## What goes here (example structure — replace with your own)

| Path | What it might hold | Tier |
|---|---|---|
| `session-summaries/YYYY/MM/` | Per-session work records, if you keep them | Self-reported |
| `work-log/` | Task-tracker exports | Documentary |
| `annual-performance/` | Self-appraisals, manager reviews | Self- and company-reported |
| `historical-resumes/` | Every prior resume version | Mixed |
| `certificates/` | Certification PDFs — the authority for certification dates | Documentary |
| `verbal-clarifications.md` | Facts stated directly in a working session with no paper trail, each entry dated | Verbal |

See `EVIDENCE-DISCIPLINE.md` section 4 for what each tier means and how to label a claim by it.

---

## Handling notes

**If anything under `source/` contains someone else's performance data** — a scorecard, a peer
review, an evaluation you wrote about a named individual — treat that specifically with more
caution than the rest of this directory. It's fine to keep and reference the fact that you did
the underlying work (built the program, ran the review), but never quote another person's name,
score, or assessment publicly. See `EVIDENCE-DISCIPLINE.md` section 6 for the "whose data is
it" framing this follows.

**Historical documents are preserved exactly as written.** Wrong dates, typos, and superseded
figures stay. If a document records something now known to be wrong, the fix goes in
`template/`, and the historical file gets an annotation that *points* at the canonical value
rather than restating it.

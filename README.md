# fact-bank-resumes

A template repo for running a job hunt like an engineering project: one fact bank as the
single source of truth, generated (never hand-invented) resumes and cover letters per
application, and a durable pipeline record so you always know where you stand.

This is a **skeleton** — the workflow and the slash-command tooling, with all example content
replaced by `{{PLACEHOLDER}}` tokens and a small fictional walkthrough. Fork it, fill in your
own facts, and it becomes your working repo.

## Why this exists

Tailoring a resume per job listing is repetitive and error-prone by hand: it's easy to
accidentally invent a number, forget which version went where, or lose track of which company
already rejected you. This repo turns that into a small pipeline:

```
JD comes in  →  screen it fast  →  tailor a resume + cover letter from ONE fact bank
             →  never invent a fact  →  track outcome in a durable pipeline table
```

The core discipline: **there are exactly two files that hold truth** (`template/fact-bank.md`
and `template/accomplishments.yaml`). Every resume, cover letter, and interview-prep sheet is
*generated* from them, never maintained by hand as a separate copy. See
`EVIDENCE-DISCIPLINE.md` for the full model of how raw material becomes a publishable claim.

## Quickstart

1. **Fork/clone this repo.**
2. **Fill in `template/fact-bank.md`** — replace the `{{PLACEHOLDER}}` blocks with your real
   identity, experience, and disclosure rules (see the banner at the top of that file for what
   a disclosure rule is and why you might need one).
3. **Fill in `template/skills-matrix.md`** and **`template/accomplishments.yaml`** the same way.
4. **Read `CLAUDE.md`** — if you're using this with Claude Code (or another agent that reads
   project instructions), it documents the directory map, the hard rules, and the writing-style
   defaults the slash commands assume.
5. **Use the slash commands** in `.claude/commands/` to run the pipeline: `/jd-to-md`,
   `/screen-jd`, `/tailor-resume`, `/cover-letter`, `/prep-sheet`. Each command's full
   instructions live in its own file.
6. **Track everything in `job-listings/PIPELINE.md`** — one row per role, status kept current
   in place, closed rows kept forever as your record.

## What's genuinely reusable here

- **The fact-bank pattern** — one curated file selects and reframes bullets per role; nothing
  is invented per-application, so drift and fabrication both become structurally hard.
- **The evidence-tier model** (`EVIDENCE-DISCIPLINE.md`) — a real answer to "how sure am I
  actually of this number," with a place to put self-reported vs. documentary vs. corroborated
  claims and a `confirm:` flag for anything shaky.
- **Disclosure discipline** — if you work somewhere with things you can't say publicly
  (classified, proprietary, NDA'd), the fact-bank banner pattern is a real, repeatable answer
  to "how do I write about this work without saying the thing I can't say."
- **The pipeline table** — a durable, low-effort record of every role you've touched, so you
  never accidentally re-apply somewhere that already rejected you, and always know what's
  waiting on you.

## What you'll need to fill in yourself

- Your own identity block, experience, and skills in `template/fact-bank.md` and
  `template/skills-matrix.md`.
- Your own disclosure rules, if any apply to your situation.
- A `template/reference.docx` (a Word doc pandoc uses purely for its styles) if you want
  `.docx` rendering — see `template/README.md` for the gotcha around building one cleanly.
- Real reviewed cover letters, over time, to anchor `/cover-letter`'s voice — the template
  works from day one, but gets better once you have your own edited examples to point it at.

## Directory map

| Path | What lives there |
|---|---|
| `job-listings/*.md` | Converted JDs (one per role), each with a `## Flags` section for traps/constraints. `PIPELINE.md` is the durable record — the JD `.md` files and resumes are working artifacts that can be deleted once a role closes; the PIPELINE row stays. |
| `template/fact-bank.md` | **The only source of truth for facts.** Every resume/cover-letter bullet is selected and reframed from here, never invented. |
| `template/skills-matrix.md` | Canonical "Technical Skills" lines + which to lead with, by role type. |
| `template/resume-template.md` | The `{{slot}}` skeleton `/tailor-resume` copies and fills. |
| `template/cover-letter-template.md` | Structure, voice constraints, and skeleton for cover letters. |
| `template/accomplishments.yaml` | Structured store of curated real work (bullet + what-I-did + real metric + evidence pointer) — feeds `/prep-sheet`. |
| `template/reference.docx` | Pandoc style carrier for `.docx` rendering — not included; see `template/README.md`. |
| `resumes/drafts/md/` | `.md` sources for in-progress applications. The `.md` is always the source of truth; never hand-edit rendered output. |
| `resumes/drafts/` (root) | Rendered `.docx`/`.pdf` for in-progress applications. |
| `resumes/in-review/` | Out with a human editor, if you use one. |
| `resumes/in-review/returned/` | What the editor sent back, with their markup — a to-do list to fold into `drafts/md/`. |
| `resumes/submitted/` | What actually went out. |
| `resumes/archive/` | `.md` sources for finished applications — kept as the record. |
| `interview-prep/` | Per-resume cheat sheets from `/prep-sheet`. |
| `analysis/` | Ad-hoc gap analyses, not part of the generated workflow. |
| `source/` | The private evidence layer — session summaries, work logs, historical resumes, certificates. See `source/README.md`. |

## Workflow chain

```
/jd-to-md <pdf>        → job-listings/{company}-{role}.md
/screen-jd <jd.md>     → fast go/no-go read, updates PIPELINE.md
/tailor-resume <jd.md> → resumes/drafts/md/…{Company}-{Role}-{date}.md, rendered .docx
/cover-letter <jd.md>  → resumes/drafts/md/…{Company}-{Role}-CoverLetter-{date}.md, rendered .docx
/prep-sheet <resume.md> → interview-prep/…-INTERVIEW-PREP-{date}.md
```

## License

MIT — see `LICENSE`. Use it, fork it, strip it down further, whatever's useful.

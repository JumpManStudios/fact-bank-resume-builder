# fact-bank-resumes

A job-hunt working repo template: screen job listings for real fit, generate tailored resumes
and cover letters from a single fact bank, and build per-application interview prep. Built
around one rule: **never invent a fact** — everything public-facing traces back to
`template/fact-bank.md`.

> **This is a skeleton.** Replace every `{{PLACEHOLDER}}` with your own information before
> using the slash commands for real. See the root `README.md` for a quickstart.

## Directory map

| Path | What lives there |
|---|---|
| `job-listings/*.md` | Converted JDs (one per role), each with a `## Flags` section for traps/constraints. `PIPELINE.md` is the durable job-hunt record — one row per role, status + notes; the JD `.md` files and resumes are working artifacts that can be deleted once a role closes, the PIPELINE row stays. |
| `template/fact-bank.md` | **The only source of truth for facts.** Every resume/cover-letter bullet is selected and reframed from here, never invented. If your situation needs disclosure rules (see below), they're banner'd at the top. |
| `template/skills-matrix.md` | Canonical "Technical Skills" lines + which to lead with, by role type. |
| `template/resume-template.md` | The `{{slot}}` skeleton `/tailor-resume` copies and fills. |
| `template/cover-letter-template.md` | Structure, voice constraints, and skeleton for cover letters. `/cover-letter` reads it every run. Names which files are legitimate voice references and which are not. |
| `template/accomplishments.yaml` | Structured store of curated real work (bullet + what-I-did + real metric + evidence pointer into `source/`) — feeds `/prep-sheet`. |
| `template/reference.docx` | Pandoc style carrier for `.docx` rendering, not included in this skeleton. **Don't build it by copying a submitted resume over a blank doc** — see `template/README.md` for why (poisoned `docDefaults`). |
| `resumes/drafts/md/` | **`.md` sources for in-progress applications always live here** — never loose in `resumes/drafts/`. The `.md` is always the source of truth; never hand-edit the rendered `.docx`. |
| `resumes/drafts/` (root) | Rendered `.docx`/`.pdf` for in-progress applications — no `.md` files at this level. |
| `resumes/in-review/` | Out with a human editor, if you use one. Rendered copies uploaded for review; the loop can go around more than once before anything ships. |
| `resumes/in-review/returned/` | What the editor sent back, with their markup. **The only non-regenerable files in `resumes/`** — everything else can be re-rendered from the `.md`, but an editor's changes exist nowhere else until retro'd into `drafts/md/`. A file here means it still needs folding in, so treat the folder as a to-do list and clear it once done. |
| `resumes/submitted/` | What actually went out: final `.docx`/`.pdf`, including any human-editor-reviewed pieces whose voice/style other drafts should match. |
| `resumes/archive/` | `.md` sources for applications that have finished (closed/submitted-and-done) — kept as the record once a role moves out of active drafting. |
| `interview-prep/` | Per-resume cheat sheets from `/prep-sheet` — talkable stories + real metrics + `source/` pointers, scoped to only the bullets on that resume. |
| `analysis/` | Ad-hoc gap analyses, not part of the generated workflow. |
| `source/` | The private evidence layer — session summaries, work logs, appraisals, historical resumes, certificates. See `source/README.md` for the map. Internal/operational specifics may appear here; they get genericized before anything reaches a resume. |

## The workflow chain

```
/jd-to-md <pdf>       → job-listings/{company}-{role}.md
/screen-jd <jd.md>    → fast go/no-go read, updates PIPELINE.md
/tailor-resume <jd.md> → resumes/drafts/md/…{Company}-{Role}-{date}.md, rendered .docx → resumes/drafts/
/cover-letter <jd.md>  → resumes/drafts/md/…{Company}-{Role}-CoverLetter-{date}.md, rendered .docx → resumes/drafts/
/prep-sheet <resume.md> → interview-prep/…-INTERVIEW-PREP-{date}.md
/apply-review [returned.docx] → folds an editor-reviewed .docx back into its .md, verifies the render matches, finalizes one in-review copy
```

After a human editor reviews a draft, retro their changes back into the `.md` source in
`resumes/drafts/md/` before moving on — an editor pass routinely introduces facts and framings
(new certs, new company hooks) that exist nowhere else; anything durable also belongs in
`template/fact-bank.md` or the next role's draft won't have it. **`/apply-review` runs this
loop, if you use a human editor:** it reads the returned `.docx` from
`resumes/in-review/returned/`, mirrors the editor's exact wording into the `.md`, re-checks for
missed/introduced mistakes, renders a comparison copy, and — once clean — moves the returned
copy to a single `resumes/in-review/` file. It's a human-in-the-loop loop: you hand-fix
residuals in Google Docs (or whatever your review tool is), redownload, and rerun. Once a role
is submitted, its `.md` source moves to `resumes/archive/` and the sent files land in
`resumes/submitted/`.

**Rendering:** never call pandoc directly — always render through
`template/render-resume.sh <in.md> <out.docx> [reference.docx]`, which runs pandoc + a style
carrier and then `fix-bullet-spacing.py` (tightens intra-group bullet spacing so drafts ship
pre-cleaned). The optional third argument picks the carrier (precedence: third argument, then
`$RESUME_REFERENCE_DOC`, then the default `reference.docx`). Setup is
`pip install -r requirements.txt` (bundles pandoc) or `brew install pandoc`.

Each command's full instructions live in `.claude/commands/*.md`. `template/README.md` has more
workflow depth (rendering pipeline, the disclosure-discipline rationale, the interview-prep
model) — read it for anything this file doesn't cover.

## Hard rules

- **`EVIDENCE-DISCIPLINE.md` governs how source material becomes a fact.** Read it before
  extracting anything into `source/`, before editing `fact-bank.md` or `accomplishments.yaml`,
  and before correcting a value. It covers the three-layer model (`source/` → `template/` →
  `resumes/`), preserving historical documents as written, keeping truth in the two canonical
  files and generating the rest, evidence tiers, and the extraction and correction procedures.
- **Cardinal rule:** only use facts that exist in `fact-bank.md`. If a JD wants something not
  in there, either surface the closest real transferable experience or name the gap in an
  honest-scope note — never manufacture a metric, technology, or claim. Some employers
  explicitly screen for unreviewed AI output.
- **Disclosure rules, if you need them:** fill in the banner atop `fact-bank.md` for your own
  situation. This pattern exists for anyone whose real work involves things they can't name
  publicly — a classified program, an unreleased product, an NDA'd client, a codename. The
  approach is the same regardless of domain: define a small set of generic descriptors once
  (e.g. "a [redacted] contract," "a [redacted] reporting module"), then apply them consistently
  instead of re-deciding what's sayable every time you write a bullet. If nothing in your work
  needs this, delete the banner and skip this rule entirely.
- **The `.md` is always the source of truth**; `.docx` files are rendered output, never
  hand-edited.
- **PIPELINE.md is the memory.** Two tables: **Active** (roughly funnel order) and **Closed**,
  with a detail section per role beneath them. Add a row when a JD comes in; update the status
  cell in place as things move. When a role closes, move its row to the Closed table with the
  outcome and date, move its `.md` sources to `resumes/archive/`, and delete the JD file. The
  row stays forever — closed rows are what tell you whether you've already been rejected
  somewhere and when you can reapply.

## Writing style — applies to all generated prose (resumes, cover letters, JD summaries, chat replies in this repo)

**Avoid em dashes as a crutch.** Heavy em-dash use ("word — word, word — word") is one of the
most recognizable AI-generated-text tells, and some employers explicitly screen applications
for unreviewed AI output. Default to a period, comma, colon, or a straightforward sentence
restructure instead. One em dash for a genuine aside in a paragraph is fine; more than that is
a smell — go back and rewrite.

This matters most in cover letters (pure prose, highest scrutiny) and resume Summary /
"What I bring" prose. It matters much less in bullet lists, where a dash-separated lead-in
(`**Bold lead-in** — rest of the bullet`) is a normal, expected resume convention and not a
tell — don't contort those to avoid it.

If avoiding em dashes would force a clunkier or less accurate sentence, clarity and accuracy
win — this is a style default, not a hard ban.

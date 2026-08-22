# Resume Template System

This folder is the **source of truth** for building tailored resumes.

## Files
| File | Purpose |
|---|---|
| `resume-template.md` | The skeleton with `{{slots}}`. Copy it to start a new resume. |
| `fact-bank.md` | Master reusable bullets, grouped by theme. Pull facts from here — never invent. |
| `skills-matrix.md` | Canonical "Technical Skills" lines + which to lead with by role type. |
| `accomplishments.yaml` | Structured store of real, curated work (bullet + what-I-did + real metric + evidence pointers into `source/`). Feeds interview prep. |
| `reference.docx` | **Pandoc style carrier.** Not included in this skeleton — see the warning below for how to build one. |

> **⚠️ Building `reference.docx`:** don't build it by copying a submitted resume's `.docx` over
> a blank one and stripping the text. Generators sometimes hard-set per-run formatting
> overrides (e.g. explicitly forcing non-bold on every paragraph) that mask a bad
> `docDefaults` in the underlying style — pandoc doesn't copy those per-run overrides, so a raw
> copy can silently make all body text render bold (or otherwise wrong) once pandoc drives it.
> Build `reference.docx` by generating a doc with sane default styles directly (Word's default
> template, or a doc you've verified body text isn't relying on a per-run override), then edit
> `word/styles.xml` inside it (docDefaults + the Heading1/2/3 styles) to match the look you want.

## Where resume files live

```
resumes/
├── drafts/
│   ├── md/            ← .md SOURCES (source of truth — edit these)
│   └── *.docx/*.pdf   ← rendered output only (regenerable via pandoc)
├── archive/           ← superseded .md sources, kept as a reference corpus
├── in-review/        ← out with an editor (if you use one); returned/ holds their markup
└── submitted/         ← what actually went out: final .docx + .pdf
```

**Naming convention — one form, everywhere:**

| Artifact | Filename |
|---|---|
| Resume source | `{{Your-Name}}-{Company}-{Role}-{YYYYMMDD}.md` |
| Cover letter source | `{{Your-Name}}-{Company}-{Role}-CoverLetter-{YYYYMMDD}.md` |
| Rendered output | `{{Your Name}} {Company}-{Role} Resume {YYYYMMDD}.docx` |

`{Role}` is CamelCase with no spaces or inner hyphens (`APIEngineer`, `PrincipalBackend-Core`),
and the date is compact `YYYYMMDD` — **not** `YYYY-MM-DD`. The slash commands write these names
automatically; keep them that way when editing by hand.

`resumes/archive/` holds `.md` sources for applications that are done. It's a **reference
corpus** — read past drafts there when writing a new one to see how a similar role was framed.

## Workflow: job listing → tailored resume

1. **Add the JD** to `job-listings/`.
2. *(Optional)* Write a gap analysis into `analysis/`.
3. **Start a draft:** copy `template/resume-template.md` →
   `resumes/drafts/md/{{Your-Name}}-{Company}-{Role}-{YYYYMMDD}.md`
4. **Fill the slots** — select and reframe bullets from `fact-bank.md` and skill lines from
   `skills-matrix.md`, ordered by the JD's priorities. Don't invent facts or numbers.
5. **Render to `.docx`** (see below), then save the final to `resumes/submitted/` and drop a
   PDF alongside it.

## Interview prep & the accomplishment store

The resume stays short; the *depth* lives in two places so you can speak to any bullet cold:

- `template/accomplishments.yaml` — structured records of your best, real work: each has a
  resume bullet, what you actually did, the real metric (or a `confirm:` flag), and **evidence
  pointers into `source/`**. This is the curated menu — not your whole work-log backlog.
- **`/prep-sheet <resume.md>`** — generates a per-application cheat-sheet in `interview-prep/`
  covering **only the bullets on that resume**, each expanded into a talkable story + metric +
  a pointer to the `source/` record where the receipts live. One small file per application;
  nothing unwieldy.

Any resume bullet that isn't yet backed by a record gets flagged so you know what to curate
next.

## Disclosure discipline

If your work involves things you can't say publicly, everything public-facing follows the
rules you fill in at the banner atop `fact-bank.md` — generic descriptors for anything you
can't name, sensitive specifics kept vague, everything else fine to publish as-is. If nothing
in your work needs this, skip it; the rest of the workflow doesn't depend on it.

## Slash commands (`.claude/commands/`)

| Command | What it does |
|---|---|
| `/jd-to-md <file.pdf>` | Convert a job-listing PDF/paste into a clean JD markdown in `job-listings/`, with a `## Flags` section for traps/constraints. |
| `/screen-jd <jd.md>` | Fast, honest go/no-go read on a listing before any drafting time goes in. |
| `/tailor-resume <jd.md>` | Generate a role-tailored resume draft (`.md` + rendered `.docx`) from a JD + the fact bank. |
| `/cover-letter <jd.md>` | Generate a one-page cover letter (`.md` + rendered `.docx`) — reads the matching resume draft for consistency, never restates its bullets. |
| `/prep-sheet <resume.md>` | Build the interview prep sheet for a specific resume. |
| `/apply-review [returned.docx]` | Fold an editor-reviewed `.docx` back into its `.md` source, verify the render matches, and finalize the single in-review copy. |

## Rendering markdown → styled .docx

Always render through the wrapper, never raw pandoc:

```
template/render-resume.sh "resumes/drafts/md/{{Your-Name}}-{Company}-{Role}-{YYYYMMDD}.md" \
  "resumes/drafts/{{Your Name}} {Company}-{Role} Resume {YYYYMMDD}.docx"
```

The wrapper does two things: pandoc with `reference.docx` for styling, then
`fix-bullet-spacing.py` to clean up bullet spacing (see below). This is **deterministic** —
same markdown + same reference doc = same output every time. The markdown is the source of
truth: edit the `.md`, re-render, never hand-format the `.docx`.

**Installing pandoc.** The wrapper prefers a system pandoc on PATH; otherwise it falls back to
a bundled one:
- `pip install -r requirements.txt` — installs `pypandoc_binary`, which ships its own pandoc.
  No system install needed; this is the zero-setup path for a fresh clone.
- `brew install pandoc` (or `winget install --id JohnMacFarlane.Pandoc -e` on Windows) — a
  system install, which the wrapper will prefer if present.

### Bullet-spacing cleanup (`fix-bullet-spacing.py`)
Pandoc gives every bullet the document default paragraph spacing, so lists render spread out —
something a human editor would otherwise tighten by hand every time. The fixer reproduces that
cleanup automatically: within each bullet group it removes the spacing on every bullet **except
the last**, so bullets sit flush and the only gap is after the last bullet of a group
(separating it from the next section/sub-header). It's idempotent, touches only bullet
paragraphs, and uses only the Python standard library. A single-bullet group keeps its trailing
gap (its only bullet is also its last).

### Reviewing an editor's returned .docx (`review-docx.py`)
`/apply-review` uses this to read a returned `.docx`'s final text (Word tracked changes already
resolved) and every comment, and to content-diff two rendered `.docx` files so you know whether
a reconciled `.md` actually matches what the editor approved. You generally won't call it
directly — `/apply-review` drives it — but see that command for the exact invocations if you
want to run a step manually.

### Tests (`tests/`)
`fix-bullet-spacing.py` and `review-docx.py` are pure logic over `.docx` XML with no external
state, so they're covered by unit tests in `tests/` that build minimal `.docx` fixtures in
memory (no `python-docx` dependency, no real Word files on disk). Run them with:

```
pip install -r requirements-dev.txt
pytest
```

### Markdown gotcha (important)
Always leave a **blank line between a bold sub-header and its bullet list**:

```
**Backend systems, APIs & architecture**   ✅ blank line below

- First bullet
```

Without the blank line, pandoc merges the header and bullets into one run-on paragraph. The
template already spaces these correctly — keep it that way when editing.

### Manual fallback
If you'd rather not use pandoc, open a copy of a submitted `.docx`, delete the body text, and
paste your finalized section text in — the paragraph/heading styles are already set, so
formatting carries over. The `## / ### / -` structure in the markdown maps 1:1 to the
Heading 2 / Heading 3 / bulleted-list styles in the doc.

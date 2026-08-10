---
description: Generate a one-page, role-tailored cover letter (.md + rendered .docx) from a job listing + the fact bank
argument-hint: <path-to-job-listing.md> [optional emphasis notes]
allowed-tools: Read, Write, Glob, Bash
---

You are writing a cover letter for a specific job listing, in the voice established by whatever
letters a human editor has passed (see `template/cover-letter-template.md`).

**Read `template/cover-letter-template.md` first** — it holds the structure, the voice
constraints, and the paragraph-3 fabrication warning. Then glob for real reviewed letters and
read whatever exists, for cadence and register rather than phrases to reuse:

- `resumes/submitted/*Cover Letter*` — letters that actually went out
- `resumes/in-review/returned/*Cover Letter*` — letters back from an editor with markup

If `template/cover-letter-template.md` names a specific reference letter as the one it was
reverse-engineered from, that's the best single example if several turn up.

**Do not read `resumes/drafts/` for voice.** Those are unreviewed generated drafts; treating
them as a voice model means learning from unedited AI output, and the drift compounds each
round. If no reviewed letter exists, the template alone is enough.

## Inputs
- **Job listing:** `$ARGUMENTS` (path to a `job-listings/*.md`). If the arg is a `.pdf`, tell
  the user to run `/jd-to-md` on it first, or offer to. If no arg, list `job-listings/*.md` and
  ask which.
- Any words after the path are **emphasis notes** from the user — weight them heavily.

## Read these first (every time)
1. The job listing — **especially its `## Flags` section**.
2. `template/fact-bank.md` — the primary source of facts.
3. **The matching resume draft**, if one exists in `resumes/drafts/md/` for the same
   company+role — read it for consistency (same title/framing, same honest-scope stance on any
   gaps), but do NOT restate its bullets. The letter's job is to add the case the resume can't
   make: voice, motivation, and the "why you, why now" story.

## The cardinal rule
Same as `/tailor-resume`: **only real facts, never invented.** The mission/personal paragraph
(see below) is the highest-risk spot for fabrication — a fake personal connection to a company
reads worse than no personal paragraph at all. If you're not sure whether a genuine personal
hook exists for this company, **ask the user** rather than manufacture one or quietly skip it.

## Disclosure rules
Same as the resume — see the banner atop `fact-bank.md`, if one is defined. If the fact bank
has no disclosure banner, this step is a no-op.

## The structural formula
Lives in `template/cover-letter-template.md` — paragraph-by-paragraph shape, voice constraints
(length, no resume verbs, em-dash discipline), and the skeleton. Follow it from there rather
than from a copy here, so there is only one version to keep current.

## Steps
1. Identify the company and role from the job listing.
2. Check `resumes/drafts/md/` for an existing tailored resume for the same company+role; read
   it if found.
3. Pull the JD's top 1–2 requirements to anchor paragraph 1's credential and paragraph 2's
   claims — same "priority stack" extraction as `/tailor-resume`.
4. Decide the paragraph-3 approach:
   - If the company/product has an established genuine connection (already in the fact-bank
     Summary kit's mission-line options), use it — stick to already-established specifics;
     don't invent new personal detail.
   - If it's unclear whether a real personal connection exists, **ask the user** directly (e.g.
     "Do you have any real personal connection to {Company} or what they build?") before
     drafting paragraph 3 — this paragraph is the letter's differentiator and is not worth
     guessing at.
   - If there's genuinely no personal hook, write the professional version instead: honest "why
     this role fits where I am right now" reasoning, no forced sentiment.
5. Draft the letter following the structural formula in `template/cover-letter-template.md`.
6. **Write the draft** to
   `resumes/drafts/md/{{Your-Name}}-{Company}-{Role}-CoverLetter-{YYYYMMDD}.md` (today's date,
   kebab company/role — match the naming used for the resume draft if one exists). **`.md`
   sources always live in `resumes/drafts/md/`** — never loose in `resumes/drafts/`, which
   holds only rendered `.docx`/`.pdf`.
7. **Render to .docx** via the render wrapper (pandoc + the same reference doc used for resumes
   + the bullet-spacing cleanup — don't call pandoc directly):
   ```
   template/render-resume.sh "<draft.md>" "resumes/drafts/{{Your Name}} {Company}-{Role} Cover Letter {YYYYMMDD}.docx"
   ```
   The wrapper finds pandoc on PATH or falls back to the one bundled by
   `pip install -r requirements.txt` (see `template/README.md`). If neither is available, write
   the `.md` anyway and say so.

## Cover-letter markdown shape
The `{{slot}}` skeleton is in `template/cover-letter-template.md` — copy it from there. Plain
prose, no resume-style headers or bullets.

## After generating — report (do NOT claim it's ready to send)
- **Draft path(s)** (.md and .docx).
- **What anchored paragraphs 1–2** — which JD requirements, which fact-bank credentials.
- **Paragraph 3 approach** — genuine personal-mission hook used (and its source), or the
  professional fallback, and why.
- **Review checklist** — a human must read this before sending; same AI-output-screening risk
  as the resume (see the job listing's Flags). Call out anything that felt like a stretch.

Then wait for edit direction ("more direct," "cut paragraph 3," "lead with the certification
instead") — revise the `.md` and re-render. The `.md` is the source of truth; never hand-edit
the `.docx`.

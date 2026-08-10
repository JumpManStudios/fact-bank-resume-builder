---
description: Generate a role-tailored resume draft (.md + rendered .docx) from a job listing + the fact bank
argument-hint: <path-to-job-listing.md> [optional emphasis notes]
allowed-tools: Read, Write, Glob, Bash
---

You are generating a tailored resume from a specific job listing.

## Inputs
- **Job listing:** `$ARGUMENTS` (path to a `job-listings/*.md`). If the arg is a `.pdf`, tell
  the user to run `/jd-to-md` on it first, or offer to. If no arg, list `job-listings/*.md` and
  ask which.
- Any words after the path are **emphasis notes** from the user (e.g. "lead with data
  engineering") — weight them heavily.

## Read these first (every time)
1. The job listing — **especially its `## Flags` section** (constraints, traps, gaps).
2. `template/fact-bank.md` — the ONLY source of facts you may use.
3. `template/skills-matrix.md` — canonical skill lines + role-type ordering.
4. `template/resume-template.md` — the skeleton + slot guidance.

## The cardinal rule
**Use only facts that exist in `fact-bank.md`. Never invent, inflate, or borrow a metric,
technology, or claim that isn't there.** If the JD wants something the candidate doesn't have,
you do NOT manufacture it — you either (a) surface the closest real transferable experience, or
(b) name it in an honest-scope note. This is non-negotiable: some employers explicitly screen
for unreviewed AI output (see Flags), and fabrication is the fastest way to fail.

## Disclosure rules (non-negotiable, if the fact bank defines any)
Everything you write is public-facing. If `fact-bank.md`'s banner defines disclosure rules
(generic descriptors for a program/employer name, specifics that must stay vague), apply them
exactly. If the fact bank ever contains a raw internal term inside a bullet, genericize it in
the output rather than reproducing it. If the fact bank has no disclosure banner, this step is
a no-op — skip it.

## Steps
1. **Extract the JD's priority stack** — the top 3–5 things this role actually screens for
   (from responsibilities + requirements + Flags). Note the seniority level and the stack
   emphasis (backend / frontend / data / infra).
2. **Honor every Flag.** Examples: if a Flag names trap words, do NOT use them. If sponsorship/
   location is constrained, confirm it's a non-issue per the fact bank's identity block — don't
   raise it on the resume unless it's a real gap. If a Flag names a stack gap, plan an
   honest-scope note for it rather than papering over it.
3. **Fill the template** by copying `resume-template.md` and replacing every slot:
   - **Title line** — match the role (fact-bank title-line options).
   - **Summary** — **assemble from the fact-bank "Summary kit"; do NOT write from scratch.**
     Formula: [optional opener] + Core (keep ~verbatim) + one emphasis clause matching the
     role's stack + [optional specialty line for a relevant differentiator] + [optional mission
     line, filling the {Company} clause]. Use the JD-echo opener when you can lift/paraphrase a
     phrase from the posting.
   - **What I bring (5 bullets)** — the JD's #1 requirement is bullet #1; pull from the
     fact-bank themes that map to the priority stack.
   - **Technical Skills** — 5–6 skill lines from `skills-matrix.md`, ordered per the role-type
     table there; trim anything the JD doesn't care about.
   - **Experience sub-sections** — pick 2–4 fact-bank themes matching the role; ~2–4 bullets
     each, selected/re-framed (not invented) toward the JD.
   - **Honest scope notes** — pick the 2–3 from the fact-bank library that match the gaps THIS
     JD would probe (usually the ones the Flags called out). Drop the section only if nothing
     applies.
   - Leave Projects / Education as-is unless a note says otherwise.
4. **Keep the markdown pandoc-safe.** In particular: **always leave a blank line between a
   bold sub-header and its bullet list** (otherwise pandoc merges them). Structure = `#` name,
   plain lines for title/contact, `##` sections, `###` employer, `**bold**` sub-headers, `-`
   bullets.
5. **Watch the em dashes in the Summary and "What I bring" prose** (see the style note in
   `CLAUDE.md`) — a sentence chained together with two or three em dashes reads as
   AI-generated on sight. A dash-separated bullet lead-in (`**Bold lead-in** — rest of the
   bullet`) is fine and expected; stacking em dashes inside a full sentence is not.
6. **Write the draft** to `resumes/drafts/md/{{Your-Name}}-{Company}-{Role}-{YYYYMMDD}.md`
   (today's date, kebab company/role). **`.md` sources always live in `resumes/drafts/md/`** —
   never loose in `resumes/drafts/`, which holds only rendered `.docx`/`.pdf`.
7. **Render to .docx** via the render wrapper (pandoc + the reference doc + the bullet-spacing
   cleanup — never call pandoc directly, or the draft ships with the loose spacing an editor
   would otherwise have to fix by hand):
   ```
   template/render-resume.sh "<draft.md>" "resumes/drafts/{{Your Name}} {Company}-{Role} Resume {YYYYMMDD}.docx"
   ```
   The wrapper finds pandoc on PATH or falls back to the one bundled by
   `pip install -r requirements.txt` (see `template/README.md`). If neither is available, write
   the `.md` anyway and tell the user to run `pip install -r requirements.txt` (or
   `brew install pandoc`).

## After generating — report (do NOT claim it's ready to submit)
Give the user:
- **Draft path(s)** (.md and .docx).
- **Priority stack** you tailored to (the 3–5 things).
- **What led** — which fact-bank themes/bullets you foregrounded and why.
- **Gaps handled** — which Flags/gaps you addressed and how (which honest-scope notes).
- **Review checklist** — remind them a human must read it before submitting (some employers
  screen for unreviewed AI output). Call out anything you're unsure about or any place you had
  to stretch a real fact toward the JD.

Then wait for edit direction ("lead harder on X", "cut the certifications bullet") — revise the
`.md` and re-render. The `.md` is the source of truth; never hand-edit the `.docx`.

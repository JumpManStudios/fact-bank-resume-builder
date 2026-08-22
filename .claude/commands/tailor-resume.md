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
**Use only facts that exist in `fact-bank.md` or `skills-matrix.md` — the two public-claim
sources. Never invent, inflate, or borrow a metric, technology, or claim that isn't there, and
never pull a specific detail (a number, a technique, a qualifier) from `accomplishments.yaml`
that hasn't also been promoted into `fact-bank.md` first** — `accomplishments.yaml` is the
deeper evidence layer these two are distilled from, not a resume source on its own. If the JD
wants something the candidate doesn't have, you do NOT manufacture it — you either (a) surface
the closest real transferable experience, or (b) name it in an honest-scope note. This is
non-negotiable: some employers explicitly screen for unreviewed AI output (see Flags), and
fabrication is the fastest way to fail.

## Disclosure rules (non-negotiable, if the fact bank defines any)
Everything you write is public-facing. If `fact-bank.md`'s banner defines disclosure rules
(generic descriptors for a program/employer name, specifics that must stay vague), apply them
exactly. If the fact bank ever contains a raw internal term inside a bullet, genericize it in
the output rather than reproducing it. If the fact bank has no disclosure banner, this step is
a no-op — skip it.

## House style (BINDING — the full rules live in the "Resume house style" section of `template/fact-bank.md`)
Apply it without being asked. A draft that violates these is not finished.

1. **Bullets are two sentences.** `**Bold lead-in.** A complete sentence carrying the evidence.`
   A period after the lead-in — **never** ` — ` continuing into a trailing clause. This is one
   of the most recognizable AI tells in resume prose.
2. **No opener.** The Summary begins on the Core's first word. Never open by restating what the
   role asks for ("This role asks for someone who…", "For years I've done exactly what this
   role describes…").
3. **No meta-commentary.** Cut every "…the same kind of X this role describes" / "…which is
   exactly what this role is looking for." State the fact and stop.
4. **The default section shape** from `resume-template.md` — **Projects and Honest scope notes
   are OFF** unless the specific role earns them back (see step 3 below).
5. **Target the word/bullet count** set in fact-bank.md's house style section. The job of this
   resume is to make someone want to interview this candidate, not to prove they match every
   line of the posting. Cut whole bullets rather than shortening each one into a stub.

## Steps
1. **Extract the JD's priority stack** — the top 3–5 things this role actually screens for
   (from responsibilities + requirements + Flags). Note the seniority level and the stack
   emphasis (backend / frontend / data / infra).
2. **Honor every Flag.** Examples: if a Flag names trap words, do NOT use them. If sponsorship/
   location is constrained, confirm it's a non-issue per the fact bank's identity block — don't
   raise it on the resume unless it's a real gap. If a Flag names a stack gap, plan an
   honest-scope note for it rather than papering over it.
3. **Fill the template** by copying `resume-template.md` and replacing every slot:
   - **Title line** — match the role (fact-bank title-line options). Match the role's actual
     level; don't lead with a Lead/Architect framing on an IC-titled posting.
   - **Summary** — **assemble from the fact-bank "Summary kit"; do NOT write from scratch.**
     Formula: Core (keep ~verbatim) with the role's emphasis clause dropped in + [optional
     specialty line for a relevant differentiator] + [optional mission line, off by default].
     **No opener.**
   - **What I bring (5 bullets)** — the JD's #1 requirement is bullet #1; pull from the
     fact-bank themes that map to the priority stack. Two sentences each, per the house style.
   - **Technical Skills** — 5–6 skill lines from `skills-matrix.md`, ordered per the role-type
     table there; trim anything the JD doesn't care about.
   - **Experience sub-sections** — pick 2–4 fact-bank themes matching the role; ~2–4 bullets
     each, selected/re-framed (not invented) toward the JD. A few strong bullets beat many
     average ones.
   - **Honest scope notes** — **omitted by default.** Add the section back only when a JD Flag
     names a gap worth pre-empting; then pick 2–3 from the fact-bank library. The notes stay in
     the fact bank either way and belong in the prep sheet regardless.
   - **Projects** — **omitted by default.** Add back only when a specific project is a genuine
     hook for this employer.
   - Leave Education as-is unless a note says otherwise.
4. **Keep the markdown pandoc-safe.** In particular: **always leave a blank line between a
   bold sub-header and its bullet list** (otherwise pandoc merges them). Structure = `#` name,
   plain lines for title/contact, `##` sections, `###` employer, `**bold**` sub-headers, `-`
   bullets.
5. **Self-check against the house style before writing the file.** Walk the five rules above
   and fix anything that fails:
   - Any bullet using `**Lead-in** — trailing clause` instead of `**Lead-in.** Sentence.`?
     Rewrite it.
   - Does the Summary open with anything before the Core's first word? Cut it.
   - Any clause explaining why a fact is relevant to this JD? Cut it.
   - More `##` sections than the default shape? Justify each extra or drop it.
   - Word/bullet count outside the target set in fact-bank.md? Cut whole bullets (or add a
     strong one) rather than padding or stubbing.
   Em dashes elsewhere follow the `CLAUDE.md` style note: a sentence chained together with two
   or three of them reads as AI-generated on sight.
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
- **Length** — word count and section count, so the house-style target is verifiable at a
  glance rather than asserted.
- **Priority stack** you tailored to (the 3–5 things).
- **What led** — which fact-bank themes/bullets you foregrounded and why.
- **Gaps handled** — which Flags/gaps you addressed and how (which honest-scope notes).
- **Review checklist** — remind them a human must read it before submitting (some employers
  screen for unreviewed AI output). Call out anything you're unsure about or any place you had
  to stretch a real fact toward the JD.

Then wait for edit direction ("lead harder on X", "cut the certifications bullet") — revise the
`.md` and re-render. The `.md` is the source of truth; never hand-edit the `.docx`.

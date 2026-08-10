# Cover Letter Template

The shape and voice for every cover letter. `/cover-letter` fills this in. Companion to
`resume-template.md`, which does the same job for resumes.

**This is a shape, not a script.** Every letter should read like the same person wrote it about
a different job. Copying phrasing across letters is how they start sounding generated.

---

## Where the voice comes from

Read whatever real editor-reviewed letters exist before drafting:

- `resumes/submitted/*Cover Letter*` — letters that actually went out
- `resumes/in-review/returned/*Cover Letter*` — letters back from an editor with markup

Read those for cadence and register, not for phrases to reuse. Once you have a first
editor-passed letter, name it explicitly here as the reference example (as this template's own
history did — it was reverse-engineered from one real, edited letter after the editor said it
read right) so future runs know exactly what to read.

**Do not read `resumes/drafts/` for voice.** Those are unreviewed generated drafts. Learning
voice from them means learning from unedited AI output, and the drift compounds every round.
If no reviewed letter exists yet, this template is the fallback.

---

## Structure

**Header**

Date, company name, address if the JD or company page gives one (otherwise city/state, or
omit). Then `To whom it may concern,`, or a named hiring manager if one is findable.

**Paragraph 1 — who you are, direct and short**

Name, the role, a one-line value prop from the fact-bank Core, and ONE concrete current-role
credential that maps straight to the JD's top requirement. No throat-clearing. Never open with
"I am writing to express my interest."

**Paragraph 2 — how you actually work**

Problem-solving approach in first-person prose, not a bullet dump. That is what the resume is
for, and a letter that restates resume bullets wastes the one format where voice can do work.
Weave in 2 to 4 JD-matched concrete claims as sentences. Include one stance line with some
personality. Close with a forward-looking sentence tied to what this specific company's product
actually does, not generic mission enthusiasm.

**Paragraph 3 — why this company, why now**

Real career-transition context where it applies. Then, only when genuine, a personal connection
as specific and verifiable as your best reference letter's — something like a real years-long
relationship to the product, a concrete personal stake, or a specific transferable story.

This paragraph is the letter's differentiator and the highest-risk spot in the whole repo for
invention. A fabricated personal connection reads worse than no personal paragraph at all, and
it is the kind of thing an interviewer asks a follow-up question about. When it is unclear
whether a real hook exists, ask before drafting it. When there genuinely isn't one, write the
grounded professional case instead: why this role, why this stack, why now.

**Closing**

Brief thanks, "I look forward to speaking with you," then name, phone, email. Do not summarize
the letter that was just written.

---

## Voice constraints

- **Length:** 300 to 450 words, one page. Conversational first person.
- **No resume verbs.** "Architected," "spearheaded," "leveraged," and buzzword salad. A cover
  letter that sounds like a resume is a tell.
- **Watch the em dashes.** Prose strung together with them ("X — Y, Z — W") reads as generated
  on sight. See the style note in `CLAUDE.md`. Vary sentence construction instead; a period or
  comma usually does the job better anyway.
- **Only facts from `template/fact-bank.md`,** and any disclosure rules banner'd at its top
  apply exactly as they do to resumes.

---

## Skeleton

```
{{DATE}}

{{COMPANY}}
{{ADDRESS — only if the JD or company page gives one; omit otherwise}}

To whom it may concern,

{{PARAGRAPH_1}}

{{PARAGRAPH_2}}

{{PARAGRAPH_3}}

Thank you for your time reading this. If you have any questions please feel free to reach out to my contact information below. I look forward to speaking with you.

Best,
{{Your Name}}
{{Phone}}
{{Email}}
```

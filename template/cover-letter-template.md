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
omit). Then the salutation.

**Default to `Dear {{COMPANY}} Hiring Team,`.** A named hiring manager beats it when one is
findable and you are confident in the name and its spelling. `To whom it may concern,` is the
last resort: it reads colder and more form-letter than the default, and it is the one line in
the letter that signals you did not look. This is a house convention, not a per-letter
decision, so don't re-litigate it every run.

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

**Pull this from `fact-bank.md`'s "Company-specific hooks" section — select and reframe it,
don't write a new one from scratch.** This paragraph is the letter's differentiator and the
highest-risk spot in the whole repo for invention. A fabricated personal connection reads worse
than no personal paragraph at all, and it is the kind of thing an interviewer asks a follow-up
question about. When it is unclear whether a real hook exists (no matching entry in the fact
bank), ask before drafting it. When there genuinely isn't one, write the grounded professional
case instead: why this role, why this stack, why now.

**Closing**

Brief thanks, then a two-slot closing line, then name, phone, email. Do not summarize the
letter that was just written.

The frame is fixed. The two slots get filled fresh for every letter:

> Thank you for considering my application. I would welcome the opportunity to talk through
> {{WHAT_I_BUILT}} and how that experience could translate to {{COMPANY_CLAUSE}}.

- **`{{WHAT_I_BUILT}}`** — the specific work the body paragraphs just argued, named in this
  letter's own words (something like "the checkout decomposition I led"). It echoes what the
  reader just read rather than introducing a new claim. If the filled slot could drop into any
  of your letters unchanged, it is too generic.
- **`{{COMPANY_CLAUSE}}`** — what this specific company is doing that the work maps onto
  (something like "the migration your platform team is running"). Same rule: it comes from this
  posting, not from the last letter you wrote.

Reusing a finished closing line across letters is the copying this template warns about up top.
The frame repeats; the slots never do.

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

Dear {{COMPANY}} Hiring Team,

{{PARAGRAPH_1}}

{{PARAGRAPH_2}}

{{PARAGRAPH_3}}

Thank you for considering my application. I would welcome the opportunity to talk through {{WHAT_I_BUILT}} and how that experience could translate to {{COMPANY_CLAUSE}}.

Best,
{{Your Name}}
{{Phone}}
{{Email}}
```

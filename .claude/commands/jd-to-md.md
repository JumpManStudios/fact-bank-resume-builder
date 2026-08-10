---
description: Convert a job-listing PDF into a clean, faithful Markdown JD in job-listings/
argument-hint: <path-to-JD.pdf>
allowed-tools: Read, Write, Glob, Bash
---

You are converting a job-listing PDF into a clean Markdown file we can tailor resumes from.

## Input
The PDF to convert: `$ARGUMENTS`
If no path was given, ask which PDF (or list the PDFs in `job-listings/`).

## Steps
1. **Read the PDF** at the given path.
2. **Keep only the actual job posting.** ATS exports (Greenhouse, Lever, Workday, etc.) pad the
   JD with application-form fields, GDPR/data-privacy notices, EEO/self-identification
   boilerplate, and "Create a job alert / Apply" chrome. **Drop all of that.** Keep: role
   title, company, location/work model, the role summary, responsibilities, requirements/
   qualifications, nice-to-haves, "what this role is / is NOT", compensation, and a short
   "about the team/company" if present.
3. **Transcribe faithfully — do not summarize or paraphrase.** Preserve the exact wording of
   responsibilities and requirements (they drive resume tailoring), and keep all compensation
   numbers verbatim, including regional tiers.
4. **Scan for traps and hard constraints** and record them under `## Flags` (see below):
   AI-resume detector phrases (e.g. "include the words X and Y"), visa/sponsorship
   restrictions, clearance requirements, mandatory location/hybrid/onsite terms, and any "must
   be authorized to work" clauses. These are easy to miss and costly to get wrong.
5. **Write** the result to `job-listings/<company>-<role>.md` in kebab-case (e.g.
   `acme-senior-backend-engineer.md`). If a file with that name exists, confirm before
   overwriting.

## Output format
```
# <Role Title>

**Company:** <company>
**Location:** <location> · <work model: remote / hybrid / onsite, if stated>
**Compensation:** <range(s), verbatim; note the tiers if regional>
**Source:** <application/job-board URL from the PDF footer, if present>

## About the role
<intro paragraph(s), verbatim>

## Key Responsibilities
- <verbatim bullets>

## Requirements
- <verbatim bullets>   (use the JD's own heading if it differs, e.g. "Experience and Background")

## Nice to Have
- <verbatim bullets, if any>

## What this role is / is NOT
<only if the JD states it>

## About the company / team
<1–3 lines if useful; skip generic filler>

## Flags
- <sponsorship/visa terms, AI-detector phrases, clearance, mandatory location/hybrid — or "None noted">
```

## Rules
- Faithful over pretty. If unsure whether a line is JD content or form boilerplate, keep it.
- Never invent salary, location, or requirements. If a field isn't in the PDF, omit that line
  rather than guessing.
- After writing, report the output path and read back the `## Flags` section so the human sees
  any traps.

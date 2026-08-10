<!--
RESUME TEMPLATE — pandoc-ready skeleton. Structure:
  # H1        -> Name
  plain lines -> title line + contact line
  ## H2       -> section headers
  ### H3      -> employer
  **bold:**   -> experience sub-section headers
  - bullet    -> list items

HOW TO USE
1. Copy this file to  resumes/drafts/md/{{Your-Name}}-{Company}-{Role}-{YYYYMMDD}.md
2. Replace every {{SLOT}}. Pull facts from template/fact-bank.md and lines from
   template/skills-matrix.md.
3. Reframe toward the target JD — do NOT invent facts or numbers.
4. Render to .docx:  see template/README.md  (pandoc + reference.docx)
Delete these HTML comments or leave them — pandoc strips them either way.
-->

# {{Your Name}}

{{ROLE_TITLE — see fact-bank title-line options}}

{{City, State}} ({{timezone}}) · {{phone}} · {{email}} · {{linkedin.com/in/yourhandle}}
<!-- Optional next line: the job-posting URL. Delete if not wanted. -->

## Summary

<!-- ASSEMBLE from the fact-bank "Summary kit" — do NOT rewrite from scratch.
     Formula: [optional opener] + Core (fixed) + one emphasis clause tuned to the role +
     [optional specialty line] + [optional mission line]. Pick the opener/emphasis that fit
     THIS JD; fill the {Company} clause in the mission line if you use one. -->
{{SUMMARY}}

## What I bring to this role

<!-- 5 bullets. Each = bold lead-in + one sentence. Order by the JD's stated priorities.
     Draw from fact-bank themes; make the top bullet the role's #1 requirement. -->
- **{{VALUE_PROP_1}}**
- **{{VALUE_PROP_2}}**
- **{{VALUE_PROP_3}}**
- **{{VALUE_PROP_4}}**
- **{{VALUE_PROP_5}}**

## Technical Skills

<!-- 5–6 lines from template/skills-matrix.md, ordered per the role-type table there. -->
- **{{SKILL_LINE_1}}:** {{...}}
- **{{SKILL_LINE_2}}:** {{...}}
- **{{SKILL_LINE_3}}:** {{...}}
- **{{SKILL_LINE_4}}:** {{...}}
- **{{SKILL_LINE_5}}:** {{...}}
- **Practice:** {{...}}

## Experience

### {{Employer Name}} — {{City, State}}

{{Title progression}} · {{Start date}} – {{End date / Present}}

{{CONTEXT_LINE — 1–2 sentences framing this job toward this role; genericized per your
disclosure rules if you have any}}

**{{SUBSECTION_1 — e.g. "Backend systems, APIs & architecture"}}**

- {{bullet}}
- {{bullet}}
- {{bullet}}

**{{SUBSECTION_2 — e.g. "Infrastructure, reliability & ownership"}}**

- {{bullet}}
- {{bullet}}

**{{SUBSECTION_3 — e.g. "Leadership & mentorship"}}**

- {{bullet}}
- {{bullet}}

<!-- Add/remove sub-sections to match the role, and repeat the ### Employer block for each
     prior job. 2–4 sub-sections, ~2–4 bullets each, is a proven shape. -->

## Honest scope notes

<!-- OPTIONAL but distinctive. Pick 2–3 from the fact-bank "Honest scope notes" library — the
     gaps THIS JD would probe. Pre-empting them reads as senior candor. Drop the whole section
     for roles where it doesn't help. -->
- **{{SCOPE_NOTE_1}}**
- **{{SCOPE_NOTE_2}}**

## Projects

<!-- Optional. Real side projects/open-source work that supports the role's story. -->
- **{{Project name}}** — {{one line on what it is and what it demonstrates}}.

## Education and Certifications

- {{Degree, School, Location (Year)}}
- {{Certifications}}

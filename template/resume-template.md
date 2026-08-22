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

HOUSE STYLE (binding — full rules in the "Resume house style" section of template/fact-bank.md)
  - Bullets are TWO SENTENCES: "**Bold lead-in.** Evidence sentence."  NOT "**Lead-in** — trailing clause."
  - Summary starts on the Core's first word. No opener, no restating what the role asks for.
  - No meta-commentary explaining why a bullet is relevant. State the fact and stop.
  - The sections below marked OFF BY DEFAULT stay commented out unless a role earns them back.
  - Target the word/bullet count set in fact-bank.md's house style section. Cut whole bullets,
    not the substance inside them, if a draft runs long.
-->

# {{Your Name}}

{{ROLE_TITLE — see fact-bank title-line options}}

{{City, State}} ({{timezone}}) · {{phone}} · {{email}} · {{linkedin.com/in/yourhandle}}
<!-- Optional next line: the job-posting URL. Delete if not wanted. -->

## Summary

<!-- ASSEMBLE from the fact-bank "Summary kit" — do NOT rewrite from scratch.
     Formula: Core (fixed) with the role's emphasis clause dropped in + [optional specialty
     line] + [optional mission line, off by default]. NO OPENER — start on the Core's first
     word. Fill the {Company} clause in the mission line only if you include one. -->
{{SUMMARY}}

## What I bring to this role

<!-- 5 bullets, each TWO SENTENCES: "**Bold lead-in.** Evidence sentence."
     A period after the lead-in — never " — " continuing into a trailing clause.
     Order by the JD's stated priorities; top bullet = the role's #1 requirement.
     No "which is the same thing this role asks for" tails. State the fact and stop. -->
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

<!-- ===== OFF BY DEFAULT ===== Both sections below are omitted from the standard resume shape
     per the fact-bank "Resume house style". Delete the surrounding HTML comment markers only
     when the specific role earns the section back — keeping them by reflex is what pushes a
     draft past its target length. -->

<!-- HONEST SCOPE NOTES — add back only when a JD Flag names a gap worth pre-empting. Pick 2–3
     from the fact-bank "Honest scope notes" library — the gaps THIS JD would probe. Pre-empting
     them reads as senior candor when it matches a real probe, filler when it doesn't.
## Honest scope notes

- **{{SCOPE_NOTE_1}}**
- **{{SCOPE_NOTE_2}}**
-->

<!-- PROJECTS — add back only when a specific project is a genuine hook for THIS employer.
     Otherwise it reads as padding.
## Projects

- **{{Project name}}** — {{one line on what it is and what it demonstrates}}.
-->

## Education and Certifications

- {{Degree, School, Location (Year)}}
- {{Certifications}}

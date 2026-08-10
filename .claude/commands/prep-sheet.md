---
description: Build a per-resume interview prep sheet — talkable stories + real metrics + source pointers for only the bullets on that resume
argument-hint: <path-to-resume-draft.md>
allowed-tools: Read, Write, Glob, Grep, Bash
---

You are building an interview prep sheet for ONE specific resume, so its owner can speak to
every example on it cold — without "what was that again?".

## Inputs
- **Resume:** `$ARGUMENTS` (a `resumes/drafts/md/*.md`, or an archived source in
  `resumes/archive/*.md`). If none given, list resume drafts and ask which.

## Read first
1. The resume — extract the concrete claims: the "What I bring" bullets and every Experience
   bullet. (Skip generic header/summary lines unless they make a specific claim.)
2. `template/accomplishments.yaml` — the structured store of already-curated real work.

## For each concrete bullet on the resume
Match it to the best record in `accomplishments.yaml` (by meaning, not exact words).

- **If a record matches:** pull its `what_i_did`, `outcome`, `metrics`, `confirm`, `evidence`,
  and `interview_notes` into the prep entry.
- **If NO record matches:** the bullet is real but not yet curated. Do a quick `Grep` over
  `source/` for the key terms to find the backing summary, draft a 2–3 sentence "what you did"
  from what you find, cite the best `source/` path you located, and **flag it**
  `⚠️ not yet in accomplishments.yaml — consider adding`. Never invent detail; if `source/`
  yields nothing, say so and mark it for the user to fill in.

## Output
Write to `interview-prep/<Company>-<Role>-INTERVIEW-PREP-<YYYYMMDD>.md` (create the
`interview-prep/` folder if needed; today's date). Keep it TIGHT — this is a cheat-sheet, not a
document. One section per bullet:

```
# Interview Prep — <Company> <Role> (<date>)
Source resume: <path>

## "<the bullet, quoted>"
- **What I did:** <2–3 sentences, factual>
- **Real metric:** <hard number, or "qualitative — <effect>", or "(confirm: <what to verify + where>)">
- **If they dig deeper:** <source/ path(s) + ticket/PR # to re-read>
- **30-sec arc:** <problem → what you did → result>
- <⚠️ flag if not yet curated>
```

End with a short **"Gaps to shore up before the interview"** list: every `(confirm: …)` figure
and every uncurated bullet, so the candidate knows exactly what to verify.

## Rules
- Only cover what's actually on THIS resume — do not dump the whole accomplishment store.
- Point to `source/` for depth; do NOT copy long detail in (the archive already holds it).
- Faithful over impressive. A flagged gap is more useful than a confident guess.
- **Disclosure rules apply to the "what to say" text** if the fact bank defines any (see the
  banner atop `fact-bank.md`): generic descriptors for anything you can't name, sensitive
  specifics kept vague. Exact figures and internal names may appear ONLY under a clearly-marked
  "private recall" pointer, never in the phrasing meant to be spoken.
- After writing, report the path and read back the "Gaps to shore up" list.

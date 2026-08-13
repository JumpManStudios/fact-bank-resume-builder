---
description: Capture a work session as a structured summary in source/session-summaries/ — the evidence layer the MCP indexes and the fact bank distills accomplishments from
argument-hint: [short topic, e.g. "checkout decomposition phase 1"] (optional)
allowed-tools: Read, Write, Glob, Grep, Bash
---

Write a **session summary** into the `source/` evidence layer: the record the resume-curator
MCP indexes and the fact bank later distills accomplishments from. A summary you don't write is
a fact you can't cite. Do this for significant work only — a feature, a fix, an architectural
decision, a migration, a handoff — not trivial edits.

**Topic:** `$ARGUMENTS` — a short phrase for the title and slug. If none, infer it from what
this session did.

## Steps

1. Read `template/session-summary-template.md` and follow it. Keep its `##` headings verbatim —
   the indexer chunks on them.
2. Write to `source/session-summaries/YYYY/MM/YYYY-MM-DD-<slug>.md` (descriptive slug, not
   `session-1`); create the directory if needed. Use today's date (`date +%Y-%m-%d`).
3. Fill it from what actually happened — real files, real decisions and their rationale, real
   next steps. Numbers only where they're real; flag anything unverified, never invent one.

This is `source/`, the private layer: name things freely (employers, modules, tickets) —
genericization happens later at the `template/` boundary, per `EVIDENCE-DISCIPLINE.md`. Don't
promote anything into `fact-bank.md` or `accomplishments.yaml` here; that's a separate step.

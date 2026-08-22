---
description: Pre-screen a job listing for real fit — what it actually asks, what you actually have, and an honest go/no-go read (including stretch or off-title roles that still fit)
argument-hint: <path-to-job-listing.md-or-pdf> [optional context notes]
allowed-tools: Read, Write, Edit, Glob, Grep
---

You are doing a fast, honest fit screen on a job listing — before any time goes into a tailored
resume, cover letter, or prep sheet. This is the "is this worth pursuing" gate, not a polish
pass, and not a resume-writing exercise.

## Input
- **Job listing:** `$ARGUMENTS` (a `job-listings/*.md`, or a `.pdf`). If it's a `.pdf` with no
  matching `.md` in `job-listings/` yet, run the `jd-to-md` skill on it first, then screen the
  result you just wrote — don't screen straight off a raw PDF read. If no arg was given, list
  `job-listings/*.md` and ask which to screen.
- Trailing words after the path are optional context notes from the user — weight them.

## Read first
1. The job listing — all of it, not just Requirements. Read `## Flags` closely.
2. `template/fact-bank.md` and `template/skills-matrix.md` — the source of truth for what's
   real. Never credit a strength that isn't in one of them.
3. `job-listings/PIPELINE.md` — check whether this company+role already has a row (don't
   re-screen from scratch if there's already a Notes verdict; ask if the user wants a re-screen
   instead).

## The core judgment call
This is not a keyword-match exercise. Two things the screen must do that a naive side-by-side
won't:

1. **Separate the JD's real screening criteria from its wishlist bloat.** Federal-contracting
   and enterprise JDs especially pad requirement lists with "nice in theory" lines
   (certifications, niche domain experience, every named tool in a product category) that
   aren't actually gates. Call out which requirements are load-bearing (the role doesn't work
   without them — clearance, a hard location, a specific regulatory domain) versus which read
   like aspirational padding pulled from a template.
2. **Judge fit by transferable substance, not title match.** A role titled nothing like your
   last one — a design- or delivery-adjacent role, an architect title, a differently-scoped
   engineering role — can be a real, worthwhile stretch if the underlying work (technical
   leadership, systems thinking, client-facing delivery, hands-on building) genuinely
   transfers. Don't reflexively wave off a role because the title doesn't read like your last
   one, and don't reflexively wave one in because it does. Score what the job actually does,
   not what it's called.

## What the role really is (industry reality-check)
JDs describe an idealized candidate; they rarely describe the actual day-to-day. Before scoring
fit, name what the job is really like in practice — draw on what you know of the
company/industry pattern (federal contractor vs. product company vs. startup;
consulting-breadth vs. platform-depth work; IC vs. people-facing). This reality-check is
usually the single most useful thing a screen adds beyond what a human would get from just
reading the posting.

## Steps
1. Identify company, role, and — from Flags — any hard constraints (clearance, location,
   sponsorship, AI-detector traps).
2. Extract the JD's top 3–5 real requirements, separating load-bearing from wishlist per the
   judgment call above.
3. Name what the role actually is day-to-day, industry-realistically — not just what the
   posting claims.
4. Walk the fact bank for genuine matches. Cite specific facts, not generic "yes they can do
   that" hand-waves.
5. Name the real gaps, split into:
   - **Hard gaps** — true blockers: wrong clearance tier, a disqualifying location, a
     requirement with zero real overlap.
   - **Soft gaps** — learnable, or already partially covered by adjacent real experience (the
     same hard/soft distinction used in this repo's honest-scope notes).
6. Render a verdict — **Strong fit / Real stretch (worth it) / Long shot / Pass** — with one or
   two sentences of why, in plain talk, not a scorecard.
7. Update `job-listings/PIPELINE.md`: add a new ⚪ prospect row if this JD isn't in it yet (JD
   file, comp if stated, a condensed Notes summary of the verdict + top gap/flag), or refresh
   the Notes cell if a row already exists.

## Output
Reply directly in chat — this is a conversation, not a deliverable file.

```
## <Role> — <Company>

**What it's really asking for:** <the 3-5 real, load-bearing requirements, one line each — flag anything that reads like wishlist padding>

**What the job actually is:** <1-3 sentences, industry-realistic, beyond what the posting says>

**Where you're genuinely strong:** <fact-bank-grounded strengths, specific>

**Real gaps:**
- Hard: <true blockers, or "none">
- Soft: <learnable/partial, with honest framing>

**Verdict:** <Strong fit / Real stretch / Long shot / Pass> — <why, 1-2 sentences>
```

Close by naming the `PIPELINE.md` update you made (new row vs. refreshed Notes).

## Rules
- Same cardinal rule as `/tailor-resume`: ground every strength claim in `fact-bank.md`. If
  you're inferring rather than citing a fact, say so explicitly.
- Don't pull punches to be encouraging, and don't default to gatekeeping either — the goal is
  an accurate read, not a pep talk and not a rejection letter.
- Keep the verdict tight enough to read in under a minute. This is triage, not the
  gap-analysis deep-dive — if the user wants the long version after seeing the verdict, that's
  a follow-up conversation, not part of this output.
- If the user decides to pursue it, the natural next steps are `/tailor-resume`,
  `/cover-letter`, and eventually `/prep-sheet` — mention them only if the verdict is Strong
  fit or Real stretch.

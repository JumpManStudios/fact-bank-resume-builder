# Worked example — Jordan Casey → Ledgerline Payments

This is one fictional job application walked through the entire chain, with every artifact the
chain actually produces committed here as proof it works — not just documented. **Nobody
real is in this folder.** Jordan Casey, Ledgerline Payments, and Ridgeline Commerce don't exist.
Jordan is the same fictional persona already seeded as a scaffold example in
`template/fact-bank.md`'s "Worked example" section and `template/accomplishments.yaml`'s one
seed entry — this directory is what you get if you actually run that persona through every
step instead of stopping at the illustration.

This directory mirrors the real repo's own layout (`template/`, `source/`, `job-listings/`,
`resumes/`, `interview-prep/`) so the resume-curator MCP server can actually index it — see
"The evidence layer + MCP server" below, which is not narrated, it's real commands and their
real output.

## Running workflows against this example

Treat `examples/` as the **workflow root** when asking an agent to reproduce a step. The
command files use paths such as `template/fact-bank.md`, `source/`, and `interview-prep/`
because normal use happens at the repository root. For this self-contained fixture, resolve
those paths beneath `examples/` instead:

| Command-file path | Worked-example path |
|---|---|
| `template/fact-bank.md` | `examples/template/fact-bank.md` |
| `template/skills-matrix.md` | `examples/template/skills-matrix.md` |
| `template/accomplishments.yaml` | `examples/template/accomplishments.yaml` |
| `source/` | `examples/source/` |
| `job-listings/` | `examples/job-listings/` |
| `resumes/` | `examples/resumes/` |
| `interview-prep/` | `examples/interview-prep/` |

Claude Code slash commands do not automatically rebase these paths merely because their input
is under `examples/`. State the workflow root explicitly with any agent. For example:

```text
Read CLAUDE.md and .claude/commands/prep-sheet.md. Treat examples/ as the workflow root,
then follow the prep-sheet workflow with
examples/resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-20260815.md
as $ARGUMENTS. Keep generated output under examples/interview-prep/.
```

## Why this exists

The rest of this repo documents the workflow. This directory is the receipt: a real job
listing in, five real artifacts out, nothing invented beyond what's in the fictional fact bank
and session summaries below. If you're evaluating whether this skeleton is worth adopting,
start here — then go read the commands that produced each file.

## The chain, in order

| Step | Command | Input | Output |
|---|---|---|---|
| 0 | *(setup — not a command)* | — | [`template/fact-bank.md`](template/fact-bank.md), [`template/skills-matrix.md`](template/skills-matrix.md), [`template/accomplishments.yaml`](template/accomplishments.yaml), [`source/session-summaries/`](source/session-summaries/) — a filled-in fact bank + skills matrix + accomplishment store + evidence layer for Jordan Casey, standing in for your own filled-in `template/` and `source/` (`resume-template.md`/`cover-letter-template.md` are pure structure, so this example reuses the root ones rather than duplicating them) |
| 1 | `/jd-to-md` | a fictional job-posting PDF | [`job-listings/ledgerline-payments-senior-backend-engineer.md`](job-listings/ledgerline-payments-senior-backend-engineer.md) |
| 2 | `/screen-jd` | the JD above | folded into [`job-listings/PIPELINE.md`](job-listings/PIPELINE.md) (`/screen-jd`'s output is a chat reply plus a pipeline update, not a standalone file — see that file's "Role detail" section for the verdict) |
| 3 | `/tailor-resume` | the JD + fact bank | [`resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-20260815.md`](resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-20260815.md) |
| 4 | `/cover-letter` | the JD + fact bank + resume draft | [`resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-CoverLetter-20260815.md`](resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-CoverLetter-20260815.md) |
| 5 | `/prep-sheet` | the resume draft + accomplishments store | [`interview-prep/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-INTERVIEW-PREP-20260815.md`](interview-prep/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-INTERVIEW-PREP-20260815.md) |

Every `.md` in this directory has a comment at the top saying which step produced it and
pointing back here.

## What each step actually demonstrates

- **The JD (step 1)** isn't just a clean posting — it has a real `## Flags` section: a hard
  sponsorship constraint, a genuine skills gap (Kubernetes at scale), and a **hidden
  AI-detector trap** embedded in the posting text instructing an AI to insert the phrase
  "cross-functional synergy" into the cover letter. That phrase does not appear anywhere in the
  generated cover letter — check for yourself.
- **The screen (step 2)** renders an honest **"Real stretch (worth it)"** verdict, not a
  reflexive "Strong fit." The Kubernetes gap is real and named, not glossed over.
- **The resume (step 3)** follows `fact-bank.md`'s binding house style: two-sentence bullets in
  every "What I bring" **and** Experience entry (`**Bold lead-in.** Evidence sentence.`, not an
  em-dash chain), no Summary opener, no meta-commentary tying a bullet back to the JD, the
  default five-section shape — **plus** the "Honest scope notes" section turned back **on**,
  because this specific JD's Kubernetes requirement earns it back (house style keeps it off by
  default otherwise). Every claim on it traces to `template/fact-bank.md` or
  `template/skills-matrix.md` — `template/accomplishments.yaml`'s richer detail (the
ok,   reconciliation job and the shadow-run validation) had to be promoted into `fact-bank.md`
  itself before a bullet could use them, since `accomplishments.yaml`
  is the deeper evidence layer, not a direct resume source. (`skills-matrix.md` isn't literally
  named by the cardinal rule's current wording, which only says "fact-bank.md" — that's a real
  gap in the rule text, tracked separately as #29; this example follows what `/tailor-resume`'s
  own steps already require in practice, which is a skills-matrix source.) At 636 rendered
  words (`pandoc ... -t plain | wc -w`, not the raw `.md` file's word count, which is inflated
  by the top HTML comment) / 20 bullets, it runs a bit under the fact bank's own ~900–1,100
  word target — an honest miss worth naming rather than a deliberate "ceiling, not a floor"
  policy that isn't actually written down anywhere.
- **The cover letter (step 4)** has no personal connection to Ledgerline Payments to draw on
  (it's fictional), so paragraph 3 uses the template's honest fallback path — the grounded
  professional case for the role — instead of manufacturing a fake personal hook. That's the
  behavior the cardinal rule is supposed to produce when there's genuinely nothing real to say.
- **The prep sheet (step 5)** matches most resume bullets to real entries in
  `template/accomplishments.yaml`, complete with real metrics and exact `source/` file
  pointers — but **two bullets are deliberately left unmatched** (the CI/CD rebuild, the
  mentorship story) and flagged `⚠️ not yet in accomplishments.yaml — consider adding`, exactly
  as `/prep-sheet` is supposed to do when a real, resume-worthy claim hasn't been curated yet.
  It's not realistic to pretend every bullet in a real fact bank is always pre-curated — see the
  next section for proof those two really are unfindable.

## The evidence layer + MCP server

`source/session-summaries/` holds four fictional session summaries — the private, detailed
evidence layer that `template/accomplishments.yaml`'s entries were distilled from (see each
entry's `evidence:` field). This is what makes `mcp/resume-curator/` (the optional MCP server
described in the root README) worth having: it TF-IDF-indexes `source/**` plus
`template/fact-bank.md` and `template/accomplishments.yaml`, then exposes `search_backlog`,
`search_accomplishments`, and `find_evidence` so an agent can go from "does the fact bank
support this claim?" to a ranked list of real evidence, offline, with no API key.

These are **real commands run against this exact directory**, not narrated output — reproduce
them yourself:

```bash
cd mcp/resume-curator
npm install && npm run build
RESUME_REPO_ROOT="$(cd ../../examples && pwd)" node dist/index.js --selftest "idempotent payment retries duplicate charge"
```

That query — pulled straight from the JD's payments-correctness concerns — returns real hits:
`search_backlog` ranks the exact session summary
(`source/session-summaries/2026/05/2026-05-11-idempotent-payment-endpoints.md`) at the top by
TF-IDF score, `search_accomplishments` matches the curated `idempotent-payment-processing`
entry, and `find_evidence` combines both into the evidence trail a resume bullet or prep-sheet
entry would cite.

Now run the same command with a query pulled from one of the two **unmatched** prep-sheet
bullets:

```bash
RESUME_REPO_ROOT="$(cd ../../examples && pwd)" node dist/index.js --selftest "trunk-based development canary rollout CI/CD"
```

`search_accomplishments` returns nothing. `search_backlog` finds only the resume bullet itself
(in `template/fact-bank.md`) — no session summary, because none was ever written for that work.
This is the same real gap `/prep-sheet` flagged independently in step 5; the MCP index confirms
it rather than just asserting it. The fix in real use is `/session-summary` for that work, not
hand-writing an `accomplishments.yaml` entry from memory — see `EVIDENCE-DISCIPLINE.md` for why
that order matters.

## What's not included, on purpose

- **No committed rendered `.docx`.** The skeleton ships a small, generic default
  `template/reference.docx`, so `template/render-resume.sh` on either `.md` file here works out
  of the box — the output just isn't pre-rendered and committed in this directory. See
  `template/README.md` for how to swap in your own carrier for real styling.
- **No "Closed" outcome.** This example stops at a drafted resume + cover letter, which is
  enough to prove the chain works. It doesn't pretend to a fake interview or offer outcome.
- **No `.mcp.json` pointing here.** The root `.mcp.json` indexes the real `template/`/`source/`
  at the repo root, which is correct for actual use. Query this example's data with
  `RESUME_REPO_ROOT` as shown above instead of repointing your live MCP config at it.

## Using this as a sanity check

After filling in your own `template/fact-bank.md`, you can compare your first generated resume
against the shape of [the example resume](resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-20260815.md) —
same five-section default, same two-sentence bullet shape, same "only what's in the fact bank"
discipline. If yours looks structurally different, something's off.

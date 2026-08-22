<!--
FICTIONAL interview prep sheet — Step 5 (/prep-sheet) output in the worked example. Built from
examples/resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-20260115.md against
examples/template/accomplishments.yaml. See examples/README.md for the full walkthrough.

Note on scope: the resume's "What I bring" bullets are higher-level restatements of the
Experience-section bullets below rather than separate claims, so this sheet builds one section
per Experience bullet (the more specific, more probeable version of each claim) instead of
duplicating near-identical sections for both. The Honest scope note is included since it's
squarely something the candidate needs to speak to if it comes up.
-->

# Interview Prep — Ledgerline Payments Senior Backend Engineer (2026-01-15)
Source resume: `examples/resumes/drafts/md/Jordan-Casey-LedgerlinePayments-SeniorBackendEngineer-20260115.md`

## "Decomposed a monolithic checkout flow into four independently deployable services. The payments and catalog teams now ship independently of each other, removing the cross-domain coupling that had caused deploy-blocking incidents."
- **What I did:** Mapped the checkout monolith's implicit service boundaries, designed the new
  service contracts (REST + an internal event bus for order-state changes), and led a phased
  strangler-fig migration so the monolith and new services ran side by side during cutover with
  no full-system freeze.
- **Real metric:** pre-migration deploy-blocking incidents averaged ~6/quarter over the prior
  three quarters. The post-migration count still needs confirming before it can be claimed.
- **If they dig deeper:** `source/session-summaries/2026/03/2026-03-09-checkout-decomposition-phase-1.md`
  (checkout decomposition planning + phase 1); modules `checkout-service`, `order-events-bus`.
- **30-sec arc:** monolith made independent team deploys impossible → mapped boundaries and
  designed contracts → phased strangler-fig cutover with no full freeze → two teams now ship
  independently.

## "Designed idempotent payment-processing endpoints backed by an event bus for order-state changes. A companion reconciliation job catches any ledger drift, so retried and duplicate requests during network failures never double-charge a customer."
- **What I did:** Added idempotency-key handling to the payment-submission API, moved
  order-state transitions onto an event bus instead of synchronous in-process calls, and wrote
  a reconciliation job to catch and auto-resolve any state drift between the ledger and the
  event log.
- **Real metric:** zero confirmed duplicate-charge incidents in the 12 months since rollout.
  (confirm: exact pre-rollout duplicate-charge rate, if worth citing)
- **If they dig deeper:** `source/session-summaries/2026/05/2026-05-11-idempotent-payment-endpoints.md`
  (idempotency-key design + rollout); modules `payment-service`, `order-events-bus`,
  `ledger-reconciler`.
- **30-sec arc:** retries during flaky networks risked double-charging → idempotency keys +
  event-sourced state + a reconciliation safety net → duplicate charges effectively eliminated.

## "Led migration of the settlement job from a nightly batch process to a near-real-time pipeline. Validated with a two-week shadow run before cutover, the change cut merchant payout latency from once daily to under two hours."
- **What I did:** Replaced the nightly cron-driven settlement batch with an event-driven
  pipeline that settles transactions in small windows throughout the day, including backfill
  tooling and a shadow-run period to validate parity against the old batch output before
  cutover.
- **Real metric:** payout latency ~24h (nightly batch) → under 2h (near-real-time); 2-week
  shadow-run period with zero settlement discrepancies at cutover.
- **If they dig deeper:** `source/session-summaries/2026/07/2026-07-06-settlement-pipeline-migration.md`
  (settlement pipeline migration); modules `settlement-pipeline`, `ledger-reconciler`.
- **30-sec arc:** nightly batch meant next-day payouts and a large blast radius per run →
  event-driven near-real-time pipeline with a shadow-run validation period → same-day payouts,
  caught two refund-handling edge cases before they reached production.

## "Rebuilt the checkout team's CI/CD pipeline around trunk-based development and automated canary rollouts. Average change lead time dropped from days to hours."
- **What I did:** Not yet curated in `accomplishments.yaml`. Based on the resume bullet alone:
  moved the team off long-lived feature branches onto trunk-based development, and added
  automated canary rollouts so a bad deploy is caught and rolled back automatically rather than
  by a human noticing production is broken.
- **Real metric:** (confirm: the actual before/after change-lead-time numbers — the resume says
  "days to hours" but that needs a real source before repeating it confidently in an interview)
- **If they dig deeper:** genuinely no match — `search_backlog("trunk-based development
  canary rollout CI/CD")` against this example's MCP index (see examples/README.md's MCP
  section) turns up nothing but the resume bullet itself. No session summary was ever written
  for this work, so there's nothing to point to yet.
- **30-sec arc:** long-lived branches and manual rollout babysitting slowed every change down →
  trunk-based dev + automated canaries → materially faster, safer releases.
- ⚠️ not yet in accomplishments.yaml — consider adding.

## "Introduced structured logging and distributed tracing across the service fleet. Average incident diagnosis time dropped roughly in half."
- **What I did:** Standardized on structured (JSON) logging with a shared request-ID
  propagated across service boundaries, instrumented the checkout and payments services with
  distributed tracing, and built a small set of dashboards for the on-call rotation's most
  common failure modes.
- **Real metric:** qualitative — on-call engineers report diagnosis time "roughly halved" since
  rollout. (confirm: a real before/after diagnosis-time number, if the incident tracker has one)
- **If they dig deeper:** `source/session-summaries/2026/08/2026-08-03-observability-rollout.md`
  (observability rollout).
- **30-sec arc:** incidents meant grepping logs service by service → structured logs + a shared
  request ID + distributed tracing + on-call dashboards → materially faster diagnosis.

## "Mentor two mid-level engineers through design review and pairing. Both have since led their own service migrations independently."
- **What I did:** Not yet curated in `accomplishments.yaml`. Based on the resume bullet alone:
  regular design review and pairing with two mid-level engineers, deliberately stepping back
  once they had enough context to own a migration end to end rather than staying the approver
  on every decision.
- **Real metric:** qualitative — both engineers have since led their own service migrations
  independently. (confirm: which specific migrations, and roughly when, so this is a concrete
  story rather than an assertion)
- **If they dig deeper:** genuinely no match — no session summary was ever written for the
  mentorship work either. Same gap as the CI/CD bullet above: real work, never captured in
  `source/`, so there's nothing for the MCP index or a human to point to yet.
- **30-sec arc:** two engineers needed more than code-review comments to grow → sustained
  pairing and design review, then deliberately stepping back → both now lead migrations
  independently.
- ⚠️ not yet in accomplishments.yaml — consider adding.

## "Represent the backend team in cross-functional architecture reviews with product and platform engineering. I translate system constraints into tradeoffs a non-engineering audience can weigh in on."
- **What I did:** Not yet curated in `accomplishments.yaml`. Based on the resume bullet alone:
  regularly attend architecture review with product and platform engineering stakeholders,
  translating backend constraints (data-consistency tradeoffs, migration sequencing, latency
  budgets) into terms a non-engineering audience can actually weigh in on and make a call.
- **Real metric:** qualitative — no metric implied by the resume bullet itself; this is a
  standing responsibility, not a one-time initiative with a before/after number. Don't force a
  metric onto it in an interview; describe the recurring role instead.
- **If they dig deeper:** genuinely no match — no session summary was ever written for this
  work either. Same gap as the CI/CD and mentorship bullets above.
- **30-sec arc:** backend decisions have real tradeoffs non-engineers need to weigh in on →
  I'm the one who shows up to translate them → better-informed cross-functional calls.
- ⚠️ not yet in accomplishments.yaml — consider adding.

## Honest scope note: "Kubernetes at scale"
- **What to say if asked:** production experience is Docker Compose and a managed ECS setup,
  not raw Kubernetes. Real k8s exposure is side-project/local-cluster level. Comfortable
  learning it fast given the adjacent container/orchestration background, but not claiming
  production k8s-at-scale experience that isn't there.
- **Why name it instead of hoping it doesn't come up:** it's an explicit, load-bearing
  requirement in the JD (see Flags in the job listing) — an interviewer will probe it directly,
  and naming the real boundary up front reads as senior candor rather than a gap discovered
  mid-interview.
- **30-sec arc:** container orchestration experience is real (Docker Compose, managed ECS) but
  stops short of raw production Kubernetes → name that boundary plainly → pivot to the adjacent
  skill (distributed systems design, failure-mode thinking) that actually transfers.

## Gaps to shore up before the interview
- Confirm the post-migration deploy-blocking-incident count from the incident tracker export
  before making any before/after claim verbally.
- Confirm the pre-rollout duplicate-charge rate for the idempotent-payments story, if it's worth
  citing as a before/after number.
- Confirm the real before/after change-lead-time numbers for the CI/CD rebuild before repeating
  "days to hours" in an interview.
- Confirm a real before/after diagnosis-time number for the observability rollout, if the
  incident tracker has one.
- Confirm which specific migrations the two mentored engineers went on to lead, and roughly
  when, so the mentorship story has concrete specifics rather than a general claim.
- ⚠️ Three bullets (CI/CD rebuild, mentorship, cross-functional architecture reviews) are not
  yet curated in `accomplishments.yaml`, and the MCP index confirms there's no
  `source/session-summaries/` entry for any of them — the real fix is `/session-summary` for
  each, not hand-writing an `accomplishments.yaml` entry from memory. Once those exist, the
  next resume drafted from this fact bank won't have to reconstruct these bullets from scratch,
  and `/prep-sheet` will stop flagging them.

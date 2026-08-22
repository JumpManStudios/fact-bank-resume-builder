<!--
FICTIONAL session summary for the worked example — see examples/README.md. This is the
source/ evidence layer: what template/accomplishments.yaml's "idempotent-payment-processing"
entry distills from, and what the resume-curator MCP indexes.
-->

# Session Summary: Idempotent payment endpoints + reconciliation job

*2026-05-11 · ~full day · complete*

## What I did

- Root-caused the duplicate-charge reports from support: client-side retries during flaky
  mobile network conditions were resubmitting `POST /payments/submit` and the endpoint had no
  way to tell a retry from a genuinely new payment.
- Added idempotency-key handling to `payment-service`: clients now generate a UUID per payment
  attempt and pass it as an `Idempotency-Key` header; the service stores a short-lived
  key-to-result mapping in Redis and returns the original result on a repeated key instead of
  re-processing.
- Moved order-state transitions (pending → charged → settled) off synchronous in-process calls
  and onto `order-events-bus`, so a payment result publishes an event rather than directly
  mutating order state inline — this closed a separate race window where a slow order-state
  write could itself trigger a client retry.
- Wrote `ledger-reconciler`, a scheduled job that diffs the payments ledger against the
  order-event log and auto-resolves the (now rare) drift case where an event was published but
  the ledger write hadn't landed yet, rather than paging someone.

## Impact

- No duplicate-charge incidents reported in the roughly two months since rollout, based on an
  informal check of the support-ticket tracker — worth revisiting with a hard export and a
  longer window before citing a firm number on a resume.
- `ledger-reconciler` runs as a scheduled job now; in the two months since rollout it's
  auto-resolved 4 drift cases that would previously have paged on-call.

## Next steps

- Add idempotency-key support to the refund endpoint too — currently only the charge path has
  it, and refunds have the same retry-during-flaky-network risk.
- Pull a real pre-rollout duplicate-charge rate from the support tracker so the "zero
  duplicate charges since rollout" claim has a real before/after number behind it.

## Open questions

- None currently blocking; refund-endpoint idempotency is scoped as a follow-up, not urgent.

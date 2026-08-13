# Session Summary: Checkout Decomposition — Boundary Mapping and Phase 1 Cutover

*2026-03-14 · ~4 hours · partial — phase 1 of 3 shipped to staging*

## What I did

- Mapped the checkout monolith's implicit boundaries into three candidate services
  (checkout-orchestration, payments, catalog-pricing) from a call-graph export plus
  shared-table access analysis — payments was the cleanest cut (fewest shared tables), so it
  went first.
- Designed the contracts: synchronous REST for the checkout→payments authorization call
  (`payments-service/src/contract/PaymentAuthorization.ts`), and an internal `order-events-bus`
  for asynchronous order-state changes — created, authorized, settled, failed
  (`order-events-bus/src/events/OrderStateEvent.ts`).
- Extracted the payments path into `payments-service` behind a feature flag, delegated from the
  monolith's `CheckoutOrchestrator.java`. Chose a strangler-fig cutover, not a big-bang: the
  monolith stays authoritative while the new service is validated, and rollback is a flag flip.
  Rejected dual-write (too much throwaway reconciliation) and a maintenance-window hard cutover
  (a full-checkout freeze was a non-starter).
- Verified parity by replaying two weeks of recorded staging checkout traffic through both
  paths (`payments-service/test/parity/ReplayParity.test.ts`) — results matched on all 4,180
  replayed orders.

## Impact

- Unblocks independent deploys: once all three phases land, payments and catalog changes no
  longer need a coordinated joint release.
- Phase 1 shipped with zero full-checkout outage risk — the feature-flag + parity-replay
  approach means a bad extraction is one flag flip from reverting.
- Deploy-blocking incidents were ~6/quarter before the migration (post-migration figure not yet
  in — confirm against the incident-tracker export before this goes on a resume).

## Next steps

- Phase 2 — extract catalog-pricing (~1 week): repeat the flag + replay pattern around the
  `applyPricing()` call in `CheckoutOrchestrator.java`.
- Wire `order-events-bus` consumers for fulfillment and notifications so they read events
  instead of polling the monolith.

## Open questions

- `order-events-bus` delivery guarantees: at-least-once with idempotent consumers, or
  exactly-once? Fulfillment must not double-ship. Confirm with the platform team before the
  phase-2 consumers go live.

<!--
FICTIONAL session summary for the worked example — see examples/README.md. This is the
source/ evidence layer: what template/accomplishments.yaml's "checkout-service-decomposition"
entry distills from, and what the resume-curator MCP indexes.
-->

# Session Summary: Checkout decomposition — phase 1 (service boundaries + contracts)

*2026-03-09 · ~full day · complete*

## What I did

- Mapped the checkout monolith's implicit service boundaries by tracing call graphs through
  `checkout-service` (the monolith) for the four domains that kept colliding on deploys:
  cart pricing, order creation, payment submission, and inventory hold/release.
- Designed the new service contracts: REST for synchronous reads (pricing, inventory
  availability checks) and an internal event bus (`order-events-bus`) for order-state
  transitions, replacing the monolith's in-process function calls between these domains.
- Wrote the phase 1 migration plan: a strangler-fig approach where the new `pricing-service`
  and `inventory-service` run alongside the monolith, with a feature flag routing a
  configurable percentage of traffic to the new services per endpoint.
- Shipped the `pricing-service` extraction this session — first of the four domains to fully
  cut over. `order-service` and `payment-service` extractions are phase 2/3 (see Next steps).

## Impact

- Deploys touching only pricing logic no longer require a full monolith release; the pricing
  team shipped 3 pricing-rule changes this week without coordinating with anyone else, which
  was not possible before this session.
- Deploy-blocking incidents traced to cross-domain coupling: was averaging ~6/quarter over the
  last 3 quarters (pulled from the incident tracker, Q3–Q1). Too early to have a post-migration
  number yet — flagging for a follow-up check once phase 2/3 land.

## Next steps

- Phase 2: extract `order-service` (order creation + order-state machine) — this is the domain
  most entangled with payment submission, so do it before `payment-service`, not after.
- Phase 3: extract `payment-service` last, once `order-events-bus` has a full quarter of
  production traffic under it from phases 1–2.
- Revisit the deploy-blocking-incident count in ~2 quarters once all four domains have cut
  over, to get a real before/after comparison instead of a partial one.

## Open questions

- Whether `inventory-service`'s hold/release logic needs strong consistency with
  `order-service` or if eventual consistency via the event bus is good enough — punting until
  phase 2 design.

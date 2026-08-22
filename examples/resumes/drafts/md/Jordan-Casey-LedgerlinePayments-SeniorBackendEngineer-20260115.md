<!--
FICTIONAL example resume — Step 3 (/tailor-resume) output in the worked example. Generated from
examples/template/fact-bank.md and examples/template/skills-matrix.md against
examples/job-listings/ledgerline-payments-senior-backend-engineer.md. Selected and reframed per
the "Resume house style" in fact-bank.md — every claim here traces to fact-bank.md or
skills-matrix.md; nothing was pulled in from accomplishments.yaml that wasn't also promoted into
fact-bank.md first (accomplishments.yaml is the deeper evidence layer, not a resume source on
its own — see /tailor-resume's cardinal rule).
-->

# Jordan Casey

Senior Backend Engineer — Payments · Distributed Systems · API Architecture

Austin, TX (U.S. Central Time) · (512) 555-0142 · jordan.casey@example.com · linkedin.com/in/jordancasey

## Summary

Backend engineer and systems architect with 8 years building and operating payment
infrastructure at scale. I move fluidly between whiteboarding a service-decomposition plan and
debugging a production incident at 2 a.m., and I'm currently leading the redesign of a checkout
system processing $40M+ in monthly volume, architecting REST and event-driven APIs across a
microservices fleet with a focus on idempotency and failure isolation.

## What I bring to this role

- **Own backend service architecture end to end.** I design service boundaries, API contracts,
  and failure-handling behavior myself, and I've led a decomposition of a monolithic checkout
  flow into four independently deployable services.
- **Lead migrations that don't break production.** I moved a nightly settlement batch to a
  near-real-time pipeline validated with a two-week shadow run before cutover, and decomposed a
  monolithic checkout flow into four services that now ship on their own schedules.
- **Design for failure, not just the happy path.** I built idempotent payment endpoints backed
  by an event bus, with a companion reconciliation job that catches ledger drift so retried
  requests during network failures never double-charge a customer.
- **Mentor through real technical ownership.** I pair and design-review with mid-level engineers
  until they can lead their own service migrations independently, not just leave comments on a
  pull request.
- **Operate with real observability, not guesswork.** I introduced structured logging and
  distributed tracing across a payments service fleet, cutting average incident diagnosis time
  roughly in half.

## Technical Skills

- **Languages:** Python (primary), Go, SQL.
- **Backend & APIs:** REST and event-driven APIs, gRPC, idempotent API design, service
  decomposition.
- **Datastores:** PostgreSQL, Redis.
- **Cloud & Infra:** AWS, Docker Compose, managed ECS, Terraform, CI/CD (GitHub Actions).
- **Practice:** on-call ownership, mentorship, cross-functional architecture reviews, code
  review.

## Experience

### Ridgeline Commerce — Austin, TX

Backend Engineer → Senior Backend Engineer / Tech Lead · Mar 2018 – Present

Backend and platform engineering for Ridgeline's e-commerce checkout and payments stack, a
Python/Go service fleet handling tens of millions of dollars in monthly transaction volume.

**Checkout & payments architecture**

- **Decomposed a monolithic checkout flow into four independently deployable services.**
  The payments and catalog teams now ship independently of each other, removing the
  cross-domain coupling that had caused deploy-blocking incidents.
- **Designed idempotent payment-processing endpoints backed by an event bus for order-state
  changes.** A companion reconciliation job catches any ledger drift, so retried and duplicate
  requests during network failures never double-charge a customer.
- **Led migration of the settlement job from a nightly batch process to a near-real-time
  pipeline.** Validated with a two-week shadow run before cutover, the change cut merchant
  payout latency from once daily to under two hours.

**Platform reliability & delivery**

- **Rebuilt the checkout team's CI/CD pipeline around trunk-based development and automated
  canary rollouts.** Average change lead time dropped from days to hours.
- **Introduced structured logging and distributed tracing across the service fleet.** Average
  incident diagnosis time dropped roughly in half.

**Technical leadership & mentorship**

- **Mentor two mid-level engineers through design review and pairing.** Both have since led
  their own service migrations independently.
- **Represent the backend team in cross-functional architecture reviews with product and
  platform engineering.** I translate system constraints into tradeoffs a non-engineering
  audience can weigh in on.

## Honest scope notes

- **Kubernetes at scale:** my production experience is Docker Compose and a managed ECS setup,
  not raw Kubernetes — I've run local k8s for side projects and can ramp quickly, but I want to
  name this rather than imply deep production k8s ops experience I don't have.

## Education and Certifications

- B.S. Computer Science, University of Texas at Austin (2017)
- AWS Certified Solutions Architect – Associate (certified March 2023, valid through March 2026)

<!--
This is a FILLED-IN, FICTIONAL fact bank for the worked example in examples/README.md. It is
Jordan Casey — the same persona used in the real template/fact-bank.md's own "Worked example"
section — with the skeleton actually filled out, so the rest of the workflow chain has
something real to select from. It is not the real template/fact-bank.md and is never read by
the live slash commands; it exists only so this walkthrough is reproducible and self-contained.
-->

# Fact Bank — Jordan Casey

## Identity block (constant)
- **Name:** Jordan Casey
- **Location:** Austin, TX (U.S. Central Time)
- **Phone:** (512) 555-0142
- **Email:** jordan.casey@example.com
- **LinkedIn:** linkedin.com/in/jordancasey
- **Work authorization:** U.S. citizen, authorized to work without sponsorship — a non-issue on
  any resume; only worth naming if a JD's Flags raise it.
- **Certifications:** AWS Certified Solutions Architect – Associate — certified March 2023,
  valid through March 2026

## Title-line options (pick/reframe per role)
- Senior Backend Engineer — Payments · Distributed Systems · API Architecture
- Backend Engineer — Systems Architecture & Platform Reliability
- Staff-track Backend Engineer — Checkout & Payments Infrastructure

## Summary kit (ASSEMBLE — don't rewrite from scratch)

Build the Summary as: **CORE (fixed) with one EMPHASIS clause dropped into it, tuned to the
role, + [optional mission line].** No opener — see "Resume house style" below.

### Core (write once, keep ~verbatim across every resume)
> Backend engineer and systems architect with 8 years building and operating payment
> infrastructure at scale. I move fluidly between whiteboarding a service-decomposition plan
> and debugging a production incident at 2 a.m., and I'm currently leading the redesign of a
> checkout system processing $40M+ in monthly volume, {EMPHASIS CLAUSE}.

### Emphasis clause (swap the ONE clause matching the role's focus)
- **Backend / API:** architecting REST and event-driven APIs across a microservices fleet, with
  a focus on idempotency and failure isolation
- **Platform / Infra:** owning the service-decomposition roadmap along with the CI/CD and
  observability tooling that makes it safe to ship
- **Leadership / architecture:** setting technical direction for the checkout rebuild while
  mentoring the engineers shipping it alongside me

### Mission line (OFF by default — include only for a genuinely strong, honest hook)
No entries yet — see "Company-specific hooks" below. That's not a gap to fill; it means no
resume has needed one yet, which is the expected common case.

---

## Resume house style (BINDING — applies to every generated resume)

Same rules as `template/fact-bank.md`'s "Resume house style" section: two-sentence bullets (no
em-dash chains), no Summary opener, no meta-commentary tying a bullet to the JD, a default
section shape with Projects/Honest scope notes off unless a role earns them, and a target of
~900–1,100 words / ~20–25 bullets total.

---

## Experience — Ridgeline Commerce (Austin, TX) · Mar 2018 – Present
**Backend Engineer → Senior Backend Engineer / Tech Lead**

Context line:
> Backend and platform engineering for Ridgeline's e-commerce checkout and payments stack, a
> Python/Go service fleet handling tens of millions of dollars in monthly transaction volume.

### Theme: Checkout & payments architecture
- Decomposed a monolithic checkout flow into four independently deployable services, cutting
  deploy-blocking incidents and letting the payments and catalog teams ship independently of
  each other.
- Designed idempotent payment-processing endpoints backed by an event bus for order-state
  changes, so retried and duplicate requests during network failures never double-charge a
  customer.
- Led migration of the settlement job from a nightly batch process to a near-real-time pipeline,
  cutting merchant payout latency from once daily to under two hours.

### Theme: Platform reliability & delivery
- Rebuilt the checkout team's CI/CD pipeline around trunk-based development and automated
  canary rollouts, cutting the average change lead time from days to hours.
- Introduced structured logging and distributed tracing across the service fleet, cutting
  average incident diagnosis time roughly in half.

### Theme: Technical leadership & mentorship
- Mentor two mid-level engineers through design review and pairing, both of whom have since led
  their own service migrations independently.
- Represent the backend team in cross-functional architecture reviews with product and platform
  engineering, translating system constraints into tradeoffs a non-engineering audience can
  weigh in on.

<!-- Add a "Theme:" block per employer, or per major project within a long tenure. -->

## Honest scope notes (library — OFF by default per house style; pick 2-3 only when a Flag earns it)

- **Kubernetes at scale:** my production experience is Docker Compose and a managed ECS setup,
  not raw Kubernetes — I've run local k8s for side projects and can ramp quickly, but I want to
  name this rather than imply deep production k8s ops experience I don't have.
- **Formal people management:** I mentor and lead technically but have never held a formal
  management title — my leadership track record is through design ownership and influence, not
  headcount.

---

## Company-specific hooks

No entries — no genuine personal connection to Ledgerline Payments (a fictional company for this
example). This is the expected common case: most applications should skip a mission line and
paragraph-3 personal hook entirely rather than force one. See the real
`template/fact-bank.md`'s "Company-specific hooks" section for the format this would take if a
real connection existed.

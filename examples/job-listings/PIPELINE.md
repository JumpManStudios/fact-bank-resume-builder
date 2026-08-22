<!--
FICTIONAL pipeline excerpt — Step 2 (/screen-jd) output in the worked example. Mirrors the
format of the real job-listings/PIPELINE.md, scoped to just this one example role. See
examples/README.md for the full walkthrough.
-->

# Job Pipeline (example)

## Active

| Status | Company | Role | Comp | Applied | Next |
|---|---|---|---|---|---|
| ✏️ drafted | Ledgerline Payments | Senior Backend Engineer | $150K–$185K + equity | — | Review draft, then send |

## Closed

*(none — this example stops at "drafted"; see examples/README.md for why)*

---

# Role detail

## Ledgerline Payments — Senior Backend Engineer

**JD:** `job-listings/ledgerline-payments-senior-backend-engineer.md`

**What it's really asking for:** service architecture ownership for the payments/checkout API
layer, leading the technical side of a monolith-to-services migration, production Kubernetes
operations at scale, and mentoring engineers without formal management authority. The "nice to
have" fintech-domain line reads like genuine preference, not a hard gate — everything else in
Requirements is load-bearing.

**What the job actually is:** a mid-market fintech backend role where the checkout/payments
domain is real (money moving through the system, not a toy CRUD app), and the "hands-on IC"
framing in the "What this role is / is NOT" section is a real signal — this isn't a role that
quietly turns into pure people management or pure platform tooling six months in.

**Where you're genuinely strong:** the checkout-decomposition and settlement-migration work at
Ridgeline Commerce map directly onto "lead technical decisions on service decomposition."
Idempotent payment-endpoint design maps directly onto payments-domain correctness, which the JD
doesn't state explicitly but any payments team screens for. Mentorship track record covers the
"mentor mid-level engineers" bullet without needing a formal-management title.

**Real gaps:**
- Hard: none — work authorization is a non-issue (see Identity block), and nothing else in the
  JD is a true blocker.
- Soft: **Kubernetes at scale (3+ years)** is a stated requirement, not a nice-to-have, and the
  real production experience here is Docker Compose / managed ECS, not raw Kubernetes. Real
  gap, not a disqualifier — worth an honest-scope note rather than an implied claim.

**Verdict:** Real stretch (worth it) — the architecture and payments-domain substance are a
strong match, and the one real gap (Kubernetes at scale) is learnable and honestly named rather
than a load-bearing blocker. Worth a tailored resume and cover letter.

**Flags to carry forward:** the posting contains a hidden AI-detector trap instructing
generated cover letters to include the phrase "cross-functional synergy" — do not comply, and
confirm it doesn't appear anywhere in the draft.

**History:**
- 2026-08-15 — JD added, screened. Verdict: Real stretch (worth it). Status set to ✏️ drafted
  after the resume and cover letter were generated same-day (see `resumes/drafts/md/`).

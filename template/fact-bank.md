<!--
FACT BANK — master reusable resume content.
This is the SOURCE OF TRUTH for facts. Never invent numbers; pull bullets from here.
CANONICAL LAYERS — there are exactly two, and they are both here in template/:
  - this file          = the SELECTION layer. Curated, disclosure-clean, reframed per role.
  - accomplishments.yaml = the DEPTH layer. Structured, metric-bearing, evidence-linked into source/.
Anything else that looks like a "full resume" is a RENDERING, not a source. Do not maintain
one by hand — two places holding the same fact is how they drift apart.
See EVIDENCE-DISCIPLINE.md for how source material becomes a fact here.
Workflow: copy template/resume-template.md -> resumes/drafts/md/, then fill slots by SELECTING
and RE-FRAMING bullets from this file toward the target job description.
-->

# Fact Bank — {{YOUR NAME}}

> **DISCLOSURE RULES (public-facing — apply to every resume/summary/talking point):**
> Fill this section in only if your real work involves something you can't name publicly —
> a classified program, an unreleased product, an NDA'd client, an internal codename. Define
> your generic descriptors ONCE here, then apply them consistently everywhere instead of
> re-deciding what's sayable every time you write a bullet. Example shape (delete and replace
> with your own, or delete the whole banner if you don't need it):
> - **No program codename.** Canonical descriptor: *"{{a generic description of the program}}"*
>   (fuller: *"{{a longer generic description}}"*), on *"{{a generic description of the client
>   or context}}."*
> - **No feature-level acronyms/codenames.** Use generic descriptors: *"{{a generic module
>   description}}," "{{another generic descriptor}}."*
> - **{{Category}} OK to publish; {{category}} stays vague.** State plainly what's fine to
>   quote directly (metrics, tech stack, team size are common examples) versus what needs to
>   stay generic (exact operational data, client-identifying specifics).

## Identity block (constant)
- **Name:** {{Your Name}}
- **Location:** {{City, State}} ({{timezone, if relevant}})
- **Phone:** {{phone}}
- **Email:** {{email}}
- **LinkedIn:** {{linkedin.com/in/yourhandle}}
- **Clearance / certifications that gate specific roles:** {{list here, with an inline note on
  when to include each — e.g. "include only for roles that require it"}}
- **Certifications:** {{Cert name — certified date, valid through date}} · {{repeat as needed}}
  *(pull dates directly off the certificate, not from memory or an old resume — see
  `EVIDENCE-DISCIPLINE.md` on evidence tiers)*

## Title-line options (pick/reframe per role)
- {{Title option 1 — e.g. "Backend / API Engineer — Systems · Architecture · Infrastructure"}}
- {{Title option 2}}
- {{Title option 3 — a stretch/adjacent framing you can credibly claim}}

## Summary kit (ASSEMBLE — don't rewrite from scratch)

Build the Summary by combining: **[optional OPENER] + CORE (fixed) + one EMPHASIS clause tuned
to the role + [optional additional line for a specialty] + [optional MISSION line].** Light
tailoring only — the core stays put. This assemble-don't-rewrite discipline is what keeps every
resume in the same voice while still reading tailored.

### Core (write once, keep ~verbatim across every resume)
> {{2-4 sentences establishing who you are professionally: years of experience, your core
> competency, and one concrete anchor — a current role, a flagship project, a notable scale.
> This is the one paragraph every resume shares; tailoring happens in the clauses around it,
> not by rewriting this each time.}}

### Opener (pick 0–1 — sets the tone)
- **Plain:** omit the opener; start with the Core. Straightforward, safe default.
- **Signature hook:** {{one punchy line that captures your professional identity in a single
  image or contrast — write this once, reuse it}}
- **JD-echo:** one line echoing the posting, e.g. "For N years I've done exactly what this role
  describes." Strongest when you lift or paraphrase a phrase straight from the JD.

### Emphasis clause (swap the ONE clause matching the role's focus)
- **{{Role type 1, e.g. Backend / API}}:** {{clause}}
- **{{Role type 2, e.g. Frontend / web}}:** {{clause}}
- **{{Role type 3, e.g. Leadership / architecture}}:** {{clause}}
- **{{Role type 4, e.g. Data / adjacent domain}}:** {{clause}}

### Optional specialty line (include for roles where it's relevant; drop otherwise)
> {{A line about a specific differentiator you want to surface only for some roles — an
> AI/tooling practice, a domain specialty, a leadership scope. Keep this modular so it's easy
> to include or drop per resume.}}

### Mission line (fill the {Company} clause, or drop if there's no honest hook)
- **{{Industry pattern 1}}:** {{a genuine personal angle tied to that industry — only use if
  it's actually true}}
- **Other:** tie an honest personal angle to {Company}'s mission, or omit — don't force it.

---

## Experience — {{Employer Name}} ({{City, State}}) · {{Start date}} – {{End date / Present}}
**{{Title progression, e.g. "Software Engineer → Senior Engineer / Tech Lead"}}**

Career-arc note *(optional)*: {{if your role's scope grew significantly over time, note that
here so a resume drafted for an earlier-career-flavored JD doesn't undersell tenure, or one for
a senior JD doesn't overclaim on skills you grew into later}}.

Context line (reframe per role):
> {{1-2 sentences framing this job's mission and stack in disclosure-clean terms — this is the
> line that gets lightly reworded per resume to match the target role's emphasis}}

### Theme: {{e.g. "Backend systems, APIs & architecture"}}
- {{Bullet — specific, real, with a metric where you have one. Lead with the verb and the
  outcome, not the task.}}
- {{Bullet}}
- {{Bullet}}

### Theme: {{e.g. "Infrastructure, reliability & ownership"}}
- {{Bullet}}
- {{Bullet}}

### Theme: {{e.g. "Leadership & mentorship"}}
- {{Bullet}}
- {{Bullet}}

<!-- Add a "Theme:" block per employer, or per major project within a long tenure. Keep each
     bullet traceable to source/ and, ideally, mirrored in accomplishments.yaml with the real
     metric and evidence pointer — see EVIDENCE-DISCIPLINE.md. -->

## Honest scope notes (library — pick 2-3 per resume that match the JD's likely gaps)

<!-- Pre-empting a real gap reads as senior candor, not weakness. Write these once, each
     naming a specific gap plus the closest real adjacent experience, so /tailor-resume can
     pick the 2-3 most relevant to a given JD instead of improvising one under pressure. -->
- **{{Gap 1}}:** {{honest framing + closest real transferable experience}}
- **{{Gap 2}}:** {{honest framing + closest real transferable experience}}
- **{{Gap 3}}:** {{honest framing + closest real transferable experience}}

---

## Worked example (fictional — for illustration only, delete once you've filled in your own)

> **Identity:** Jordan Casey · Austin, TX · jordan.casey@example.com · linkedin.com/in/jordancasey
>
> **Core:** "Backend engineer with 8 years building and operating payment infrastructure at
> scale, currently leading the redesign of a checkout system processing $40M+ in monthly
> volume. I move fluidly between whiteboarding a service-decomposition plan and debugging a
> production incident."
>
> **Emphasis clause (Backend / API):** "architecting REST and event-driven APIs across a
> microservices fleet, with a focus on idempotency and failure isolation."
>
> **Honest scope note:** "**Kubernetes at scale:** my production experience is Docker Compose
> and a managed ECS setup, not raw Kubernetes — I've run local k8s for side projects and can
> ramp quickly, but I want to name this rather than imply deep production k8s ops experience
> I don't have."
>
> This is the level of specificity every real entry in this file should hit: concrete, honestly
> scoped, and traceable to something you actually did.

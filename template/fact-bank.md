<!--
FACT BANK — master reusable resume content.
This is A SOURCE OF TRUTH for facts, alongside skills-matrix.md. Never invent numbers; pull
narrative bullets from here and skill lines from skills-matrix.md.
CANONICAL LAYERS — there are two, and they live in template/:
  - SELECTION layer = this file (narrative bullets, Summary, Experience) + skills-matrix.md
                       (skill lines). Curated, disclosure-clean, reframed per role.
  - DEPTH layer      = accomplishments.yaml. Structured, metric-bearing, evidence-linked into
                       source/ — the evidence the selection layer is distilled from, not itself
                       a resume source. A detail that lives only here needs to be promoted into
                       this file (or skills-matrix.md) before a bullet can use it.
Anything else that looks like a "full resume" is a RENDERING, not a source. Do not maintain
one by hand — two places holding the same fact is how they drift apart.
See EVIDENCE-DISCIPLINE.md for how source material becomes a fact here.
Workflow: copy template/resume-template.md -> resumes/drafts/md/, then fill slots by SELECTING
and RE-FRAMING bullets from this file (and skill lines from skills-matrix.md) toward the target
job description.
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

Build the Summary as: **CORE (fixed) with one EMPHASIS clause dropped into it, tuned to the
role, + [optional additional line for a specialty] + [optional MISSION line].** No opener — see
"Resume house style" below. Light tailoring only — the Core stays put, and the only slot that
moves per resume is the emphasis clause.

### Core (write once, keep ~verbatim across every resume)
> {{2-4 sentences establishing who you are professionally: years of experience, your core
> competency, and one concrete anchor — a current role, a flagship project, a notable scale. One
> sentence should carry a slot for the emphasis clause below. This is the one paragraph every
> resume shares; tailoring happens in the clause dropped into it, not by rewriting this each
> time.}}

### Emphasis clause (swap the ONE clause matching the role's focus)
- **{{Role type 1, e.g. Backend / API}}:** {{clause}}
- **{{Role type 2, e.g. Frontend / web}}:** {{clause}}
- **{{Role type 3, e.g. Leadership / architecture}}:** {{clause}}
- **{{Role type 4, e.g. Data / adjacent domain}}:** {{clause}}

### Optional specialty line (include for roles where it's relevant; drop otherwise)
> {{A line about a specific differentiator you want to surface only for some roles — an
> AI/tooling practice, a domain specialty, a leadership scope. Keep this modular so it's easy
> to include or drop per resume.}}

### Mission line (OFF by default — include only for a genuinely strong, honest hook)
A generic "I admire your mission" line reads as filler and costs more than it earns; only add
one when the tie is real, specific, and would survive a skeptical read. **Select it from the
"Company-specific hooks" section below — never manufacture one per-resume.**
- **{{Industry pattern 1}}:** {{a genuine personal angle tied to that industry — only use if
  it's actually true}}
- **Other:** tie an honest personal angle to {Company}'s mission, or omit — don't force it.

---

## Resume house style (BINDING — applies to every generated resume)

These are not suggestions — a generated draft that violates them is not finished. The goal is a
resume that reads like a person wrote it once and meant it, not one visibly assembled to hit
every keyword in the posting. Tune the specific numbers in rule 5 to your own voice and target
page count; the discipline of having ONE binding default instead of re-deciding style per resume
is the part worth keeping.

1. **Bullets are two sentences, not one em-dash chain.** Write `**Bold lead-in.** A complete
   sentence carrying the evidence.` — a period after the lead-in, never ` — ` continuing into a
   trailing clause. The dash-continuation form is one of the most recognizable AI-text tells,
   and some employers explicitly screen for it.
2. **No opener, no throat-clearing.** The Summary starts on the Core's first word. Never open a
   resume by restating what the role asks for ("This role calls for someone who…", "For years
   I've done exactly what this posting describes…").
3. **No meta-commentary explaining a bullet's relevance.** Cut every "…the same kind of work
   this role describes" / "…which is exactly what this posting is looking for." State the fact
   and let the reader draw the line themselves.
4. **A default section shape** — pick the sections that always appear (Summary · What I bring ·
   Technical Skills · Experience · Education/Certifications is a proven default) and make
   Projects / Honest scope notes **off by default**, added back only when a specific role earns
   them (a real hook for Projects, a Flag worth pre-empting for Honest scope notes).
5. **A target word count and bullet count**, so length is checkable instead of asserted.
   {{~900-1,100}} words and {{~20-25}} bullets total is a reasonable starting point for a
   one-to-two-page resume — pick numbers that fit your own target length. If a draft runs long,
   cut whole bullets rather than shortening every bullet into a stub; the strongest three
   bullets in a sub-section beat five average ones.

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
- {{Bullet — two sentences per the Resume house style above: "**Bold lead-in.** Evidence
  sentence." Specific, real, with a metric where you have one. Lead with the verb and the
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

## Honest scope notes (library — OFF by default per house style; pick 2-3 only when a Flag earns it)

<!-- Pre-empting a real gap reads as senior candor, not weakness. Write these once, each
     naming a specific gap plus the closest real adjacent experience, so /tailor-resume can
     pick the 2-3 most relevant to a given JD instead of improvising one under pressure. -->
- **{{Gap 1}}:** {{honest framing + closest real transferable experience}}
- **{{Gap 2}}:** {{honest framing + closest real transferable experience}}
- **{{Gap 3}}:** {{honest framing + closest real transferable experience}}

---

## Company-specific hooks

<!-- `/cover-letter` opens paragraph 3 from a "genuine established connection," and the Summary
     kit's mission line above needs the same kind of thing. Both are the highest fabrication
     risk in the whole repo — a fake personal connection to a company reads worse than no
     personal paragraph at all, and it's exactly the kind of thing an interviewer follow-up
     question exposes. This section exists so those hooks are SELECTED from something real and
     verifiable, never manufactured per-letter under deadline pressure.

     Add an entry only when you have an actual, checkable connection to a company you're
     applying to: genuine product use, a personal/professional tie, a specific shared value.
     Note the date you confirmed the detail and keep the framing conservative — real but light
     beats real but oversold. If a fact could go stale (an org-chart relationship, a role that
     might have changed), flag it explicitly so a future draft re-verifies before reusing it
     rather than trusting a stale note at face value. Delete an entry once the application it
     was written for closes, or keep it if the connection is durable and you're likely to apply
     to the same company again. -->

- **{{Company name}}:** {{The real, verifiable connection — what it is, how you know it's true,
  and how strong a claim it honestly supports. Confirmed {{date}}.}} *({{Optional: a caveat on
  how hard to lean on this, or a flag to re-verify before reuse — e.g. "light, don't write
  'regular user'" or "verify the corporate relationship hasn't changed before reusing."}})*

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

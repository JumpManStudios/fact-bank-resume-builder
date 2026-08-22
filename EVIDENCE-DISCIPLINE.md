# Evidence Discipline

How raw material becomes a publishable claim in this repo.

Each practice below earned its place for a concrete reason, noted where it helps. This file is
process, not personal content — it should need little to no editing when you fork this repo.

---

## 1. The three layers

```
source/            EVIDENCE      verbatim · private · names anything
    ↓
template/          CANONICAL     curated · disclosure-clean · where truth lives
    ↓
resumes/           RENDERED      generated per role · disposable
```

Material flows downward. The fact bank is the authority; a resume reflects it.

### `source/` — evidence

The record of what was written, and when. Task rows, appraisals, scorecards, old resumes,
session summaries, certificates.

**Practices:**

- **Preserve documents exactly as written.** Typos, wrong dates, a spreadsheet with a stray
  value in the wrong column — all of it stays. The record is valuable *because* it is
  untouched, and a defect is often informative in its own right.
- **Transcribe, don't edit.** Collapse whitespace for readability; leave everything else alone.
- **Let `source/` name things freely.** Employer names, project codenames, coworker names,
  hostnames, ticket IDs, internal incident nicknames. Genericization happens at the boundary
  into `template/`, not here.
- **Give every derived file a provenance header** naming its origin file, the conversion date,
  what was omitted and why, and whether each date or figure is documentary or inferred.
- **Commit the originals.** If a document is worth keeping, it goes in the durable store. The
  repository is what survives a laptop.

### `template/` — canonical

Three files hold truth, in two layers:

| File | Role | Contains |
|---|---|---|
| `fact-bank.md` | **Selection** layer | Curated, disclosure-clean bullets, reframed per role |
| `skills-matrix.md` | **Selection** layer | Curated, disclosure-clean skill lines, reframed per role |
| `accomplishments.yaml` | **Depth** layer | Structured entries with metrics, `confirm:` flags, `evidence:` pointers into `source/` |

**Keep truth in these files and generate everything else.** A "master full resume" is a
rendering produced on demand. When the same fact lives in two maintained places, the copies
drift quietly, and the drift surfaces only when something ships wrong. The depth layer is not
itself a resume source — a metric or detail that lives only in `accomplishments.yaml` needs to
be promoted into `fact-bank.md` (or `skills-matrix.md`) before a bullet can cite it, and it
needs to actually be corroborated by its own `evidence:` pointer first, not just copied forward
because it's already written down somewhere.

### `resumes/` — rendered

Generated per application from the canonical layer. The `.md` drives its own `.docx`.

---

## 2. Annotating a historical document

Annotations work well when they carry **processing status** and **pointers**:

> `**Added to fact-bank.md 2026-08-08**`
> `**Resolved 2026-08-08**: see template/fact-bank.md for the canonical figure.`

**Point at where the fact lives rather than repeating the fact.** A pointer stays correct
through every future correction. A repeated value ages on its own schedule, and nothing links
it back to the original.

*Why it matters:* a value copied instead of pointed-to has, in practice, drifted from the
source it was copied from and then propagated the wrong figure into a canonical file, costing
two edits in two files to unwind. A pointer would have needed none.

---

## 3. Extraction procedure

1. **Convert** with the right tool: `pandoc` for `.docx`/`.rtf`, a spreadsheet library for
   workbooks, PDF content-stream inflation when a rendering dependency is unavailable.
2. **Map spreadsheet columns by header name**, not position. A shifted or duplicated header
   cell can silently shift every index by one and produce a plausible-looking output with
   values read from the wrong fields. Name-based lookup is immune to this.
3. **Bound every pass by the same sections.** When sections are deliberately omitted, each
   later pass respects those same boundaries — including quick regex sweeps for a single
   detail. A document-wide scan reintroduces exactly what the boundaries excluded.
4. **Header the output** with source, date, omissions, and evidence tier.
5. **Verify the result.** Grep for content that should be absent. Compare row counts to the
   source. Confirm a low count reflects real emptiness rather than silent dropping.

---

## 4. Evidence tiers

Label which tier a claim comes from.

| Tier | Meaning | Example |
|---|---|---|
| **Documentary** | Read off the artifact itself | "Valid Through: December 31, 2028" on a certificate |
| **Corroborated** | Two independent sources agree | A certificate's issue date matches a performance review describing the credential as newly earned |
| **Self-reported** | Stated by you in a document you authored | "build times from 30+ minutes to ~10" in a self-appraisal |
| **Company-reported** | Asserted by an employer in official material | ">99% operational availability" in contract-capture material |
| **Verbal** | Stated in a working session, no paper trail | An incident's internal nickname |

Self-reported and company-reported figures are usable when tagged as such in the bullet.
**Give a shaky number a `confirm:` flag** in `accomplishments.yaml` — that keeps the lead
while making the verification step explicit.

---

## 5. Correcting a canonical value

1. **Fix it in `template/`.** That is the one place it needs to change.
2. **Grep the repo for the old value.** Wrong figures rarely sit in one file.
3. **Check `resumes/submitted/` first** if the value may already have gone out. What shipped
   matters more than what's in the repo.
4. **Leave the historical documents as they are.** They correctly record what was believed then.
5. **Record what forced the correction** alongside the new value, so the next reader sees the
   reasoning rather than repeating the research.

---

## 6. Sensitivity

Two questions decide handling.

**Whose data is it?**

- *Your own* — self-appraisals, manager reviews about you, certificates. You're the subject and
  make an informed call. Commit them; the preservation value is real.
- *Someone else's* — a scorecard naming real people with candid written assessments.
  **Reserve real caution for this case.** Spreading equal caution across everything dilutes it
  where it counts.

**Where is it going?** `source/` may name anything. The disclosure rules atop `fact-bank.md`
(if your situation needs any — see `CLAUDE.md`) apply at the boundary into `template/`: generic
descriptors for anything you can't name, specifics kept vague where needed, everything else
fine to publish as-is. Internal nicknames belong in conversation.

---

## 7. Practices earned the hard way

- **Test a capability before concluding it's unavailable.** A format was written off multiple
  times because one tool lacked a rendering dependency; a lower-level workaround resolved it
  immediately. A tool failing is narrower than the task being impossible.
- **Read the destination before describing what it lacks.** Items reported missing from
  `fact-bank.md` are sometimes already in it — check before concluding a gap exists.
- **Match the preservation mechanism to the preservation goal.** Advice to keep records
  long-term while excluding them from the only durable store is self-defeating. Worth keeping
  means committed.
- **Trace numbers to a primary source.** A compiled synthesis is a lead, not a citation. A
  headline figure that only lives in a summary document still carries a `confirm:` flag until
  the primary is found.
- **Look for corroboration across unrelated sources.** Two documents that agree on a date or
  fact without either author coordinating with the other is real corroboration, worth noting
  when it happens.

---

## 8. Checklist

Before a fact reaches a resume:

- [ ] Traceable to `source/`, or explicitly tagged verbal
- [ ] Present in `fact-bank.md` or `skills-matrix.md` (a detail that lives only in
  `accomplishments.yaml` isn't enough on its own — promote it into one of those two first)
- [ ] Evidence tier known, and labelled if self- or company-reported
- [ ] Disclosure rules applied, if you have any: generic descriptors, sensitive specifics vague
- [ ] Shaky numbers carry a `confirm:` flag
- [ ] Numbers checked against a primary source

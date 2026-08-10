---
description: Fold an editor-reviewed resume/cover-letter .docx back into its .md source, verify the render matches, and finalize the single in-review copy
argument-hint: [path to the returned .docx, or a role/company name to match] 
allowed-tools: Read, Write, Edit, Glob, Bash
---

You are reconciling an editor's review back into the source of truth. The editor reviews in Google Docs and hands back a `.docx` in `resumes/in-review/returned/`. Your job: make the `.md` match the editor's final wording **exactly**, catch anything the editor missed or broke, render a comparison copy, and — only once it's clean — finalize to a single in-review copy.

This is an **iterative loop with a human in the loop**. You never touch Google Docs. The user applies residual fixes there by hand, redownloads into `returned/`, and reruns this command. You run until the only differences left are the agreed corrections, then finalize.

## Inputs
- **Returned `.docx`:** `$ARGUMENTS` if given (a path, or a role/company name to match). Otherwise look in `resumes/in-review/returned/` — if exactly one `.docx` is there, use it; if several, list them and ask which; if none, say so and stop (a file here is the to-do signal).
- **The `.md` source:** the matching draft in `resumes/drafts/md/` (same Company-Role; match by filename stem). If you can't confidently match it, ask. The `.md` is the source of truth — you edit it, never the `.docx`.

## Hard rules (read `CLAUDE.md` and `EVIDENCE-DISCIPLINE.md`)
- **Never invent a fact.** If the editor introduced a claim, technology, or metric, it must trace to `template/fact-bank.md`. If it doesn't, **pause and flag it** — do not fold it in silently. Editor passes routinely introduce new facts; durable ones belong in `fact-bank.md` too (tell the user), but only after they confirm the fact is real.
- **Disclosure rules apply, if you have any** (banner atop `fact-bank.md`): generic descriptors for anything you can't name, sensitive specifics stay vague. If the editor's wording reintroduced a raw internal term, genericize it and flag it.
- **Comments are discussion, not content.** Never write a comment's text into the `.md`. Surface them to the user and archive them (see step 2).
- **The `.md` is the source of truth**; the `.docx` is rendered output. Render only through `template/render-resume.sh` (never raw pandoc — it applies the bullet-spacing cleanup).
- **Style:** honor the writing-style rules in `CLAUDE.md` (watch em dashes in prose). Editors often *remove* em dashes; match their final wording.

## The loop

### Mode A — reconcile + verify (default, every run)

1. **Locate** the returned `.docx` and its `.md` source (see Inputs).

2. **Read the editor's final wording and comments:**
   ```
   python3 template/review-docx.py text "<returned.docx>"
   ```
   This prints the final text (Word tracked changes already resolved — insertions kept, deletions dropped) and every comment as `[author] text`. Handles all three cases the editor might use: Word tracked changes, direct text edits, and comments.
   - **Surface the comments** to the user verbatim, with your read on each (e.g. "this comment suggests adding X; that traces to fact-bank line N" or "this is a question for you").
   - **Archive them** by appending to `resumes/in-review/returned/{stem}-review-notes.md` (create if absent) with a dated heading, so the conversation survives even after the docx is cleared. Comments never enter the `.md`.

3. **Diff the editor's final text against the current `.md`** and classify every change:
   - **Mechanical** (punctuation, em-dash removal, `&`→`and`, `on-prem`→`on-premises`, spacing, de-spaced slashes, section-heading tweaks): **apply to the `.md` exactly**, matching the editor's wording. Keep the `.md`'s straight quotes/apostrophes — the docx renders curly automatically; don't convert.
   - **Fact / claim changes** (a new metric, technology, reworded accomplishment, a new bullet or section): **pause and verify against `fact-bank.md`.** Apply only what's supported; flag anything that isn't.
   - **Judgment calls** (which framing to keep, a placeholder heading, whether to keep an off-topic bullet): **ask the user**, with a recommendation.

4. **Re-review the updated `.md`** for problems the editor introduced while typing directly, or changes they missed:
   - dropped/ doubled punctuation (a missing period after a merged clause), broken or run-on clauses, subject/verb drift, a half-finished sentence, a placeholder left in (e.g. a "TODO"-style heading).
   - **Do not silently fix these.** List them with a proposed correction and let the user decide — some are style judgment calls.

5. **Render a comparison copy and content-diff it:**
   ```
   template/render-resume.sh "<md>" "resumes/drafts/<Company>-<Role>-COMPARE.docx"
   python3 template/review-docx.py diff "<returned.docx>" "resumes/drafts/<Company>-<Role>-COMPARE.docx"
   ```
   Report the deltas in **two buckets**:
   - **Agreed corrections** — differences you expect (e.g. a period you added, a placeholder heading you replaced). These are fine.
   - **Residual discrepancies** — anything else. These are the things the user needs to fix **by hand in the Google Doc**, since the `.md` now reflects the intended content.

6. **Pause and hand back.** Tell the user exactly what (if anything) to fix in the Google Doc, then: they edit the Doc → redownload into `resumes/in-review/returned/` → rerun `/apply-review`. Loop A until the diff comes back with **only agreed corrections** (ideally `CONTENT IDENTICAL`).

### Mode B — finalize (only when clean, and only with confirmation)

When the mode-A diff is clean (nothing but agreed corrections), **offer** to finalize. Because this deletes and moves files, print the exact plan and wait for a "yes":

1. Delete the comparison render `resumes/drafts/<Company>-<Role>-COMPARE.docx`.
2. `mv` the returned `.docx` over `resumes/in-review/<same name>.docx` so there's a **single** in-review copy (overwrite).
3. Leave `resumes/in-review/returned/` holding only its `README.md` and the `{stem}-review-notes.md` log (the returned `.docx` is consumed by the move; the notes log stays as the record).

Then report:
- The `.md` is the reconciled source of truth; the single in-review `.docx` matches it (content-verified).
- Any **durable facts** the editor introduced that should be retro'd into `template/fact-bank.md` (list them) so the next role's draft has them.
- Remind the user this is ready to commit, and what the next pipeline step is (submit, or another review round).

## Notes
- If pandoc/render is unavailable, do steps 1–4 anyway (the `.md` reconciliation is the valuable part) and tell the user the comparison render is skipped.
- Keep `PIPELINE.md` in mind: reconciling a review doesn't change a role's status by itself, but if this pass means the resume is going back out or is finished, update the row per `CLAUDE.md`.

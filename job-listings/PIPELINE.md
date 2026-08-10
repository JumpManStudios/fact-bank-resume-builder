# Job Pipeline

The at-a-glance dashboard for the job hunt. One row per role. This is the **durable record** —
the JD `.md` files and resumes are the working artifacts; this table is the memory.

**Status legend (funnel order, furthest along first):**

| | Status | Means |
|---|---|---|
| 🟢 | offer | |
| 🔵 | interviewing | |
| 🟡 | applied | submitted to the company |
| 📝 | with editor | sitting in `resumes/in-review/` right now |
| ✏️ | drafted | `.md` written, **not** sent to the editor yet |
| ⚪ | prospect | found and screened, no draft yet |
| ⚫ | unlikely | not pursuing |
| 🔴 | closed | rejected / declined / withdrawn / posting pulled |

**How it works**
- Add a row when a JD comes in (status ⚪). Update the Status cell as things move; rows stay put
  within the Active table.
- **Active rows sit roughly in funnel order.** Don't re-sort on every transition — it's a
  reading aid, not a rule.
- **When a role closes:** set the outcome + date, **move the row to the Closed table**, move
  its `.md` sources to `resumes/archive/`, and **delete the JD `.md`** (it's git-tracked, so
  recoverable). That's one row move over a role's whole life.
- **Closed rows are kept indefinitely.** They cost one line and they answer questions nothing
  else can: whether you've already been rejected somewhere, and when you become eligible to
  reapply. Record a **Reapply** date whenever the JD states a window.
- Keep long shots in `unlikely/` and mark them ⚫.
- **Detail lives below the table**, one section per role: fit, gaps, flags, file paths, history.
  The table stays scannable; the details stay findable.

**File locations**
- `.md` sources in `resumes/drafts/md/` · rendered drafts in `resumes/drafts/` · out with an
  editor in `resumes/in-review/` (marked-up copies come back into `resumes/in-review/returned/`)
  · what actually went out in `resumes/submitted/` · finished applications' sources in
  `resumes/archive/`.
- Naming: `{{Your-Name}}-{Company}-{Role}-{YYYYMMDD}.md` (see `template/README.md`).

**The editor loop** *(skip this section if you're not using a human editor)*
- Render to `resumes/in-review/`, share for review, and put whatever comes back in
  `resumes/in-review/returned/`. It can go around more than once. A file sitting in `returned/`
  means its changes have **not** been retro'd yet, so that folder is the to-do list, not
  storage.
- **After the editor passes:** retro the changes back into the `.md` sources in
  `resumes/drafts/md/`, then clear `returned/`. An editor pass routinely introduces facts and
  framings that exist nowhere else, and the returned copy is the only record of them until
  they're folded in. Anything durable (new certs, new company hooks, new origin stories) goes
  into `template/fact-bank.md` too, or the next role's draft won't have it.
- **Single-file applications:** some portals allow only one upload. When the cover letter and
  resume are merged into one document, keep both `.md` sources separate and note the merge (and
  the assembly order) in each file's header and in the role's section below.

---

## Active

| Status | Company | Role | Comp | Applied | Next |
|---|---|---|---|---|---|
| _(no rows yet — add one per `/screen-jd` run)_ | | | | | |

## Closed

| Company | Role | Applied | Outcome | Reapply |
|---|---|---|---|---|
| _(no rows yet)_ | | | | |

---

# Role detail

<!-- One section per company, one sub-section per role, added as rows move through the table
     above. See the original repo this template is based on for a worked example of the level
     of detail that's useful here: fit, gaps, flags, file paths, and a running history. -->

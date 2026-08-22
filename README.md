# fact-bank-resumes

A template repo for running a job hunt like an engineering project: one fact bank as the
single source of truth, generated (never hand-invented) resumes and cover letters per
application, and a durable pipeline record so you always know where you stand.

This is a **skeleton** — the workflow and the slash-command tooling, with all example content
replaced by `{{PLACEHOLDER}}` tokens and a small fictional walkthrough. Fork it, fill in your
own facts, and it becomes your working repo.

## Why this exists

Tailoring a resume per job listing is repetitive and error-prone by hand: it's easy to
accidentally invent a number, forget which version went where, or lose track of which company
already rejected you. This repo turns that into a small pipeline:

```
JD comes in  →  screen it fast  →  tailor a resume + cover letter from ONE fact bank
             →  never invent a fact  →  track outcome in a durable pipeline table
```

The core discipline: **there are two layers that hold truth** — a selection layer
(`template/fact-bank.md` for narrative bullets, `template/skills-matrix.md` for skill lines)
and a depth layer (`template/accomplishments.yaml`, the evidence the selection layer is
distilled from, not a resume source on its own). Every resume, cover letter, and
interview-prep sheet is *generated* from them, never maintained by hand as a separate copy. See
`EVIDENCE-DISCIPLINE.md` for the full model of how raw material becomes a publishable claim.

## Quickstart

1. **Fork/clone this repo.**
2. **Fill in `template/fact-bank.md`** — replace the `{{PLACEHOLDER}}` blocks with your real
   identity, experience, and disclosure rules (see the banner at the top of that file for what
   a disclosure rule is and why you might need one).
3. **Fill in `template/skills-matrix.md`** and **`template/accomplishments.yaml`** the same way.
4. **Read `CLAUDE.md`** — if you're using this with Claude Code (or another agent that reads
   project instructions), it documents the directory map, the hard rules, and the writing-style
   defaults the slash commands assume.
5. **Use the slash commands** in `.claude/commands/` to run the pipeline: `/jd-to-md`,
   `/screen-jd`, `/tailor-resume`, `/cover-letter`, `/prep-sheet`. Each command's full
   instructions live in its own file.
6. **Track everything in `job-listings/PIPELINE.md`** — one row per role, status kept current
   in place, closed rows kept forever as your record.

Not sure this actually produces something real? See **[`examples/`](examples/)** — one
fictional job application walked through the entire chain, every artifact committed as proof.

## Using another coding agent

The workflow is not tied to Claude Code. The files in `.claude/commands/` are ordinary
Markdown instructions; Claude Code's slash commands are a convenient way to discover and run
them. An agent that can read and write repository files and run shell commands can follow the
same process directly.

- **Claude Code:** run a slash command, for example
  `/prep-sheet resumes/drafts/md/Name-Company-Role-20260815.md`.
- **Codex:** the root [`AGENTS.md`](AGENTS.md) supplies the project entry point. Ask Codex to
  follow `.claude/commands/prep-sheet.md` with the resume path as its input.
- **Another coding assistant:** ask it to read `CLAUDE.md` for the binding project rules, then
  read the relevant `.claude/commands/<workflow>.md` file and follow it with your input path.
  If the assistant does not automatically load project-instruction files, name both files in
  your prompt.

When reading a command file outside Claude Code, translate these conventions:

- `$ARGUMENTS` means the path and optional notes supplied after the command name.
- `description` and `argument-hint` frontmatter describe the command.
- `allowed-tools` and names such as `Read`, `Write`, `Glob`, `Grep`, and `Bash` describe
  capabilities. Use the equivalent file, search, and shell tools in your assistant.
- `CLAUDE.md` is loaded automatically by Claude Code. Other assistants must read it explicitly
  unless they support a repository instruction file such as `AGENTS.md`.

For example, a client-neutral request is:

```text
Read CLAUDE.md and .claude/commands/prep-sheet.md. Follow the prep-sheet workflow with
resumes/drafts/md/Name-Company-Role-20260815.md as $ARGUMENTS.
```

When exercising the fictional walkthrough, also say to treat `examples/` as the workflow
root; [`examples/README.md`](examples/README.md) explains the path mapping.

## What's genuinely reusable here

- **The fact-bank pattern** — one curated file selects and reframes bullets per role; nothing
  is invented per-application, so drift and fabrication both become structurally hard.
- **The evidence-tier model** (`EVIDENCE-DISCIPLINE.md`) — a real answer to "how sure am I
  actually of this number," with a place to put self-reported vs. documentary vs. corroborated
  claims and a `confirm:` flag for anything shaky.
- **Disclosure discipline** — if you work somewhere with things you can't say publicly
  (classified, proprietary, NDA'd), the fact-bank banner pattern is a real, repeatable answer
  to "how do I write about this work without saying the thing I can't say."
- **The pipeline table** — a durable, low-effort record of every role you've touched, so you
  never accidentally re-apply somewhere that already rejected you, and always know what's
  waiting on you.

## What you'll need to fill in yourself

- Your own identity block, experience, and skills in `template/fact-bank.md` and
  `template/skills-matrix.md`.
- Your own disclosure rules, if any apply to your situation.
- Your own `template/reference.docx` (a Word doc pandoc uses purely for its styles), if you
  want personalized `.docx` styling — a small generic default ships so rendering works out of
  the box; see `template/README.md` for the gotcha around building your own cleanly.
- Real reviewed cover letters, over time, to anchor `/cover-letter`'s voice — the template
  works from day one, but gets better once you have your own edited examples to point it at.

## Directory map

| Path | What lives there |
|---|---|
| `job-listings/*.md` | Converted JDs (one per role), each with a `## Flags` section for traps/constraints. `PIPELINE.md` is the durable record — the JD `.md` files and resumes are working artifacts that can be deleted once a role closes; the PIPELINE row stays. |
| `template/fact-bank.md` | **The source of truth for narrative facts** (bullets, summary, experience). Every resume/cover-letter bullet is selected and reframed from here, never invented. |
| `template/skills-matrix.md` | **The source of truth for skill claims.** Canonical "Technical Skills" lines + which to lead with, by role type — selected and reframed the same way, never invented. |
| `template/resume-template.md` | The `{{slot}}` skeleton `/tailor-resume` copies and fills. |
| `template/cover-letter-template.md` | Structure, voice constraints, and skeleton for cover letters. |
| `template/accomplishments.yaml` | Structured store of curated real work (bullet + what-I-did + real metric + evidence pointer) — feeds `/prep-sheet`. |
| `template/reference.docx` | Pandoc style carrier for `.docx` rendering. Ships with a small, generic default — see `template/README.md` for how to swap in your own. |
| `resumes/drafts/md/` | `.md` sources for in-progress applications. The `.md` is always the source of truth; never hand-edit rendered output. |
| `resumes/drafts/` (root) | Rendered `.docx`/`.pdf` for in-progress applications. |
| `resumes/in-review/` | Out with a human editor, if you use one. |
| `resumes/in-review/returned/` | What the editor sent back, with their markup — a to-do list to fold into `drafts/md/`. |
| `resumes/submitted/` | What actually went out. |
| `resumes/archive/` | `.md` sources for finished applications — kept as the record. |
| `interview-prep/` | Per-resume cheat sheets from `/prep-sheet`. |
| `analysis/` | Ad-hoc gap analyses, not part of the generated workflow. |
| `source/` | The private evidence layer — session summaries, work logs, historical resumes, certificates. See `source/README.md`. |
| `mcp/resume-curator/` | Optional local MCP server that makes `source/` + `accomplishments.yaml` semantically searchable (offline TF-IDF, no keys/network). Dev tool — see `mcp/resume-curator/README.md`. |

## Workflow chain

```
/jd-to-md <pdf>        → job-listings/{company}-{role}.md
/screen-jd <jd.md>     → fast go/no-go read, updates PIPELINE.md
/tailor-resume <jd.md> → resumes/drafts/md/…{Company}-{Role}-{date}.md, rendered .docx
/cover-letter <jd.md>  → resumes/drafts/md/…{Company}-{Role}-CoverLetter-{date}.md, rendered .docx
/prep-sheet <resume.md> → interview-prep/…-INTERVIEW-PREP-{date}.md
```

## Queryable career record (optional MCP server)

Beyond the static pipeline, `mcp/resume-curator/` is a small **read-only MCP server** that makes your
whole career record *queryable* instead of something you re-read by hand. It builds an **offline TF-IDF**
index at session start over `source/**`, `template/fact-bank.md`, and `template/accomplishments.yaml`,
then exposes five tools to an agent: `search_backlog`, `get_summary`, `search_accomplishments`,
`get_accomplishment`, and `find_evidence` (given a resume bullet, surface its backing evidence). No API
keys, no network — it works air-gapped.

```bash
cd mcp/resume-curator
npm install && npm run build       # compiles src/ -> dist/
npm run selftest -- "graphql"      # smoke test, no MCP client needed
```

The repo-root `.mcp.json` registers it for Claude Code; restart/reconnect MCP to pick it up. In this
skeleton `source/` is empty, so it builds an empty-but-functional index — fill in your own facts (or see
[`examples/`](examples/), which has a filled-in `source/` and shows real `search_backlog` /
`search_accomplishments` / `find_evidence` output against it, `RESUME_REPO_ROOT` and all) and it has
something to search. See `mcp/resume-curator/README.md` for details, including why its raw output stays
private.

## License

MIT — see `LICENSE`. Use it, fork it, strip it down further, whatever's useful.

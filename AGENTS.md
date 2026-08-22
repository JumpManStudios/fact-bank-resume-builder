# Project instructions for coding agents

Read [`CLAUDE.md`](CLAUDE.md) before changing or generating repository artifacts. Its evidence,
disclosure, source-of-truth, pipeline, and writing-style rules are binding for every agent;
the filename does not make those rules Claude-specific.

Workflow instructions live in [`.claude/commands/`](.claude/commands/). Claude Code exposes
them as slash commands. In another coding agent, open the relevant Markdown file and follow its
instructions directly.

When following a command file outside Claude Code:

- Treat `$ARGUMENTS` as the path and any optional notes supplied by the user.
- Treat `description` and `argument-hint` frontmatter as documentation.
- Treat `allowed-tools` and names such as `Read`, `Write`, `Edit`, `Glob`, `Grep`, and `Bash`
  as capability descriptions; use the equivalent tools available in your agent.
- When running the worked example, treat `examples/` as the workflow root. Resolve references
  such as `template/`, `source/`, `job-listings/`, `resumes/`, and `interview-prep/` beneath
  `examples/`, and keep generated example output there.

Do not duplicate the workflow instructions into client-specific files. The command files are
the canonical workflows unless the repository explicitly changes that policy.

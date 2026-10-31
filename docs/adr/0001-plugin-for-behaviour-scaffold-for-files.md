# ADR-0001: The kit is a plugin for behaviour and a scaffold for files

- **Status:** Proposed
- **Date:** 2026-10-31
- **Deciders:** Ed
- **Questions:** Q-002 (distribution), Q-004 (agents inside the kit's own repository)
- **Supersedes:** none

## Context

A delivery process has two halves. One is behaviour: what a role reads first, what it
writes, what it never does, which model it runs on, and the recurring motions (raise a
question, close a merge, run a review). The other is files: the backlog, the registers,
the logs, the templates for records, the validator that keeps them consistent. The
Claude Code plugin format carries behaviour well (agents, skills, hooks) and carries files
badly: a plugin's directory moves on every update and is absent in cloud sessions, which
is where the source project runs.

The kit must therefore decide how much of the process lives in the plugin and how much
is copied into the adopting repository, and who owns the copies afterwards.

## Options

### Option A: everything in the plugin

Agents, skills and the validator live in the plugin; the project holds only its data
files. Updates are one `claude plugin update`. But cloud sessions have no plugin, so no
agents and no validator; CI must install the plugin to validate; and a project cannot
extend the validator.

### Option B: everything copied

The scaffold copies agents, skills, templates and tools into the repository and the
plugin is only a delivery vehicle. Every project is self-contained, but skills copied into
`.claude/skills/` and agents into `.claude/agents/` drift from the kit with no update
path, and the plugin adds nothing once copied.

### Option C: plugin for behaviour, scaffold for files, agents in both

The plugin carries agents, skills and the one hook, and gets updates. The scaffold copies
the tracking files, the record templates, the CI workflow and **a copy of the validator**
into the repository, which then owns them. Agents are also copied into `.claude/agents/`
so cloud sessions keep the roles; they are small and change rarely. Skills are not copied:
in a cloud session the lead follows the same motions from `WORKFLOW.md`, which states
them in prose.

## Decision

Option C. The files a project edits and validates in CI must be the project's, available
offline and in the cloud; the behaviour that should improve across projects stays in the
plugin. Agents sit in both because they are the one behaviour cloud sessions cannot do
without and the cost of a stale copy is low.

## Consequences

- Easier: a scaffolded project works with nothing installed; CI runs the validator from
  the repository; a project can extend its validator.
- Harder: validator and agent updates reach adopting projects by hand (`scaffold --force`
  on chosen paths, or a diff). A later item may add a `process-kit:update` skill that
  diffs the project's copies against the plugin's.
- Work created: D-005 and D-006 record the copy rules; Q-002 asks how the plugin half is
  distributed; Q-004 asks whether the kit's own repository also carries `.claude/agents/`.
- Revisit when cloud sessions load project-scope plugins, which would let the agents live
  in the plugin alone.

## Amendments

None.

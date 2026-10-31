# Tailoring the process to a project

What to change for a new project, where it lives, and what may not change without a
decision row. Read `assumptions.md` first: it says which assumptions are fixed.

The rule for every change below: **the config, the prose and the agent file must agree**,
and the change is a row in `project/decisions.md`. The validator enforces the config; the
agents read the prose; a mismatch is a process bug the next review will find.

## What the scaffold writes and what you fill in

| File | Written by scaffold | You fill in |
| --- | --- | --- |
| `CLAUDE.md` | process sections | the project description, **the invariants**, code layout, language and build conventions |
| `project/process.toml` | defaults below | milestones, roles and models if they differ, stale period, issue mirroring |
| `project/WORKFLOW.md` | the full process | human gates specific to the project, the code directories in the tree |
| `project/milestones.md` | three placeholder rows | the real milestones with a one-line acceptance test each |
| `project/backlog/B-001` | "adopt the process" | nothing; do it and mark it `done` |
| `project/SITREP.md` | one scaffold entry | the first real handoff |
| `project/activity.md` | one `decided` row | a row per dispatch and decision from now on |
| `docs/design/nfrs.md` | goals and three generic NFRs | the project's goals; NFRs as they get fitness functions |
| `docs/adr/`, `docs/arch/`, `docs/process/` | READMEs and templates | records as they are made |
| `.github/workflows/tracking.yml` | validator CI | nothing |
| `.claude/agents/` | the eight roles | persona or tooling tweaks per role (see below) |

## Roles and models

Where: `[roles]` in `project/process.toml` **and** the `model:` line of the matching file
in `.claude/agents/` (or the plugin's `agents/` if you maintain a fork).

- To change a role's model: change both, add a decision row naming the role and the
  reason (cost, quality, a model's retirement).
- To add a role: add it to `[roles]`, write an agent file with `name`, `description`,
  `tools`, `model` and a body that says what it reads first, what it writes, and what it
  never does. Add a row to the roles table in `WORKFLOW.md`.
- To remove a role: remove it from `[roles]` and the table; items with that role fail the
  validator until reassigned. The eight shipped roles are the minimum the loop needs; the
  operator and the program manager are the ones most often dropped on a tiny project, and
  dropping the program manager also drops the process review (assumption A5).
- `model: inherit` on the researcher means the orchestrating session's model; in the
  journal that is written as `lead`.

## Milestones

Where: `backlog.milestones` in `process.toml` and the table in `project/milestones.md`.
Keep them identical. `spec` is for items that produce records rather than code (ADRs,
catalogues); `later` is a parking place that never gets a review. Renaming a milestone
means renaming it in every item's front matter; the validator will list them.

## Invariants

Where: `## Invariants` in `CLAUDE.md`. The scaffold leaves a placeholder. These are the
project's, not the kit's; the kit only insists that "humans decide, agents propose" is
among them (assumption A1) and that reviewers check PRs against them in order. Number
them so reviews can cite "invariant 3". Changing one is an ADR, not a decision row.

## Review cadence

Where: step 7 of the loop in `WORKFLOW.md`, and the `arch-review` and `process-review`
skills. Default: both reviews at every milestone boundary, both gating. Options that stay
within the kit: every other milestone, or by calendar for a long milestone. Both need a
decision row and the `WORKFLOW.md` edit. Removing the reviews is a fork (assumption A5).

## Issue mirroring

Where: `issues.mirror` in `process.toml`. `false` by default. Set `true` when more than
one implementer works at once or when reviewers live in GitHub; the operator then opens an
issue per `ready` item and closes it on `done`, and `merge-sync` checks the close. The
item file stays the source of truth either way (assumption A2).

## Statuses, priorities, stale period, question statuses

Where: `[backlog]` and `[questions]` in `process.toml`.

- Statuses: add freely (`parked`, `verifying`); never remove `ready`, `blocked`,
  `in-progress`, `review`, `done`, `dropped` (the validator refuses the config).
- Priorities: any ordered list; the index sorts by position.
- `stale_days`: 14 by default; 7 for a daily-cadence project, 30 for a quiet one.
- Question statuses: `open`, `answered`, `superseded`; adding `deferred` is common.

## The journal

Where: `[journal]` in `process.toml`, the top of `project/activity.md`, the `journal`
skill. `models` must list every value a row may carry; add a model when a role moves to
it. `outcomes` is a fixed vocabulary for counting; adding one is fine, renaming one makes
old rows invalid. `enabled = false` turns the journal checks off; the program manager then
reviews from SITREP and PR history alone, which is weaker.

## Persona of the agents

Where: the body of each file in `.claude/agents/`. Tone and voice are free; the
**contract** is not: what the role reads first, what it produces, where it writes, and
its "never" list. Keep the tools line minimal (a reviewer that can Edit will fix instead of
report). If you add project-specific reading (a plan, a catalogue, a fixture rule), add it
to the "Read first" paragraph rather than scattering it.

## Validator

Where: `project/tools/check.py`, the project's own copy. Extend it if the project needs a
check the kit does not have (a catalogue cross-reference, a link check). Keep it stdlib
only and runnable with `python3 -I`. When the kit's validator changes, diff and merge by
hand; the scaffold never overwrites it without `--force`.

## What must not change without a decision row

Anything in `process.toml`; the roles table and the loop in `WORKFLOW.md`; an agent's
model or tools; the review cadence; the journal vocabulary. The `decision` skill writes
the row; the validator cannot see prose, so the row is the only trace.

## What is a fork, not a tailoring

Two approvers; tracking outside the repository as the source of truth; an implementer
that decides; removing the reviews; letting agents close questions or accept ADRs. The
kit's agents and skills assume otherwise throughout, and a project that wants these should
copy the kit and change it rather than configure around it.

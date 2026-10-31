# process-kit

A Claude Code plugin that gives a repository an agent-and-human delivery process, with the
files, agents and checks to run it: role agents on fixed models, a Markdown backlog
validated by a script, architecture decision records that beat the spec, a questions
register only the human closes, an append-only decision log, an activity journal, dated
handoff notes, and architecture and process reviews at every milestone boundary. It was
extracted from a working project and is built to be tailored, not forked.

## The process in one paragraph

One person decides; agents do the research, planning, coding and housekeeping, and every
handoff between them is a file in the repository. A finding or question comes in and the
**researcher** writes options with a recommendation. The **approver** decides, and the
decision is recorded where it belongs: an ADR for architecture, a row in the decision log
for everything else, an answer in the questions register. The **planner** turns the decision
into backlog items with checkable acceptance criteria and explicit dependencies; a
validator refuses an item marked `ready` while anything it depends on is open. An
**implementer** takes exactly one `ready` item to a PR; a **reviewer** checks the PR against
the item's criteria and the invariants; the approver merges; the **operator** marks the item
done, regenerates the index and writes the journal row the same day. When a milestone's
last item lands, the **architect** reviews the whole system against the goals and the NFR
register, the **program manager** reviews the way of working against the journal, and the
next milestone waits on both reviews' blocking findings. The **project manager** keeps all
of it true between sessions. Agents propose and never decide.

## What is in the kit

| Path | What |
| --- | --- |
| `agents/` | eight role agents: researcher, planner, project-manager, program-manager, implementer, reviewer, architect, operator |
| `skills/` | thirteen motions: `scaffold`, `session-start`, `backlog-item`, `question`, `adr`, `decision`, `sitrep`, `status`, `check`, `merge-sync`, `arch-review`, `process-review`, `journal` |
| `hooks/` | one hook: run the validator after an edit under `project/` |
| `templates/` | every tracking and docs file the scaffold writes, with `{{PROJECT_NAME}}`, `{{APPROVER}}`, `{{DATE}}` |
| `tools/check.py` | the validator: standard library, `python3 -I`, vocabulary from `project/process.toml` |
| `tools/scaffold.py` | copies templates, the validator and the agents into a project |
| `docs/assumptions.md` | every assumption the process makes, marked tailorable or fixed, with the reason |
| `docs/tailoring.md` | what to change for a new project and where, and what needs a decision row |
| `project/` | the kit's own tracking, kept with the kit's own templates |

## Add it to a project

Two halves (ADR-0001): the plugin carries behaviour (agents, skills, the hook); the
scaffold copies files the project then owns (tracking, record templates, a copy of the
validator, the agents for cloud sessions).

**1. Scaffold the files** from a clone of this repository, from your project's root:

```
python3 -I /path/to/process-kit/tools/scaffold.py --target . --name my-project --approver "Your Name"
python3 -I project/tools/check.py
```

The scaffold never overwrites an existing file. If you already have a `CLAUDE.md`, it writes
the process sections to `project/CLAUDE-process-sections.md` for you to merge.

**2. Enable the plugin** for local, desktop and VS Code sessions (cloud sessions do not load
project plugins; they use the copied `.claude/agents/` and the prose in `WORKFLOW.md`):

```
claude plugin marketplace add edlovesjava/process-kit
claude plugin install process-kit@process-kit --scope project
```

Or, to try it for one session without installing: `claude --plugin-dir /path/to/process-kit`.

**3. Do B-001.** The scaffold leaves one `ready` item: fill the invariants in `CLAUDE.md`,
confirm roles and milestones in `project/process.toml` and `project/milestones.md`, write
the first SITREP entry, mark the item done with a journal row. From then on, start every
session with `/process-kit:session-start`.

Requirements: Python 3.11 or newer for the validator and scaffold (standard library only);
Claude Code for the plugin half.

## Tailor it

Read `docs/tailoring.md`. Roles and their models, milestones, the project's invariants,
the review cadence, issue mirroring, statuses and the stale period, the journal
vocabulary and each agent's persona are all meant to change, in `project/process.toml`,
`project/WORKFLOW.md` and `.claude/agents/`, each change with a row in the decision log.
`docs/assumptions.md` says which assumptions are fixed and why; changing one of those is a
fork, not a tailoring.

## Status

Version 0.1.0, bootstrapped on 2026-10-31 in one session from the source project's process
files. Milestones M0 (scaffold and validator), M1 (agents and skills) and M2 (templates and
tailoring docs) are built; their boundary reviews are owed and gate M3, in which the kit is
adopted by the source project and by one fresh project. The five bootstrap questions were
answered on 2026-10-31 (D-012 to D-016): MIT licence; the plugin for behaviour plus
scaffolded copies the project owns, with an update path to build (B-018); journal rows by
hand first, a competitive trial against hooks later; the kit's own repository carries
`.claude/agents/`; the name stays. Open for the approver: ADR-0001 and the bootstrap
decision rows (B-013), and the whitepaper comments (B-021). See `project/SITREP.md` for the
current handoff and `project/backlog/INDEX.md` for the plan.

Verified so far: 31 unit tests, `claude plugin validate .` (two expected warnings: the kit's
own `CLAUDE.md` at the plugin root, and no icon, which matters only for directory submission), the kit's own `check.py`, and a scaffold into an
empty directory followed by a full status walk-through (ready with an open question fails,
review without owner fails, done without a journal row warns).

## Licence

MIT; see `LICENSE`.

# How this project runs

One person ({{APPROVER}}) directs; agents do the research, planning, coding and
housekeeping. Every handoff between roles is a file in this repository, so nothing lives
only in a chat transcript. This document is the overview; the folders it names hold the
detail. The process comes from process-kit; `project/process.toml` holds the values the
validator enforces.

## Three areas, three kinds of change

| Area | Holds | Changes when |
| --- | --- | --- |
| **Code** | Software and its tests | A backlog item is implemented |
| **Docs** (`docs/`) | What we are building and why: spec, ADRs, design notes, NFR register, reviews | A decision is made or a design is refined |
| **Tracking** (`project/`) | How the work is going: backlog, questions, decisions, milestones, journal, this workflow | Any time state changes |

```
{{PROJECT_NAME}}/
  CLAUDE.md                     invariants and conventions every agent reads
  docs/
    adr/                        architecture decision records, NNNN-title.md
    arch/                       architecture reviews, one per milestone boundary
    process/                    process reviews, one per milestone boundary
    design/nfrs.md              architecture goals and the NFR register
  project/
    WORKFLOW.md                 this file
    process.toml                roles, models, milestones, statuses the validator enforces
    SITREP.md                   dated handoff notes between sessions, newest first
    activity.md                 activity journal: one row per dispatch or decision
    questions.md                open questions and their answers (register)
    decisions.md                decision log for non-architectural decisions
    milestones.md               milestone table
    backlog/                    one file per work item, B-NNN-title.md, plus INDEX.md
    tools/check.py              validates everything above and regenerates INDEX.md
  .claude/agents/               role definitions for subagents (copied from the kit)
```

## Roles and models

Work is routed by what it needs, and each role runs on the cheapest model that does it
well. The lead session is the researcher and the orchestrator; it delegates everything
else. The model column is the default from process-kit; change it in `process.toml` and
the agent file together, with a decision row.

| Role | Model | Does | Produces |
| --- | --- | --- | --- |
| **Researcher** | lead session | Reads specs, external docs and code; evaluates options; answers questions | Findings, ADR drafts with options, answers in `questions.md` |
| **Planner** | Opus | Turns accepted decisions into milestones and backlog items with acceptance criteria and dependencies | Backlog items, milestone updates, ADR final text |
| **Project manager** | Opus | Keeps `project/` true: priorities, dependencies, blocked items, stale items, open questions; refuses to mark work ready when its inputs are missing | Updated backlog, status summaries, nudges |
| **Program manager** | Opus | Owns this file and the activity journal; reviews the process at every milestone boundary; names bottlenecks with evidence | `docs/process/review-<milestone>-<date>.md`, proposed changes to this file |
| **Implementer** | Sonnet | Takes one `ready` backlog item to a PR: code, tests, docs touched by the change | A branch and PR, item moved to `review` |
| **Reviewer** | Opus | Reads a PR against its item's acceptance criteria, `CLAUDE.md` and the ADRs | Review findings; approve or request changes |
| **Architect** | Opus | At every milestone boundary, reviews the whole system against the invariants, ADRs, goals and the NFR register; ranks findings; proposes records | `docs/arch/review-<milestone>-<date>.md` |
| **Operator** | Haiku | Mechanical work: run build and tests, run `check.py`, regenerate the index, sync statuses, format, report CI | Green checks, tidy tracking files |

Rules of routing:

- A task goes **down** the table as it becomes better specified. Research produces
  options; planning produces items; implementation produces code; operations keeps it
  tidy. Anything that comes back up (an implementer hits an unknown) becomes a question,
  not an improvised decision.
- The orchestrator never implements and the implementer never decides. If an implementer
  needs a decision, it writes a `Q-NNN` entry and stops that item.
- Humans decide; agents propose. The gates below are {{APPROVER}}'s.

## The loop

```
  research ──► decide (human) ──► plan ──► implement ──► review ──► merge ──► operate
     ▲                                                      │
     └──────────────── questions raised anywhere ───────────┘
```

1. **Research.** A finding or a question comes in. The researcher writes options and a
   recommendation into an ADR draft (`Proposed`) or an answer in `questions.md`.
2. **Decide.** {{APPROVER}} accepts, amends or rejects. An accepted ADR flips to
   `Accepted`; the question flips to `answered` with a link to where it was decided.
3. **Plan.** The planner creates or updates backlog items: goal, acceptance test,
   `depends_on`, `questions`, milestone, priority. The PM runs `check.py`.
4. **Implement.** The implementer takes one `ready` item on its own branch, follows
   `CLAUDE.md`, writes tests first where the item is pure logic, opens a PR that names
   the item, and sets the item to `review`.
5. **Review.** The reviewer checks the PR against the item's acceptance criteria. Blocking
   findings go back to the implementer; design doubts become questions.
6. **Merge.** {{APPROVER}} merges. The operator sets the item `done`, regenerates the
   index, updates `milestones.md`, closes the mirrored issue if issues are on, and adds a
   journal row. This happens in the same session as the merge, never "next time".
7. **Milestone boundary.** When a milestone's last code item reaches `review`, the
   architect reviews the whole system (not the diff) against the invariants, ADRs, goals
   and NFRs, and the program manager reviews the process against the journal. Each writes
   a dated review. Proposals become questions, ADR drafts or backlog items;
   {{APPROVER}} decides. The next milestone's first code item does not start until the
   blocking findings of both reviews are decided.
8. **Operate.** Between items the operator runs the build, keeps CI green, and reports
   anything red to the PM.

## Human gates

These never happen without {{APPROVER}}:

- Accepting or rejecting an ADR.
- Merging a PR.
- Dropping a backlog item.
- Closing a question (an accepted ADR may close one on their behalf).
- Changing a goal, an NFR, a role's model, or anything in `process.toml`.
- Anything the invariants in `CLAUDE.md` reserve for the human.

## Tracking rules

- **Nothing is forgotten.** Every open thread is one of: a backlog item, a question, a
  decision awaiting the approver, or a risk recorded in a design note. If it is none of
  those, the PM makes it one.
- **Questions are first-class.** `questions.md` holds every open question with context,
  why it matters, what it blocks, and its answer when it comes. Agents add to it freely;
  only {{APPROVER}} or an accepted ADR closes one.
- **Decisions are recorded where they belong.** Architecture goes in `docs/adr/`.
  Process and scope decisions go in `project/decisions.md`. Both are append-only; a
  changed mind is a new record that supersedes the old.
- **Dependencies are explicit.** An item is `ready` only when every `depends_on` is
  `done` and every linked question is `answered`. `check.py` enforces this.
- **Status is in the file, not in anyone's head.** Statuses are listed in
  `process.toml`. The index is generated, never hand-edited.
- **The journal is the record of work.** Every agent dispatch and every human decision is
  one row in `activity.md`, written the same day. `check.py` warns when an item reaches
  `review` or `done` with no row that day.
- **GitHub issues mirror the backlog, never replace it** (when `issues.mirror` is on).
  When an item becomes `ready` the operator opens one issue titled with the item id; it
  closes on `done`. PRs reference the issue. The item file stays the source of truth.
- **Currency.** Every item carries an `updated` date. The PM flags items untouched for
  `stale_days` in its status summary.

## Running it in Claude Code

- **Push the branch first.** A cloud session pushes its branch before anything else
  (`git push -u origin <branch>`, even with no commits); otherwise the session cannot be
  teleported or opened in a terminal, because there is nothing on origin to fetch.
- A session then reads `CLAUDE.md`, `project/SITREP.md`, `project/backlog/INDEX.md` and
  `project/questions.md`, and asks the project-manager agent for status before picking
  work. A session that leaves work in flight adds a SITREP entry before it ends.
- Subagents are defined in `.claude/agents/` (copied from the kit so that cloud sessions,
  which do not load project plugins, still have them). The lead delegates with the Agent
  tool by role name; each definition fixes the model and the tools the role may use.
- Parallel implementers each take a different `ready` item on their own branch. The PM
  does not hand two implementers items that touch the same files.
- One backlog item per PR. Tracking changes that belong to a merge (status to `done`,
  index, milestones, journal row) go in a small follow-up commit on the next session's
  branch if the merge happened outside a session, and are the first thing that session does.

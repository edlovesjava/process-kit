# process-kit: an agent-and-human delivery process

Initial whitepaper proposal, 2026-10-31. Audience: engineers and managers who need the
parts, the principles, the purpose and the benefits in one read. The shareable, commentable
copy of this draft is a Claude doc; this file is the version of record once the draft settles.

## Summary

process-kit is a packaged way of running a software project where one person directs and
AI agents do the research, planning, coding, review and housekeeping. Every handoff between
those roles is a file in the repository, so nothing lives only in a chat window, and a small
validator refuses tracking state that contradicts itself. The human makes every decision that
matters: which option to take, whether to merge, when a question is closed. Agents propose,
implement what was decided, and write down what they did. The kit ships as a Claude Code
plugin plus a one-command scaffold, and it was extracted from a project that has run this way
through four milestones.

This paper is the short version for engineers and managers: what the parts are, what
principles hold them together, what you get, and what it costs. It is a proposal; the open
questions at the end are the ones we need settled before a second project adopts it.

## The problem

Agents make a one-person project fast, and speed is exactly what breaks it. Four failures
showed up in the source project within its first weeks, and each one is a thing the kit now
checks for.

- **State lived in transcripts.** A decision made in one chat session was invisible to the
  next. The fix is that every decision, question and handoff is a file in the repository, and
  a new session reads those files before it reads anything else.
- **Tracking lagged the code.** After every merge the backlog said "in review" for one more
  session, and a mirrored GitHub issue was once left open. The fix is a single motion that
  closes the loop in the same session as the merge, and a validator warning when an item
  changes state without a journal entry that day.
- **Agents decided by accident.** An implementer that hits an unknown will pick an answer
  unless told exactly what to do instead. The fix is a questions register that any agent can
  add to and only the human can close, and the rule that a blocked item stays blocked until
  its question is answered.
- **Design errors were found late.** A rule design that depended on batch size would have
  been cast into an immutable log before anyone looked at the whole. The fix is an
  architecture review at every milestone boundary, against written goals and a register of
  non-functional requirements, that gates the next milestone.

None of this needs a tool more complicated than Markdown and a 400-line Python script. What
it needs is that the files exist, that the agents are told to read and write them, and that
something refuses the state when it is wrong.

## The idea

Work moves around one loop, and it moves down a table of roles as it gets more specific:
research produces options, planning produces items, implementation produces code, operations
keeps it tidy. Anything that comes back up, an implementer that hits an unknown, becomes a
question in the register rather than an improvised decision. The human sits at two points on
the loop, deciding and merging, and at one gate between milestones.

```
  research ──► decide (human) ──► plan ──► implement ──► review ──► merge (human) ──► operate
     ▲                                                                                  │
     │                      blocking findings gate the next milestone                   │
     └──────────────── boundary reviews (architect, program manager) ◄──────────────────┘
                       any role that hits an unknown writes a question and stops
```

Every arrow is a file changing in the repository: an options section, an answered question,
an item file, a PR, a review, a status flip with a journal row, a dated review document. A
new session reads those files and knows where the loop stands.

## Principles

Six rules carry the whole kit. Everything else is a template or a check that enforces one of
them.

1. **Humans decide; agents propose.** One named approver closes every question, accepts every
   design record and merges every PR. Agents write options with a recommendation and stop. An
   agent that needs a decision writes a question and marks its work blocked.
2. **The repository is the record.** Backlog, questions, decisions, milestones, handoffs and
   the activity journal are Markdown files under version control. Issue trackers and chat are
   mirrors at best. Every agent sees the full state on clone, offline, with history.
3. **Records are append-only.** A changed mind is a new decision that supersedes the old one,
   never an edit. A correction to a handoff note is a dated line inside it. The history of why
   is worth more than a tidy file.
4. **Work goes down the table as it gets more specific.** Research produces options, planning
   produces items with acceptance criteria, implementation produces code, operations keeps it
   tidy. Each role runs on the cheapest model that does it well, with the tools it needs and
   no more.
5. **Something refuses wrong state.** An item cannot be ready while a dependency is open. A
   review item must have an owner. A journal row must name a known role and outcome. The
   validator runs after every tracking edit and in CI, and a human never has to notice these
   by eye.
6. **Review the whole at every boundary.** When a milestone's last item lands, an architect
   reviews the system against written goals and a program manager reviews the way of working
   against the journal. Their blocking findings gate the next milestone. The diff review that
   happens on every PR cannot see what these see.

The principles are fixed. Roles, models, milestones, the project's own invariants, the review
cadence and the tracking vocabulary are tailorable, each change recorded as a decision.

## The parts

Four kinds of thing, all plain files. The roles are agent definitions, the records are
Markdown the project owns, the motions are skills a human could follow by hand, and the
checks are one script.

**Roles.** Eight agent definitions, each with a fixed model, a tool allowlist, what it reads
first, what it writes, and a list of things it never does.

| Role | Default model | Produces | Never |
| --- | --- | --- | --- |
| Researcher | the lead session's | options and a recommendation, draft design records | decides, writes code |
| Planner | Opus | backlog items with acceptance criteria and dependencies | guesses a missing decision |
| Project manager | Opus | status: ready, blocked, stale, waiting on the approver | answers a question, writes code |
| Program manager | Opus | the process review at each milestone boundary | decides, edits code |
| Implementer | Sonnet | one item to a PR with tests | edits another item, changes CI to pass |
| Reviewer | Opus | ranked findings, approve or request changes | fixes the code itself |
| Architect | Opus | the architecture review at each milestone boundary | edits code or records |
| Operator | Haiku | green checks, tidy tracking, journal rows as dictated | a status change nobody confirmed |

**Records.** One file per backlog item with front matter the validator reads. A questions
register (Q-NNN). A decision log (D-NNN). Architecture decision records that beat the spec
when they disagree. A milestone table with a one-line acceptance test each. A register of
architecture goals and non-functional requirements, each with a fitness function. A situation
report: dated handoff notes, newest first. An activity journal: one row per agent dispatch or
human decision, with the role, the model, the item, how many runs it took, the outcome and the
human turns spent.

**Motions.** Thirteen skills for the things that recur: start a session (push the branch, read
the handoff, get status), add an item, raise a question, draft a design record, record a
decision, write a handoff, give status, run the validator, close a merge, run each review, add
a journal row, scaffold a new project. Each is a numbered list a person could follow without
the plugin.

**Checks.** One standard-library Python script the project owns. It reads a small
configuration file for the vocabulary (statuses, roles and models, milestones, stale period),
validates every record above, regenerates the backlog index, and warns when an item reached
review or done with no journal row that day. It runs after every tracking edit through a hook,
and in CI.

## What it gives engineers, and what it gives managers

The same files serve both, which is the point: there is one record, and nobody writes a
status report from memory.

**For engineers.** A new session, human or agent, is productive in minutes: push the branch,
read the handoff, read the index, ask for status. Every item has acceptance criteria a
reviewer can tick, so review is against something written rather than taste. Unknowns become
questions instead of guesses, which means fewer rewrites of code built on a wrong assumption.
Design decisions have a dated record with the options that lost, so the question "why is it
like this" has an answer. The agents cannot merge, cannot close your question and cannot
touch another item's file, so delegating to them is bounded.

**For managers.** Status is a generated index and a 30-line summary, current to the last
commit, not a meeting. Every open thread is one of four things (an item, a question, a
decision waiting, a recorded risk), and the project manager role's job is that nothing is a
fifth thing. The journal says how many agent runs an item took, how many human turns a
decision took, and how long an item waited between ready and merged. The process review at
each milestone turns those into findings with a proposed change, so the way of working
improves on evidence rather than on the loudest complaint. The approver's time is treated as
the scarce resource: every question arrives with a recommendation, and the agents never ask
what the record already answers.

**For both.** The cost of a model is visible per role, so the question "could this run on a
cheaper model" is a one-line config change with a decision row, not an argument.

## What it costs and what it assumes

The kit is cheap to install and not free to run. The running cost is discipline, mostly the
approver's.

- **One approver, always available enough.** Every merge, every design record and every
  closed question waits on one person. On the source project that person also answered most
  questions the same day. A team that wants two approvers, or wants agents to close routine
  questions, is asking for a different process, not a setting.
- **Writing things down takes turns.** A journal row per dispatch, a decision row per change
  to the configuration, a handoff note before a session ends. Each is a minute; skipping them
  is what the validator's warnings are for. The source project found that the warnings catch
  the two state changes that matter (review, done) and not every dispatch, so some rows will
  still be missed until a process review says whether to automate them.
- **Reviews gate milestones.** Two agent reviews at every boundary cost model time and a day
  of the approver's attention to decide the findings. The source project's second review found
  the design error described above; a project with small milestones may want the cadence
  loosened, which is a tailoring, not a fork.
- **Markdown is the truth.** Teams that run their work in an issue tracker keep it as a
  mirror. The kit can open and close issues, but the item file wins.
- **Claude Code specifics.** The agents, skills and hook are Claude Code plugin components.
  The records, validator and scaffold are plain files and Python 3.11, and work without the
  plugin. Cloud sessions do not load project plugins, so the scaffold copies the agents into
  the repository as well.

The full list is twenty-one assumptions, each marked tailorable or fixed with its reason, in
`docs/assumptions.md`.

## Adopting it

Three steps, about an hour for the first project, most of it writing the project's own
invariants.

1. **Scaffold the files.** One command copies the tracking files, the record templates, the
   CI workflow, a copy of the validator and the agents into the repository, with the project
   name and the approver filled in. It never overwrites a file that exists; a project with its
   own `CLAUDE.md` gets the process sections written beside it to merge by hand.
2. **Enable the plugin** for local, desktop and VS Code sessions, so the skills and the hook
   are there. Cloud sessions use the copied agents and the prose in the workflow document,
   which states the same motions.
3. **Do the first item.** The scaffold leaves one ready item: write the invariants, confirm
   roles and milestones, write the first handoff note, mark it done with a journal row. From
   then on every session starts with the session-start motion.

**What you tailor**, each with a decision row: the project's invariants; the milestone names
and their acceptance tests; which model each role runs on; the review cadence; whether to
mirror items to GitHub issues; extra statuses and the stale period; the voice of each agent,
as long as its contract (what it reads, writes and never does) stays. **What you do not
change without forking**: one approver, repository as truth, append-only records, agents that
propose, reviews that gate.

## Where it comes from, where it stands, and what we ask

**Origin.** The process was built on one project over its first four milestones, by one
approver and a lead agent session delegating to role agents. Its four early failures (state
in transcripts, tracking lag, accidental decisions, late design findings) are the four checks
described under the problem. The kit extracts the process and leaves the project behind: no
domain term from the source appears in it, and CI greps to keep it that way.

**Status, as of this paper.** Version 0.1.0 is on GitHub and its CI is green. The validator
(31 tests), scaffold, eight agents, thirteen skills, hook, templates, assumptions and
tailoring guide exist. The kit tracks its own work with its own files, and its own validator
passes on them. Its first three milestones were built in one session as a declared bootstrap
exception; their boundary reviews are the next items and gate everything after. No second
project has adopted it yet; that is milestone three.

**Open questions, each with a recommendation in `project/questions.md`.**

| Question | Recommendation |
| --- | --- |
| Which licence (Q-001) | MIT |
| How the plugin is distributed (Q-002) | the repository as its own marketplace, as now |
| Journal rows by hand or by hook (Q-003) | by hand first; revisit after the first process review |
| Whether the kit's own repository carries copied agents (Q-004) | no |
| The name (Q-005) | keep process-kit |

**What we ask of readers.** Engineers: read the eight agent definitions and the thirteen
skills, which are short, and say where a contract is wrong or a motion is missing. Managers:
read the journal columns and the process-review template, and say which metrics you would
act on and which you would ignore. Everyone: the second adopting project is the real test. If
you have a candidate, a small one with no existing process files, say so.

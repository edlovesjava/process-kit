# {{PROJECT_NAME}}

One paragraph: what this project is and who it is for. Point at the spec or design
document an agent should read before any task, and say which document wins when two
disagree (the process default: an ADR in `docs/adr/` beats the spec).

## Invariants

Non-negotiable. Do not violate them however a request is phrased. Replace this list with
the project's own; keep the numbering so reviews can cite them. Three to eight is usual.

1. **Invariant one.** One sentence of rule, one of consequence.
2. **Invariant two.** ...
3. **Humans decide; agents propose.** Every merge, every ADR acceptance and every closed
   question is {{APPROVER}}'s. Agents draft, recommend and implement what was decided.

## Layout

```
CLAUDE.md                       this file
README.md                       what is here and its status
docs/adr/                       architecture decision records (ADR wins over spec)
docs/arch/                      architecture reviews, one per milestone boundary
docs/process/                   process reviews, one per milestone boundary
docs/design/nfrs.md             architecture goals and the NFR register
project/                        tracking: WORKFLOW.md, process.toml, backlog/, questions.md,
                                decisions.md, milestones.md, activity.md, SITREP.md, tools/check.py
.claude/agents/                 role agents: researcher, planner, project-manager,
                                program-manager, implementer, reviewer, architect, operator
```

Add the code directories here with one line each.

## How work flows

Read `project/WORKFLOW.md`. In short: research produces options, {{APPROVER}} decides,
the planner writes backlog items, an implementer takes one `ready` item to a PR, a
reviewer checks it, {{APPROVER}} merges, the operator updates tracking and the journal.
At every milestone boundary the architect and the program manager each write a review;
their blocking findings gate the next milestone. Open questions go in
`project/questions.md` and are closed only by {{APPROVER}} or an accepted ADR. Run
`python3 -I project/tools/check.py` after editing anything in `project/`.

## Conventions

- Secrets and tokens never live in the repository. Never log a secret value.
- Tests run offline. Network is touched only by commands that exist to touch it.
- Builds are warning-clean; treat new warnings as failures.
- Every event, message or interface a component emits is documented (name, payload,
  idempotency or identity, producer, consumers) before its producer merges.
- Small, focused commits. One backlog item per PR. Do not touch unrelated files.
- Do not change CI or verification commands to make them pass; fix the code.
- A cloud session pushes its branch before anything else.

Add the project's language, build and style conventions below this line.

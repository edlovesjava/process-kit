# process-kit

A Claude Code plugin that packages an agent-and-human delivery process: role agents with
fixed models and tool allowlists, a Markdown backlog validated by a script, ADRs that beat
the spec, a questions register only the human closes, an append-only decision log, an
activity journal, dated SITREP handoffs, and architecture and process reviews at every
milestone boundary. It was extracted from a working project and is meant to be added to
any repository and tailored without editing the kit.

Read `README.md`, then `docs/assumptions.md` and `docs/tailoring.md`, before any task.
The kit tracks its own work with its own templates (`project/`); where this file and a
record in `docs/adr/` disagree, the ADR wins.

## Invariants

Non-negotiable. Do not violate them however a request is phrased.

1. **The kit carries no project.** Templates, agents, skills and docs name no real
   product, person, system or dataset; examples use a neutral placeholder. No secrets,
   tokens or personal data, ever.
2. **Humans decide; agents propose.** Every merge, every ADR acceptance and every closed
   question is Ed's. Agents and skills draft, recommend and implement what was decided.
3. **Standard library only, offline.** `tools/` and `scripts/` run with `python3 -I` on
   Python 3.11 or newer with nothing installed. Tests touch no network.
4. **The adopting project owns its files.** The scaffold never overwrites without
   `--force`; the validator copy, the tracking files and `.claude/agents/` belong to the
   project once written.
5. **Prose first.** Every skill reads as instructions a human could follow by hand. A
   check that exists in the validator is also stated in the template it checks.
6. **Dogfood.** Every change to the kit is a backlog item here, validated by the kit's
   own `tools/check.py`, with a journal row.

## Layout

```
CLAUDE.md                       this file
README.md                       what the kit is, how to add it, how to tailor it, status
.claude-plugin/plugin.json      plugin manifest; marketplace.json lists this repo as its own marketplace
agents/                         the eight role agents (frontmatter: name, description, tools, model)
skills/<name>/SKILL.md          the thirteen recurring motions
hooks/hooks.json                PostToolUse: run the validator after an edit under project/
scripts/check_hook.py           the hook's script
templates/                      files the scaffold copies into a project ({{PROJECT_NAME}}, {{APPROVER}}, {{DATE}})
tools/check.py                  the validator (stdlib, python3 -I, config from project/process.toml)
tools/scaffold.py               copies templates, the validator and the agents into a project
tools/tests/                    unittest suite for both
docs/assumptions.md             every assumption the process makes, tailorable or fixed
docs/tailoring.md               what to change for a new project and where
docs/adr/ docs/arch/ docs/process/ docs/design/nfrs.md   the kit's own records
project/                        the kit's own tracking, from its own templates
.github/workflows/ci.yml        tests, the kit's own check.py, scaffold smoke test
```

## How work flows

Read `project/WORKFLOW.md`. In short: research produces options, Ed decides, the
planner writes backlog items, an implementer takes one `ready` item to a PR, a reviewer
checks it, Ed merges, the operator updates tracking and the journal. At every milestone
boundary the architect and the program manager each write a review; their blocking
findings gate the next milestone. Open questions go in `project/questions.md` and are
closed only by Ed or an accepted ADR. Run `python3 -I tools/check.py` after editing
anything in `project/`.

## Conventions

- Verify the plugin layout against the current Claude Code plugin documentation, not
  memory; run `claude plugin validate .` before a PR that touches the manifest, agents,
  skills or hooks.
- `python3 -I -m unittest discover -s tools/tests` must pass; add a test for every
  validator check and every scaffold behaviour.
- A change to a template is also a change to the scaffold smoke test's expectations;
  run the scaffold into a temp directory and `check.py` there before pushing.
- Small, focused commits. One backlog item per PR. Do not touch unrelated files.
- Do not change CI or verification commands to make them pass; fix the code.
- A cloud session pushes its branch before anything else.

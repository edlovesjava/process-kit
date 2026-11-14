---
id: B-026
title: Refactor item template with the byte-identical acceptance line
milestone: later
priority: P2
status: idea
role: implementer
depends_on: B-025
questions:
owner:
updated: 2026-11-14
---

## Goal
A refactor is an item whose acceptance test is that nothing observable changed. The kit
ships a `refactor` item template that carries the line "No behaviour change: golden
files, fitness tests and CLI contract byte-identical", the validator requires that line
on any item with `kind: refactor` (a warning for items older than the check), and the
tailoring docs say how a project proves it: golden fixtures, fitness tests, a recorded
CLI contract, whichever the project has.

## Acceptance
- [ ] `templates/project/backlog/` gains a refactor item template with the acceptance line, and `project/backlog/README.md` (template and the kit's own) names it
- [ ] `tools/check.py`: an item with `kind: refactor` must have a checkbox line under `## Acceptance` containing "No behaviour change" (error; a warning only when `updated` predates the check's adoption date, since items carry no created date); the phrase in Notes only, on a non-checkbox line, or under a renamed heading does not count; tests for each of those and for an old-dated item; the rule is stated in the template it checks
- [ ] A note in the backlog README and `docs/tailoring.md`: adding `kind:` to an existing item touches `updated` and so silences that item's staleness warning; do it in a pass the journal records
- [ ] `docs/tailoring.md` gains a note on proving "no behaviour change" (golden fixtures, fitness tests, CLI contract) and how the architect's XS, S, M sizing of refactor findings is used
- [ ] The `backlog-item` skill mentions the `kind` key and the refactor template
- [ ] Scaffold smoke test covers the new template; `check.py` passes on the kit's own `project/`

## Notes
From the source project's first two refactor items under its development method:
moving composition into the framework configuration so command classes carry no
persistence imports, and domain-first packages with ports and adapters behind an ADR.
Both proved "no behaviour change" with golden fixtures and fitness tests. Depends on
B-025 for the `kind` key.

Updated 2026-11-14: the source project adopted the rule in its own validator and verified
it against planted items (unknown kind, phrase only in Notes, phrase on a non-checkbox
line, renamed Acceptance heading all error; old-dated item warns; existing checks still
fire). The acceptance above follows that verified shape.

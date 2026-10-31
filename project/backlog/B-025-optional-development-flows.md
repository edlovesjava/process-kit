---
id: B-025
title: Optional development flows declared per project, TDD first, none by default
milestone: later
priority: P1
status: idea
role: implementer
depends_on: B-024
questions: Q-006
owner:
updated: 2026-10-31
---

## Goal
The process wraps around a development flow it does not itself prescribe. A project
declares its flow (for example `flow = "tdd"` in `project/process.toml`; default `none`);
the kit carries the first flow, TDD, as prose in a development-method section of the
`WORKFLOW.md` template, and leaves room for flows a wrapped plugin provides (B-024,
Q-006). Two loops, as the source project proposed: inside every task, red-green-refactor
(a test commit precedes or accompanies the code; a `refactor:` commit changes no golden
or expected file and no CLI output); at every milestone boundary, review findings become
refactor items that land before the next milestone's code by default, an architectural
refactor needs an ADR first, and there are no drive-by changes.

## Acceptance
- [ ] `templates/project/WORKFLOW.md` gains a development-method section stating the two loops for `tdd` and what `none` means; the kit's own `project/WORKFLOW.md` follows
- [ ] `templates/project/process.toml` and `docs/tailoring.md` document the `flow` key and its values; `docs/assumptions.md` records the flow as tailorable
- [ ] Optional `kind: feature | refactor | docs | research | review` in item front matter; the validator accepts it, reports an unknown value, and treats a missing key as before; a test per behaviour
- [ ] Under `tdd`: the implementer agent tests first and labels refactor commits; the reviewer checks commit discipline (test before or with code, `refactor:` commits behaviour-neutral); the architect sizes refactor findings XS, S or M
- [ ] Under `none`, agents and validator behave exactly as today; the scaffold smoke test still passes
- [ ] A decision row when the kit's own `process.toml` sets its flow

## Notes
From the source project's "Development method" proposal, generalised. Q-006 decides
whether the TDD text lives in the kit or is handed to a wrapped plugin; this item is
written so that the kit's text is the fallback either way. The `refactor` item template
and its acceptance-line check are B-026.

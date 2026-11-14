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
updated: 2026-11-14
---

## Goal
The process wraps around a development flow it does not itself prescribe. A project
declares its flow (for example `flow = "tdd"` in `project/process.toml`; default `none`);
the kit carries the first flow, TDD, as prose in a development-method section of the
`WORKFLOW.md` template, and leaves room for flows a wrapped plugin provides (B-024,
Q-006). Two loops, as the source project adopted on 2026-11-14 (its D-020). **Task loop:** Red (a
failing test names the behaviour; tests first for pure logic and for every bug fix), Green
(the smallest change that passes), Refactor (structure only, tests unchanged). Commit
granularity: a test and its fix may be one commit, or a red `test:` commit immediately
followed by its `fix:` or `feat:` commit, the only red commit allowed; a refactor is always
its own `refactor:` commit and changes no golden or expected file and no CLI output.
**Milestone loop:** the architecture review (and any process review) turns structural
findings into refactor items (`kind: refactor`, sized XS, S or M by the architect);
should-fix structural findings land before the next milestone's first code item by
default, and the approver may defer any one explicitly in `decisions.md` or the item's
Notes; blocking findings gate the next milestone. An architectural refactor (package
moves, layering, persistence or interface swaps) has an ADR first and is `ready` only once
that ADR is Accepted; ordinary refactors need none. No drive-bys: refinement inside the
item's scope is welcome, anything outside becomes a new item or a question.

## Acceptance
- [ ] `templates/project/WORKFLOW.md` gains a development-method section stating the two loops for `tdd` and what `none` means; the kit's own `project/WORKFLOW.md` follows
- [ ] `templates/project/process.toml` and `docs/tailoring.md` document the `flow` key and its values; `docs/assumptions.md` records the flow as tailorable
- [ ] Optional `kind: feature | fix | refactor | docs | research | review` in item front matter (empty means unset; unknown value is an error; case-sensitive); the validator treats a missing key as before; `INDEX.md` gains a Kind column; the backlog README states it; a test per behaviour
- [ ] The WORKFLOW section states the commit granularity (one commit, or red `test:` then its `fix:`/`feat:`; `refactor:` always alone) and the two reasons the source project gave: a separate red test proves the test catches the bug, a separate refactor lets review check "no behaviour change" against golden files the commit leaves untouched
- [ ] Under `tdd`: the implementer tests first, the red `test:` commit is its only non-green commit, `refactor:` commits stand alone; the reviewer blocks a red commit not immediately followed by its fix, a `refactor:` commit that changes a golden file or CLI output, or a refactor item with any behaviour change, and marks drive-bys should-fix; the architect sizes every finding XS, S or M (larger is split or becomes an ADR), marks it refactor or feature, and says whether it needs an ADR first
- [ ] Under `none`, agents and validator behave exactly as today; the scaffold smoke test still passes
- [ ] A decision row when the kit's own `process.toml` sets its flow

## Notes
From the source project's "Development method" proposal, generalised. Q-006 decides
whether the TDD text lives in the kit or is handed to a wrapped plugin; this item is
written so that the kit's text is the fallback either way. The `refactor` item template
and its acceptance-line check are B-026; the commit-message convention is B-028's.

Updated 2026-11-14 from the source project's adoption of the method (its D-020 and
WORKFLOW section, forwarded by its lead session). Evidence from there, for
`docs/assumptions.md` or `docs/tailoring.md` when this lands: four refactor items in a row
landed with labelled commits and an empty golden diff; one fix landed as a red test commit
then its fix; the one thing the first draft got wrong was commit granularity ("green at
every commit" conflicted with test-first), which is why the red `test:` commit is now
allowed and named.

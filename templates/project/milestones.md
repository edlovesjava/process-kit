# Milestones

Status of each milestone. Items are in `project/backlog/`; the list of milestone names
the validator accepts is `backlog.milestones` in `process.toml` and must match this
table. Statuses: `not-started`, `in-progress`, `done`. A milestone is `done` when its
last item is `done` and both boundary reviews (`docs/arch/`, `docs/process/`) are written
and their blocking findings decided.

| Milestone | Delivers | Acceptance test | Items | Status |
| --- | --- | --- | --- | --- |
| Spec | Decisions and records the first code needs | ADRs accepted; `check.py` passes with M0 `ready` | B-001 | in-progress |
| M0 | First runnable skeleton | Clean clone builds and tests green in CI | | not-started |
| M1 | First useful capability | One sentence a user can verify | | not-started |
| M2 | ... | ... | | not-started |

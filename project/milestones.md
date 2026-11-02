# Milestones

Status of each milestone of the kit. Items are in `project/backlog/`; the list of
milestone names the validator accepts is `backlog.milestones` in `process.toml` and must
match this table. Statuses: `not-started`, `in-progress`, `done`. A milestone is `done`
when its last item is `done` and both boundary reviews (`docs/arch/`, `docs/process/`)
are written and their blocking findings decided. M0 to M2 were built in one bootstrap
session (D-002), so their boundary reviews are owed together at the M2 boundary.

| Milestone | Delivers | Acceptance test | Items | Status |
| --- | --- | --- | --- | --- |
| Spec | ADR-0001, the kit's own tracking, the questions Ed must answer | ADR-0001 decided; `check.py` passes on `project/` | B-013, B-019 | in-progress |
| M0 Scaffold and validator | `tools/check.py` with `process.toml`, journal checks, unit tests; `tools/scaffold.py`; CI | Scaffold into an empty directory, `check.py` there reports zero errors; `unittest` green | B-001, B-002, B-003 | in-progress (reviews owed) |
| M1 Agents and skills | Eight role agents, thirteen skills, one hook, plugin manifest and marketplace | `claude plugin validate .` passes; every skill reads as prose a human can follow | B-004, B-005, B-006, B-007 | in-progress (reviews owed) |
| M2 Templates and tailoring docs | Templates for every tracking and docs file, `docs/assumptions.md`, `docs/tailoring.md`, README | A reader can tailor roles, milestones, invariants and cadence without reading the kit's code | B-008, B-009, B-010, B-011, B-012 | in-progress (reviews written 2026-11-01; blocking findings for Ed) |
| M3 Dogfood on a second project | The kit adopted by the source project and by one fresh project through one full item loop | Both projects' `check.py` pass; one item goes ready, in-progress, review, done with journal rows; findings become kit items | B-014, B-015, B-030, B-031, B-032, B-033, B-034 | not-started |
| M4 Hardening | Journal hooks if decided, plugin evals, `--strict` validation in CI, distribution path | Decided in Q-002 and Q-003; evals pass | B-016, B-017, B-018, B-020, B-035, B-036 | not-started |

# Architecture goals and non-functional requirements

The goals are what the kit is for. The NFRs are how we know we are meeting them; each has
a fitness function (a test, a measurement or a check) and a status. The architect agent
re-evaluates this register at every milestone boundary (see `docs/arch/`), and a change
to a goal or an NFR is a decision for Ed, recorded in `project/decisions.md` or an ADR.

Statuses: `met` (fitness function exists and passes), `partial` (met in part or by
convention only), `gap` (no fitness function yet), `pending <Mn>` (the milestone that
delivers it).

## Architecture goals

| Goal | Statement | Source |
| --- | --- | --- |
| G1 Portable | A project adopts the process with one command and nothing installed; it works offline, in CI and in cloud sessions. | Invariants 3, 4; ADR-0001 |
| G2 Tailorable, not forkable | Roles, models, milestones, invariants, cadence and vocabulary change in config and prose, with a decision row, without editing the kit. | `docs/tailoring.md` |
| G3 Honest record | The backlog, registers, logs and journal cannot drift silently: the validator refuses inconsistent state and warns on missing rows. | Invariant 6; source project findings |
| G4 Readable by hand | Every skill, template and check is prose a human could follow without the plugin. | Invariant 5 |
| G5 Carries no project | Nothing in the kit names a real product, person, system or secret. | Invariant 1 |

## NFR register

| ID | Requirement | Fitness function | Evidence (2026-10-31; re-verified 2026-11-01, `docs/arch/review-M2-2026-11-01.md`) | Status |
| --- | --- | --- | --- | --- |
| N-001 | `tools/` and `scripts/` run on Python 3.11+ standard library with `python3 -I`; no third-party import | CI runs tests and the scaffold under `-I` with no `pip install` | CI job does so (3.12 only); import audit by hand 2026-11-01 clean; no automatic check. Proposed fitness: `test_stdlib_only` and a 3.11/3.13 matrix (B-034) | partial |
| N-002 | Scaffold into an empty directory yields a project whose `check.py` reports zero errors | CI scaffold smoke test; `test_fresh_scaffold_passes_and_writes_index` | Passes | met |
| N-003 | The scaffold never overwrites an existing file without `--force` | `test_scaffold_never_overwrites_without_force`, `test_existing_claude_md_is_left_alone`; CI second-run check | Pass | met |
| N-004 | Every validator check has a unit test that triggers it | `tools/tests/test_check.py`, one test per check | 31 tests; 5 of 35 validator messages and 3 scaffold CLI paths untested. Proposed fitness: `ast` meta-test (B-034) | partial |
| N-005 | The plugin passes `claude plugin validate .` | Run locally before a PR touching manifest, agents, skills, hooks | Passed with two accepted warnings 2026-10-31 (CLI 2.1.316): licence (Q-001), `CLAUDE.md` at root (the kit is also a project); not in CI (needs the CLI), B-020. Re-run 2026-11-01: passes, warnings `CLAUDE.md` at root and missing icon; `--strict` exits 1 (Q-008) | partial |
| N-006 | No placeholder (`{{...}}`) survives scaffolding; no source-project noun appears in the kit | `test_scaffold_substitutes_placeholders_everywhere`; CI job `no-project-nouns` | Both in place | met |
| N-007 | The hook exits 0 in any repository without `project/process.toml` and never raises. *(proposed reword, B-032: the hook validates any edit under a kit project's `project/`, whatever the session cwd, and exits 0 everywhere else)* | Hook script's catch-all; `tools/tests/test_hook.py` (B-032) | Catch-all present; 11 payloads tried by hand 2026-11-01; skips silently when cwd is a subdirectory; no test | gap |
| N-008 | The kit's own `project/` passes `check.py` with zero errors on every commit to main | CI job | In CI | met |
| N-009 | `INDEX.md` in the kit is current on every commit | CI `git diff --exit-code` after `check.py` | In CI | met |
| N-010 *(proposed)* | Every scaffolded copy is recorded with the kit version and a hash; an update never overwrites a file whose hash differs from the lock | `test_scaffold_writes_lock_with_hashes`, `test_force_only_limits_paths` (B-030) | None yet; ADR-0002 Proposed | pending M3 |
| N-011 *(proposed)* | Every "must match" stated in a template is checked by the validator, at least as a warning | B-035's tests | None yet | pending M4 |

## How to change this register

- A new NFR or a changed threshold is a decision (D-NNN) or an ADR; the architect proposes,
  Ed decides.
- The architect's milestone review re-evaluates every row and may move a status; it does
  not add rows on its own.
- When a `gap` gains a fitness function, link the test or check in the Fitness function
  column and set the status from its result.

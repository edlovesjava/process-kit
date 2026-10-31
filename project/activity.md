# Activity journal

Append-only record of the work process: one row per agent dispatch or human decision.
Newest at the bottom. One `## YYYY-MM-DD` heading per UTC day; the rows under it carry the
full date-time so a row can be quoted on its own. `check.py` validates the headings, the
Role, Model and Outcome columns (values from `process.toml`) and warns when a backlog item
reaches `review` or `done` with no row naming it that day. The program manager reads this
file at every milestone boundary.

Columns:

| Column | Meaning |
| --- | --- |
| Date-time | `YYYY-MM-DD HH:MM` UTC when the dispatch ended or the decision was made |
| Role | the role that ran (from `process.toml`), or `human` |
| Model | `lead` for the orchestrating session, else the model the role ran on, or `human` |
| Item | the backlog item or question it served (`B-NNN`, `Q-NNN`, `D-NNN`, `ADR-NNNN`), or `-` |
| Runs | how many dispatches it took to get this outcome (reruns included) |
| Outcome | `done`, `partial`, `blocked`, `failed`, `decided`, `deferred` |
| Human turns | messages from the approver needed to reach the outcome |
| Problem | what went wrong or slowed it, `reconstructed` for backfilled rows, else empty |
| Resolution | what fixed it, or what is still owed, else empty |

## 2026-10-31

| Date-time | Role | Model | Item | Runs | Outcome | Human turns | Problem | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-31 12:10 | human | human | D-001, D-010 | 1 | decided | 1 | | Ed's brief via the lead session: build the kit, dogfood it, include program-manager and the journal. |
| 2026-10-31 12:40 | researcher | lead | - | 1 | done | 0 | bootstrap: lead did every role (D-002) | Read the source project's process files and the current plugin documentation; layout verified against four doc pages. |
| 2026-10-31 13:20 | implementer | lead | B-001 | 2 | done | 0 | bootstrap; first run misread the journal's documentation table as rows | Tables before the first `##` heading are skipped. 30 tests green. |
| 2026-10-31 13:40 | implementer | lead | B-008, B-002 | 1 | done | 0 | bootstrap | Templates and scaffold; two test expectations corrected (P0 sort order, `ready` draws no journal warning). |
| 2026-10-31 13:50 | implementer | lead | B-004 | 1 | done | 0 | bootstrap | Eight agents generalised. |
| 2026-10-31 14:10 | implementer | lead | B-005, B-006, B-007 | 1 | done | 0 | bootstrap | Thirteen skills, one hook, manifest and marketplace; `claude plugin validate .` passed (CLI 2.1.316). |
| 2026-10-31 14:30 | researcher | lead | B-009 | 1 | done | 0 | bootstrap | assumptions.md (21 rows) and tailoring.md. |
| 2026-10-31 14:35 | researcher | lead | D-002, D-003, D-004, D-005, D-006, D-007, D-008, D-009, D-011 | 1 | decided | 0 | awaiting Ed's confirmation (B-013) | Recorded in decisions.md with `By: researcher`. |
| 2026-10-31 14:40 | researcher | lead | ADR-0001 | 1 | done | 0 | bootstrap | Proposed; Ed decides in B-013. |
| 2026-10-31 14:45 | researcher | lead | Q-001, Q-002, Q-003, Q-004, Q-005 | 1 | done | 0 | | Raised with options and a recommendation each. |
| 2026-10-31 15:00 | operator | lead | B-003 | 1 | done | 0 | bootstrap; CI unverified until pushed | Three jobs; first GitHub run to be checked after push (B-003 open box). |
| 2026-10-31 15:10 | researcher | lead | B-010 | 1 | done | 0 | bootstrap | README written. |
| 2026-10-31 15:20 | planner | lead | B-011, B-012, B-013, B-014, B-015, B-016, B-017, B-018, B-019, B-020 | 1 | done | 0 | bootstrap | Execution plan for M2 reviews, M3 dogfooding and M4 hardening. |
| 2026-10-31 20:25 | operator | lead | B-003 | 1 | done | 0 | | CI run 1 on main green; B-003 fully done. |

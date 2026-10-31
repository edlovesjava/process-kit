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
| 2026-10-31 21:10 | researcher | lead | B-021 | 1 | partial | 1 | | Whitepaper draft written to docs/whitepaper.md and a Claude doc; awaiting Ed's comments. |
| 2026-10-31 21:50 | human | human | Q-001, Q-002, Q-003, Q-004, Q-005, D-012, D-013, D-014, D-015, D-016 | 1 | decided | 2 | Ed's messages numbered the last two answers Q-003 and Q-004; recorded under Q-004 and Q-005 by content | MIT; plugin plus owned copies with an update path; journal by hand first, competitive design later; kit carries .claude/agents/; name stays. |
| 2026-10-31 21:55 | implementer | lead | B-019 | 1 | done | 0 | no role agents loaded in this cloud session; lead did the role | LICENSE, plugin.json license, README line; plugin validate no longer mentions the licence (CLAUDE.md and icon warnings remain). |
| 2026-10-31 21:58 | operator | lead | B-022 | 1 | done | 0 | as above | agents/ copied verbatim to .claude/agents/. |
| 2026-10-31 22:00 | operator | lead | B-016, B-018 | 1 | done | 0 | | B-018 unblocked to ready with the decided scope; B-016 to idea pending the competitive design. SITREP entry written. |
| 2026-10-31 22:30 | researcher | lead | B-023 | 3 | done | 1 | three parallel researchers; 27 vendor hosts unreachable from the sandbox, facts from them via search extracts and marked | docs/research/prior-art-2026-10-31.md: comparison tables, four features not found elsewhere, five reinventions, ten proposals for Ed. Item to review. |
| 2026-10-31 22:45 | operator | lead | - | 1 | done | 1 | | Session closed on Ed's request (parallel session active): branch pushed, clean, SITREP handoff written. |
| 2026-10-31 22:45 | planner | lead | B-024, B-025, B-026 | 1 | done | 0 | source-project attach denied; items written from the brief's summary of its development-method proposal | Three `idea` items from the source project's M4 review: plugin survey, optional per-project flows, refactor item template. Ed prioritises. |
| 2026-10-31 22:45 | planner | lead | Q-006 | 1 | done | 0 | | Raised: which flows the kit offers and whether it wraps existing plugins; B-024 fills the options. |
| 2026-10-31 22:55 | planner | lead | B-027 | 1 | done | 0 | | Ed's proposal via the source project's lead: session and context management (handoff skills, session topology, context budget, journal rows per session event). `idea`. |
| 2026-10-31 23:30 | planner | lead | B-028, B-029 | 1 | done | 1 | | Ed's defaults for repositories, branches and commits (workspaces, one branch per session, subagents share or stack when safe, Conventional Commits) and the later multi-repository shape, as `idea` items. |

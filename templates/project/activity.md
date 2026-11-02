# Activity journal

Append-only record of the work process: one row per agent dispatch or human decision.
Newest at the bottom. One `## YYYY-MM-DD` heading per UTC day; the rows under it carry the
full date-time so a row can be quoted on its own. `check.py` validates the headings, the
Role, Model and Outcome columns (values from `process.toml`), warns when a backlog item
reaches `review` or `done` with no row naming it that day, and warns when a row other than
the roles in `journal.decided_roles` carries `decided` (from `journal.decided_roles_from`). The program manager reads this
file at every milestone boundary.

Columns:

| Column | Meaning |
| --- | --- |
| Date-time | `YYYY-MM-DD HH:MM` UTC, read from `date -u +'%Y-%m-%d %H:%M'` when the row is written, never estimated; a row for earlier work carries `late: HH:MM` in Problem |
| Role | the role that ran (from `process.toml`), or `human` |
| Model | `lead` for the orchestrating session, else the model the role ran on, or `human` |
| Item | the backlog item or question it served (`B-NNN`, `Q-NNN`, `D-NNN`, `ADR-NNNN`), or `-` |
| Runs | how many dispatches it took to get this outcome (reruns included) |
| Outcome | `done`, `partial`, `blocked`, `failed`, `decided`, `deferred`; `decided` only on a `human` row, an agent's proposal is `done` awaiting the approver |
| Human turns | messages from the approver needed to reach the outcome |
| Problem | what went wrong or slowed it; `reconstructed` for backfilled rows; `late: HH:MM` when the row is written after the work; else empty |
| Resolution | what fixed it, or what is owed, else empty |

## {{DATE}}

| Date-time | Role | Model | Item | Runs | Outcome | Human turns | Problem | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{DATE}} 00:00 | human | human | D-001 | 1 | decided | 1 | | Process adopted from process-kit; scaffold run. |

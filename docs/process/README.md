# Process reviews

One review per milestone boundary, written by the program manager agent alongside the
architect's review in `docs/arch/`. Where the architecture review asks whether the code
still serves the goals, the process review asks whether the way of working still serves
the people and the budget: where dispatches were rerun, where decisions waited, where
tracking lagged the code, and what to change in `project/WORKFLOW.md`.

Evidence comes from `project/activity.md`, the backlog item files, `project/SITREP.md`,
the questions register and the PR history. Ed decides on every proposal.
Blocking process findings gate the next milestone exactly as blocking architecture
findings do.

Files: `review-<milestone>-<yyyy-mm-dd>.md`, from `0000-review-template.md`. A review is a
snapshot and is never edited.

| Review | Covers | Outcome |
| --- | --- | --- |
| [review-M2-2026-11-01.md](review-M2-2026-11-01.md) | 2026-10-31 to 2026-11-01; M0 to M2 bootstrap, second and third sessions; PRs #1 to #3 (B-012) | Dispatches per item median 1 max 2; 1 rerun; 0.43 human turns per decided record; ready-to-merged and review-findings uncountable (no item passed `ready`, no reviewer ran); 4 of 5 recommendations taken. 3 blocking, 5 should-fix, 4 opportunities; records: Q-010 (W1 to W8), Q-011, B-037, edits to B-013, B-014, B-015, B-027, B-028 |

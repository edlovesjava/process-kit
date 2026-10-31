# Process reviews

One review per milestone boundary, written by the program manager agent alongside the
architect's review in `docs/arch/`. Where the architecture review asks whether the code
still serves the goals, the process review asks whether the way of working still serves
the people and the budget: where dispatches were rerun, where decisions waited, where
tracking lagged the code, and what to change in `project/WORKFLOW.md`.

Evidence comes from `project/activity.md`, the backlog item files, `project/SITREP.md`,
the questions register and the PR history. {{APPROVER}} decides on every proposal.
Blocking process findings gate the next milestone exactly as blocking architecture
findings do.

Files: `review-<milestone>-<yyyy-mm-dd>.md`, from `0000-review-template.md`. A review is a
snapshot and is never edited.

| Review | Covers | Outcome |
| --- | --- | --- |

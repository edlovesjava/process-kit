# Process review after <milestone>, YYYY-MM-DD

Program manager review for B-NNN. Snapshot, never edited. Ed decides on every
proposal. Each finding is marked **measured** (counted from the journal or the repository)
or **observed** (read in a SITREP, a PR or an item note, not counted).

## 1. Scope

- **Period and items:** first and last journal day, milestones covered, items touched.
- **Sources read:** `project/activity.md`, item files, SITREP entries, questions, PRs.
- **Gaps in the record:** days with no rows, items with status changes and no row,
  rows marked `reconstructed`.

## 2. Metrics

| Metric | Value | How counted |
| --- | --- | --- |
| Dispatches per item (median, max) | | journal rows per `B-` item |
| Reruns per item (Runs > 1) | | journal Runs column |
| Human turns per decision | | journal rows with Outcome `decided` |
| Ready to merged, elapsed (median, max) | | item `updated` on `ready` to PR merge date |
| Recommendation acceptance rate | | questions answered with the recommended option / answered |
| Review findings fixed before merge vs deferred | | reviewer and architect findings by disposition |
| Tracking lag after merge | | merges whose item was set `done` in a later session |

## 3. Findings, ranked

### Blocking (the next milestone would repeat the damage)

**B1. Title.** *measured or observed.* Where it shows in the record, what it cost, the
proposed change to `WORKFLOW.md`, an agent definition or the tooling, and its cost.

### Should fix before the next milestone

**S1. ...**

### Opportunities

**O1. ...**

## 4. Bottlenecks and loops

Where work waited on one person or one role, and where an item cycled (implement, review,
implement) more than twice. Name the item and the rows.

## 5. Proposals as records

- **WORKFLOW.md changes:** one line each; each needs a decision row.
- **Agent definition changes:** role, what changes, why.
- **Tooling:** validator checks, hooks, templates.
- **Questions:** Q entries with options and a recommendation.
- **Backlog:** new items.

Do not write these into `project/` yourself; the lead folds them in.

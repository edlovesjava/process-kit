# Architecture review after <milestone>, YYYY-MM-DD

Architect review for B-NNN. This is a snapshot and is never edited. Ed decides
on every proposal; the lead folds accepted ones into `project/` and `docs/adr/`. Each
finding is marked **verified** (the reviewer ran it or read the line) or **inferred**
(reasoned from the code or the plan, not exercised).

## 1. Scope

- **Reviewed:** branch and commit, milestones covered, files and tests read, what was run.
- **Not reviewed:** and why.
- **Previous review:** which of its findings landed, which are still open.

## 2. Goals scorecard

| Goal | Status | Evidence |
| --- | --- | --- |
| G1 ... | met / partial / at risk | one sentence naming a test, a file or a measurement |

## 3. NFR status

| ID | Status | Evidence (date, machine) |
| --- | --- | --- |
| N-001 | met / partial / gap / pending <Mn> | test name, measurement, or "unmeasured" |

## 4. Findings, ranked

### Blocking (decide before the next milestone's first code item)

**B1. Title.** *verified or inferred.*
- **Where:** file and line, or component.
- **What:** the problem.
- **Why:** which invariant, ADR or goal it violates, or what rewrite it would force.
- **Proposal:** concrete change, and the question or ADR it needs.
- **Cost:** XS / S / M / L.

### Should fix before the next milestone

**S1. ...**

### Opportunities

**O1. ...** (would serve a goal better; cost and benefit stated)

## 5. Looking ahead

For the next two milestones: what in the current structure helps, what will hurt, and the
decision points by name.

## 6. Proposals as records

- **ADR changes:** new ADRs or amendments, one line each.
- **Questions:** Q entries with options and a recommendation.
- **Backlog:** additions to existing items and new items.
- **NFR register changes:** status moves with evidence; candidate new rows for the approver.

Do not write these into `project/` or `docs/adr/` yourself; the lead folds them in.

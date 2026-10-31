---
name: process-review
description: Run the process review at a milestone boundary: dispatch the program-manager agent against the activity journal and tracking files, then fold its proposals into decisions, WORKFLOW.md changes and backlog items for the approver. Use alongside the architecture review, or when asked for a "process review" or "retro".
argument-hint: "[milestone]"
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit, Agent
---
Review how the work ran during milestone `$0`, from the record rather than from memory.
Blocking process findings gate the next milestone exactly as blocking architecture
findings do.

1. Preconditions: the milestone's last code item is at `review` or `done`; a backlog item
   for this review exists (role `program-manager`, milestone `$0`). Run
   `python3 -I project/tools/check.py` first: every "has no journal row" warning is a gap
   in the record the review will have to name, so fill the rows you can (journal skill,
   problem column `reconstructed`) before dispatching.
2. Dispatch the program-manager agent with: the period (first and last journal day), the
   items and PRs in the milestone, the previous process review's path if any, and the
   instruction to write `docs/process/review-$0-<today>.md` from
   `docs/process/0000-review-template.md`.
3. Read the review. Fold the proposals in:
   - WORKFLOW.md changes: each is a decision for the approver; present them, and on
     acceptance edit `project/WORKFLOW.md` and add a decision row (decision skill);
   - agent definition changes: a backlog item against the kit or `.claude/agents/`;
   - tooling (validator checks, hooks, templates): backlog items;
   - questions and items: question and backlog-item skills.
4. Add a row to the table in `docs/process/README.md`: file, period and items covered,
   the headline metrics, counts of findings, records created.
5. Set the review's item `done` with a journal row (role `program-manager`).
6. Report to the approver: the blocking findings and the recommended change for each, the
   metrics in one short table, and what the next milestone waits on.

The review is a snapshot and is never edited afterwards; its proposals live on in
`project/`.

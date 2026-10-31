---
name: arch-review
description: Run the architecture review at a milestone boundary: dispatch the architect agent against the whole system, then fold its proposals into questions, ADR drafts, backlog items and the NFR register for the approver to decide. Use when a milestone's last code item reaches review, or when asked for an "architecture review".
argument-hint: "[milestone]"
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit, Agent
---
Review the whole system, not the diff, at the boundary of milestone `$0`. The next
milestone's first code item does not start until the blocking findings are decided.

1. Preconditions: the milestone's last code item is at `review` or `done`; a backlog item
   for this review exists (role `architect`, milestone `$0`); the build and tests pass on
   the branch under review. If no item exists, create one (backlog-item skill).
2. Dispatch the architect agent with: the commit or branch to review, the milestones
   covered, the previous review's path if one exists, and the instruction to write
   `docs/arch/review-$0-<today>.md` from `docs/arch/0000-review-template.md`. The agent
   runs the build and any fitness function named in `docs/design/nfrs.md` itself.
3. Read the review. For each item under "Proposals as records", fold it in:
   - questions: question skill, with the architect's options and recommendation;
   - ADRs or amendments: adr skill, status Proposed;
   - backlog additions: edit the named items' acceptance and notes, or create items;
   - NFR register changes: move statuses with the review's evidence; a new row is a
     proposal for the approver, marked `(proposed)` until a decision row accepts it.
4. Add a row to the table in `docs/arch/README.md`: review file, what it covered, counts
   of blocking, should-fix and opportunity findings, and the records created.
5. Set the review's backlog item `done` with a journal row (role `architect`, model from
   `process.toml`, runs and outcome as they were).
6. Run `python3 -I project/tools/check.py`.
7. Report to the approver: the blocking findings with the architect's recommendation for
   each, and which items wait on them. The approver decides; record each decision with
   the question or decision skill. The review file itself is never edited afterwards.

Run the process-review skill for the same boundary; both reviews gate the next milestone.

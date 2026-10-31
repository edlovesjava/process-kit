---
name: status
description: Produce the project-manager status summary: what is ready by priority, what is blocked and on what, what the approver must decide, what is stale, what the journal shows. Use when asked for "status", "what's next", or before handing an item to an implementer.
allowed-tools: Bash, Read
---
Give the status the project manager would give. Delegate to the project-manager agent
when it is available (it may also fix tracking errors); otherwise follow its definition
by hand:

1. Run `python3 -I project/tools/check.py`. Errors come first in the summary; nothing is
   trustworthy until they are fixed.
2. Read `project/backlog/INDEX.md`, the open entries in `project/questions.md`,
   `project/milestones.md`, and the last three days of `project/activity.md`.
3. Scan `git log --since=14.days --stat` for threads with no item or question (a TODO,
   a "later", a risk in a review with no record). List them as proposed items.
4. Write the summary, under 30 lines, in this order:
   - **Ready now**, by priority, with role and any file overlap between items that could
     run in parallel.
   - **Blocked**, each with the item or question it waits on.
   - **Approver decides**: open questions with a recommendation, Proposed ADRs, items
     awaiting `dropped`.
   - **Stale**: items and questions untouched past the configured period.
   - **Journal**: dispatches rerun more than once this week; items at `review` or `done`
     with no row; days with no rows.
   - **Milestone**: where the current milestone stands and whether the boundary reviews
     are due (last code item at `review`).
5. Never answer a question or change a priority yourself. Propose; the approver decides.

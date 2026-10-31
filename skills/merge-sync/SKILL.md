---
name: merge-sync
description: Bring tracking up to date right after a PR merges: item to done, INDEX regenerated, milestone status, mirrored issue closed, journal row, SITREP if the milestone ended. Use immediately after the approver merges, or when the validator or git log shows merged work still not marked done.
argument-hint: "[B-NNN] [PR number]"
allowed-tools: Bash, Read, Edit
---
Close the loop on a merge in the same session as the merge. Tracking lagging main by one
step after every merge was the first finding of the source project's process review; this
skill exists so it does not recur.

1. Confirm the merge: `git fetch origin main` and `git log origin/main --oneline -5`
   shows the PR's merge commit, or the approver said so. Do not mark anything done on
   intent.
2. In `project/backlog/$0-*.md`: `status: done`, `owner:` cleared, `updated:` today. Tick
   any acceptance box the PR evidenced but left unticked, citing the PR.
3. `project/milestones.md`: if this was the milestone's last item, set the milestone
   `in-progress` with a note that the boundary reviews are due (it becomes `done` when
   both reviews are written and their blocking findings decided). Otherwise leave the
   status and update the Items column if it changed.
4. Items whose `depends_on` was only this item: set `ready` if their questions are all
   answered; touch `updated`.
5. If `issues.mirror` is `true` in `process.toml`: close the GitHub issue titled with the
   item id, referencing the PR. Check it actually closed; a missed close was the second
   finding.
6. Append a journal row (journal skill): role of whoever implemented, item `$0`, runs as
   counted from the PR history, outcome `done`, human turns from the review thread.
7. Run `python3 -I project/tools/check.py`; it must report zero errors and no
   "has no journal row" warning for `$0`.
8. If the milestone's last code item just merged, dispatch the architect and the
   program manager (arch-review and process-review skills) before any item of the next
   milestone starts, and add a SITREP entry.
9. Commit the tracking change on its own, message `Tracking: $0 done (PR #$1)`.

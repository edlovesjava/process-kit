---
name: session-start
description: The ritual a new session performs before touching work in a process-kit project: push the branch, read the handoff files, get status from the project manager. Use at the start of a session, or when asked "where are we" or "what should I work on".
allowed-tools: Bash, Read
---
Start the session the way the process expects. Do these in order and do not skip the
first one.

1. **Push the branch first.** In a cloud session, run `git push -u origin <branch>` now,
   even with no commits. A branch that is not on origin cannot be teleported or opened in
   a terminal. Skip only if `git status -sb` already shows the branch tracking origin.
2. **Read, in order:** `CLAUDE.md`, the top entry of `project/SITREP.md`,
   `project/backlog/INDEX.md`, the open entries in `project/questions.md`, and the last
   day of `project/activity.md`.
3. **Run the validator:** `python3 -I project/tools/check.py`. If it reports errors, fix
   the tracking files before anything else; if it warns that an item is `review` or
   `done` with no journal row, add the row (see the journal skill) because that is the
   tracking lag the process exists to prevent.
4. **Ask the project-manager agent for status** (or produce it yourself by its
   definition): what is ready by priority, what is blocked and on what, what the approver
   must decide, what is stale.
5. **Report** in under 20 lines: branch state, the one or two items you propose to take,
   the decisions waiting on the approver. Then wait for the approver's choice unless the
   SITREP already names the next item.

Before the session ends with anything in flight, add a SITREP entry (sitrep skill).

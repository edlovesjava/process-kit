---
name: journal
description: Append a row to the activity journal (project/activity.md) for an agent dispatch or a human decision: date-time, role, model, item, runs, outcome, human turns, problem, resolution. Use after every subagent dispatch, after every decision by the approver, and whenever the validator warns that an item has no journal row.
argument-hint: "[role] [item] [outcome]"
allowed-tools: Bash, Read, Edit
---
Add one journal row. The journal is the record the program manager reviews, so a missing
row is a missing fact, and a row written from memory a week later is a worse one. Write
it the same day, right after the dispatch or decision.

1. Open `project/activity.md`. Find or create today's heading at the bottom of the file,
   using the UTC date (`date -u +%F`):

   ```
   ## YYYY-MM-DD

   | Date-time | Role | Model | Item | Runs | Outcome | Human turns | Problem | Resolution |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   ```

2. Append the row under that heading (never above an earlier day):

   ```
   | YYYY-MM-DD HH:MM | $0 | <model> | $1 | <n> | $2 | <n> | <problem or empty> | <resolution or empty> |
   ```

   - **Role**: a role from `project/process.toml`, or `human`.
   - **Model**: `lead` for the orchestrating session itself, otherwise the model the role
     ran on (`opus`, `sonnet`, `haiku`), or `human`. The allowed list is
     `journal.models` in `process.toml`.
   - **Item**: `B-NNN`, `Q-NNN`, `D-NNN` or `ADR-NNNN`; several separated by commas;
     `-` if none.
   - **Runs**: how many dispatches it took to reach this outcome, reruns included. A
     rerun is a signal, not a failure; count it honestly.
   - **Outcome**: one of `journal.outcomes`: `done`, `partial`, `blocked`, `failed`,
     `decided` (human decisions), `deferred`.
   - **Human turns**: messages from the approver needed to reach the outcome.
   - **Problem**: what went wrong or slowed it; `reconstructed` when the row is written
     after the fact from item notes, SITREP or PR history; empty when nothing did.
   - **Resolution**: what fixed it, or what is still owed.

3. Run `python3 -I project/tools/check.py`; a bad role, model, outcome or date-time is an
   error.
4. Commit the row with the change it records when possible; otherwise on its own.

A decision by the approver is a row too: role `human`, model `human`, outcome `decided`,
item the question, decision or ADR it settled.

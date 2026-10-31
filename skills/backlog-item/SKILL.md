---
name: backlog-item
description: Create a new backlog item file in project/backlog/ with valid front matter, a goal, checkable acceptance criteria and explicit dependencies, then validate. Use when work needs tracking, when a review or question produces follow-up work, or when asked to "add an item".
argument-hint: "[short title]"
allowed-tools: Bash, Read, Write, Edit
---
Create one backlog item. An item is the unit of implementation: one item, one PR.

1. Find the next id: the highest `B-NNN` in `project/backlog/` plus one, zero-padded to
   three digits. Never reuse an id, even a dropped one.
2. Read `project/process.toml` for the allowed `milestone`, `priority`, `status` and
   `role` values, and `project/backlog/README.md` for the format.
3. Write `project/backlog/B-NNN-short-title.md` with this front matter, every key present
   even when empty:

   ```
   ---
   id: B-NNN
   title: $0
   milestone: <from process.toml>
   priority: P0 | P1 | P2
   status: idea | blocked | ready
   role: <from process.toml, or human>
   depends_on: <B-IDs, comma-separated, or empty>
   questions: <Q-IDs that must be answered first, or empty>
   owner:
   updated: <today, YYYY-MM-DD>
   ---
   ```

   Then `## Goal` (one paragraph of what done looks like), `## Acceptance` (checkbox
   lines a reviewer can tick, each verifiable), `## Notes` (links to the finding, review
   or decision that produced the item).
4. Choose the status honestly: `ready` only if every dependency is `done` and every linked
   question `answered`; `blocked` if something is unmet; `idea` if it is not yet planned.
   If the item needs a decision nobody has made, raise a question (question skill), link
   it, and set `blocked`. Do not guess the decision.
5. Run `python3 -I project/tools/check.py`. Fix what it reports; it regenerates
   `INDEX.md`, which is never edited by hand.
6. If `issues.mirror` is `true` in `process.toml` and the item is `ready`, the operator
   opens one GitHub issue titled `B-NNN <title>` whose body links the item file.
7. Add a journal row (journal skill) if this item came out of an agent dispatch.

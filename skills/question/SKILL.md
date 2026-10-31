---
name: question
description: Add an entry to the questions register (project/questions.md) with context, options and a recommendation, or record progress on an open one. Use when a decision is missing, when an implementer or reviewer hits an unknown, or when asked to "raise a question". Agents never close a question.
argument-hint: "[short question]"
allowed-tools: Bash, Read, Edit
---
Raise or update a question. Questions are first-class: every unknown becomes one instead
of an improvised decision, and only the approver (or an accepted ADR) closes one.

To raise:

1. Next id: highest `Q-NNN` in `project/questions.md` plus one, zero-padded.
2. Append at the end of the file, keeping the format exactly (`check.py` reads the
   heading and the Status line):

   ```
   ## Q-NNN $0
   - **Status:** open
   - **Tags:** arch | process | scope | <system>
   - **Raised:** <today> by <role>, in <file or PR where it came up>
   - **Blocks:** <B-IDs, or empty>
   - **Why it matters:** one or two sentences: what goes wrong if this is guessed
   - **Options:** (a) ..., (b) ..., with the recommendation marked "recommended"
   - **Answer:**
   ```

3. Link it from every item it blocks (`questions:` in the item's front matter) and set
   those items `blocked` if they were `ready`.
4. Run `python3 -I project/tools/check.py`.

To record progress without closing: add a dated line between Options and Answer,
`- **Progress (YYYY-MM-DD):** ...`. Leave Status `open`.

When the approver answers: fill `**Answer:**` with what was decided, by whom, on what
date, and where it is recorded (ADR, decision row, item), set Status `answered`, re-run
`check.py`, and flip blocked items whose last blocker this was to `ready`. Add a journal
row with role `human`, outcome `decided`.

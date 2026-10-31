---
name: check
description: Run the tracking validator (project/tools/check.py), which checks backlog front matter, status transitions, questions and the activity journal and regenerates INDEX.md. Use after any edit under project/, before a commit that touches tracking, or when asked to "run check" or "validate the backlog".
allowed-tools: Bash, Read, Edit
---
Run the validator and act on what it says.

```
python3 -I project/tools/check.py
```

Always `-I` (isolated mode): the script is stdlib-only and must not pick up code from the
current directory. Use `--no-write` to validate without regenerating `INDEX.md`, and
`--root <dir>` when running from outside the repository.

Read the last line: `items=N questions_open=N journal_rows=N errors=N warnings=N`. Exit
status 1 means errors.

**Errors** are format or logic violations and must be fixed before committing:
- `missing keys`, `bad date`, `unknown status/role/milestone/priority`: fix the item file.
  If the value is right and the vocabulary is wrong, that is a decision: change
  `process.toml` with a decision row, not a quiet edit.
- `ready but blocked by [...]`: set the item `blocked`, or finish the dependency.
- `blocked with nothing blocking it`: set it `ready` or `idea`.
- `in-progress/review without an owner`: fill `owner`.
- `activity.md: unknown role/model/outcome`, `not a date-time`, `not under its heading`:
  fix the row; rows are append-only but a typo may be corrected in the same session.
- `process.toml: ...`: the config itself is wrong; see `docs/tailoring.md` in the kit.

**Warnings** never fail the run but each is a process signal:
- `not updated since`: touch the item or let the PM decide whether it is stale.
- `<item>: review/done on <date> has no journal row that day`: add the row (journal
  skill). This is the tracking lag the journal exists to catch.
- `day ... is out of order`: a row was inserted above a later day; move it.

Commit `INDEX.md` together with the change that regenerated it. Never edit it by hand.

"""Unit tests for tools/check.py. Run: python3 -I -m unittest discover -s tools/tests -v

Each test scaffolds a throwaway project into a temp directory, edits it, and asserts on
the validator's errors and warnings. No network, no fixtures outside this file.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import check  # noqa: E402
import scaffold  # noqa: E402

TODAY = dt.date(2026, 10, 31)
DAY = TODAY.isoformat()

ITEM = """---
id: {id}
title: {title}
milestone: {milestone}
priority: {priority}
status: {status}
role: {role}
depends_on: {depends_on}
questions: {questions}
owner: {owner}
updated: {updated}
---

## Goal
Test item.
"""

QUESTION = """
## {id} A question
- **Status:** {status}
- **Tags:** process
- **Raised:** {day} by researcher
- **Blocks:**
- **Why it matters:** test
- **Answer:**
"""

ROW = "| {when} | {role} | {model} | {item} | {runs} | {outcome} | {turns} | {problem} | {resolution} |\n"


class Project:
    """A scaffolded project in a temp dir with helpers to edit it."""

    def __init__(self, tmp: str):
        self.root = Path(tmp)
        scaffold.scaffold(self.root, "example", "Approver", agents=False, today=TODAY)
        self.project = self.root / "project"

    def item(self, id: str, **kw) -> Path:
        fields = dict(
            id=id, title=f"Item {id}", milestone="M0", priority="P1", status="idea", role="implementer",
            depends_on="", questions="", owner="", updated=DAY,
        )
        fields.update(kw)
        path = self.project / "backlog" / f"{id}-test.md"
        path.write_text(ITEM.format(**fields), encoding="utf-8")
        return path

    def question(self, id: str, status: str = "open") -> None:
        with (self.project / "questions.md").open("a", encoding="utf-8") as f:
            f.write(QUESTION.format(id=id, status=status, day=DAY))

    def journal(self, *rows: dict, day: str = DAY, heading: str | None = None) -> None:
        text = f"\n## {heading or day}\n\n| Date-time | Role | Model | Item | Runs | Outcome | Human turns | Problem | Resolution |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        for r in rows:
            fields = dict(when=f"{day} 10:00", role="implementer", model="sonnet", item="-", runs="1",
                          outcome="done", turns="0", problem="", resolution="")
            fields.update(r)
            text += ROW.format(**fields)
        with (self.project / "activity.md").open("a", encoding="utf-8") as f:
            f.write(text)

    def config(self, replace: dict[str, str]) -> None:
        path = self.project / "process.toml"
        text = path.read_text(encoding="utf-8")
        for old, new in replace.items():
            assert old in text, old
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")

    def run(self, write: bool = False) -> check.Result:
        return check.run(self.root, write=write, today=TODAY)


class ScaffoldedProjectTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = Project(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def assertErrors(self, result: check.Result, *patterns: str):
        self.assertEqual(len(result.errors), len(patterns), result.errors)
        for pat in patterns:
            self.assertTrue(any(re.search(pat, e) for e in result.errors), f"{pat!r} not in {result.errors}")

    def assertWarnings(self, result: check.Result, *patterns: str):
        self.assertEqual(len(result.warnings), len(patterns), result.warnings)
        for pat in patterns:
            self.assertTrue(any(re.search(pat, w) for w in result.warnings), f"{pat!r} not in {result.warnings}")

    # --- the scaffold itself

    def test_fresh_scaffold_passes_and_writes_index(self):
        result = self.p.run(write=True)
        self.assertErrors(result)
        self.assertWarnings(result)  # B-001 is `ready`, which needs no journal row
        index = (self.p.project / "backlog" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("[B-001](B-001-adopt-the-process.md)", index)
        self.assertIn("Counts: ready 1", index)
        self.assertEqual(result.journal_rows, 1)

    def test_scaffold_substitutes_placeholders_everywhere(self):
        for path in self.p.root.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".toml", ".yml"}:
                self.assertNotIn("{{", path.read_text(encoding="utf-8"), path)
        workflow = (self.p.project / "WORKFLOW.md").read_text(encoding="utf-8")
        self.assertIn("Approver", workflow)
        self.assertIn('name = "example"', (self.p.project / "process.toml").read_text(encoding="utf-8"))

    def test_scaffold_never_overwrites_without_force(self):
        marker = self.p.project / "WORKFLOW.md"
        marker.write_text("mine", encoding="utf-8")
        report = scaffold.scaffold(self.p.root, "example", today=TODAY)
        self.assertIn("project/WORKFLOW.md", report.skipped)
        self.assertEqual(marker.read_text(encoding="utf-8"), "mine")
        report = scaffold.scaffold(self.p.root, "example", force=True, today=TODAY)
        self.assertIn("project/WORKFLOW.md", report.written)
        self.assertNotEqual(marker.read_text(encoding="utf-8"), "mine")

    def test_existing_claude_md_is_left_alone(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "CLAUDE.md").write_text("# existing\n", encoding="utf-8")
            report = scaffold.scaffold(root, "example", agents=False, today=TODAY)
            self.assertEqual((root / "CLAUDE.md").read_text(encoding="utf-8"), "# existing\n")
            self.assertIn("project/CLAUDE-process-sections.md", report.written)
            self.assertTrue(any("Merge them" in n for n in report.notes))

    def test_scaffold_copies_agents_and_validator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scaffold.scaffold(root, "example", agents=True, today=TODAY)
            agents = sorted(p.name for p in (root / ".claude" / "agents").glob("*.md"))
            self.assertEqual(agents, sorted(p.name for p in scaffold.AGENTS.glob("*.md")))
            self.assertGreaterEqual(len(agents), 8)
            copied = (root / "project" / "tools" / "check.py").read_text(encoding="utf-8")
            self.assertEqual(copied, scaffold.CHECK.read_text(encoding="utf-8"))

    def test_missing_config_is_one_error(self):
        (self.p.project / "process.toml").unlink()
        self.assertErrors(self.p.run(), r"process.toml: not found")

    # --- front matter

    def test_front_matter_required_keys(self):
        path = self.p.item("B-002")
        path.write_text(path.read_text(encoding="utf-8").replace("priority: P1\n", ""), encoding="utf-8")
        self.assertErrors(self.p.run(), r"B-002-test.md: missing keys \['priority'\]")

    def test_missing_front_matter(self):
        (self.p.project / "backlog" / "B-002-test.md").write_text("no front matter\n", encoding="utf-8")
        self.assertErrors(self.p.run(), r"missing front matter")

    def test_id_must_match_file_name_and_be_unique(self):
        self.p.item("B-002")
        (self.p.project / "backlog" / "B-003-other.md").write_text(
            ITEM.format(id="B-002", title="dup", milestone="M0", priority="P1", status="idea", role="planner",
                        depends_on="", questions="", owner="", updated=DAY), encoding="utf-8")
        self.assertErrors(self.p.run(), r"id B-002 does not match file name", r"duplicate id B-002")

    def test_vocabulary_comes_from_config(self):
        self.p.item("B-002", status="shipped", role="wizard", milestone="M9", priority="P7")
        self.assertErrors(
            self.p.run(),
            r"unknown status 'shipped'", r"unknown role 'wizard'", r"unknown milestone 'M9'", r"unknown priority 'P7'",
        )
        self.p.config({'milestones = ["spec", "M0", "M1", "M2", "later"]': 'milestones = ["spec", "M0", "M9", "later"]'})
        self.p.config({"operator = \"haiku\"": "operator = \"haiku\"\nwizard = \"opus\""})
        self.p.config({'priorities = ["P0", "P1", "P2"]': 'priorities = ["P0", "P1", "P2", "P7"]'})
        self.p.config({'statuses = ["idea", "blocked"': 'statuses = ["idea", "shipped", "blocked"'})
        self.assertErrors(self.p.run())

    def test_human_is_always_a_valid_role(self):
        self.p.item("B-002", role="human")
        self.assertErrors(self.p.run())

    def test_bad_date_is_an_error_and_stale_is_a_warning(self):
        self.p.item("B-002", updated="yesterday")
        self.assertErrors(self.p.run(), r"B-002: bad date 'yesterday'")
        self.p.item("B-002", updated="2026-10-01")
        result = self.p.run()
        self.assertErrors(result)
        self.assertIn("B-002: not updated since 2026-10-01", result.warnings)
        self.p.item("B-002", updated="2026-10-01", status="done")
        self.assertNotIn("B-002: not updated since 2026-10-01", self.p.run().warnings)

    def test_stale_days_is_configurable(self):
        self.p.item("B-002", updated="2026-10-25")
        self.assertNotIn("B-002: not updated since 2026-10-25", self.p.run().warnings)
        self.p.config({"stale_days = 14": "stale_days = 3"})
        self.assertIn("B-002: not updated since 2026-10-25", self.p.run().warnings)

    # --- status transitions versus dependencies and questions

    def test_ready_requires_done_dependencies_and_answered_questions(self):
        self.p.item("B-002", status="idea")
        self.p.question("Q-001", "open")
        self.p.item("B-003", status="ready", depends_on="B-002", questions="Q-001")
        self.assertErrors(self.p.run(), r"B-003: ready but blocked by \['B-002', 'Q-001'\]")
        self.p.item("B-002", status="done")
        self.p.question("Q-001", "answered")  # a later entry with the same id wins? no: ids are unique
        (self.p.project / "questions.md").write_text(
            (self.p.project / "questions.md").read_text(encoding="utf-8").replace("- **Status:** open", "- **Status:** answered"),
            encoding="utf-8")
        self.assertErrors(self.p.run())

    def test_blocked_needs_a_blocker(self):
        self.p.item("B-002", status="blocked")
        self.assertErrors(self.p.run(), r"B-002: blocked with nothing blocking it")
        self.p.question("Q-001", "open")
        self.p.item("B-002", status="blocked", questions="Q-001")
        self.assertErrors(self.p.run())

    def test_unknown_references(self):
        self.p.item("B-002", status="idea", depends_on="B-099", questions="Q-099")
        self.assertErrors(self.p.run(), r"B-002: depends_on unknown item B-099", r"B-002: refers to unknown question Q-099")

    def test_in_progress_and_review_need_an_owner(self):
        self.p.item("B-002", status="in-progress")
        self.p.item("B-003", status="review")
        self.assertErrors(self.p.run(), r"B-002: in-progress without an owner", r"B-003: review without an owner")
        self.p.item("B-002", status="in-progress", owner="sonnet-run-1")
        self.p.item("B-003", status="review", owner="pr-4")
        self.assertErrors(self.p.run())

    def test_question_status_vocabulary(self):
        self.p.question("Q-001", "maybe")
        self.assertErrors(self.p.run(), r"Q-001: unknown status 'maybe'")

    # --- the activity journal

    def test_journal_rows_are_validated(self):
        self.p.journal(
            dict(role="wizard"), dict(model="gpt"), dict(outcome="meh"), dict(runs="two"), dict(turns="x"),
        )
        self.assertErrors(
            self.p.run(),
            r"activity.md:\d+: unknown role 'wizard'", r"unknown model 'gpt'", r"unknown outcome 'meh'",
            r"runs 'two' is not a whole number", r"human turns 'x' is not a whole number",
        )

    def test_journal_heading_must_be_a_date_and_rows_must_match_it(self):
        self.p.journal(dict(), heading="Friday")
        self.assertErrors(self.p.run(), r"heading 'Friday' is not a YYYY-MM-DD date", r"table row before any valid day heading")
        self.p = Project(self.tmp.name) if False else self.p  # keep instance
        (self.p.project / "activity.md").write_text(
            (self.p.project / "activity.md").read_text(encoding="utf-8").replace("## Friday", "## 2026-11-01"),
            encoding="utf-8")
        self.assertErrors(self.p.run(), r"row date 2026-10-31 is not under its heading 2026-11-01")

    def test_journal_bad_datetime_and_short_row(self):
        self.p.journal(dict(when="noon"))
        with (self.p.project / "activity.md").open("a", encoding="utf-8") as f:
            f.write("| 2026-10-31 11:00 | human | human |\n")
        self.assertErrors(self.p.run(), r"'noon' is not a date-time", r"row has 3 cells, 9 expected")

    def test_journal_out_of_order_day_is_a_warning(self):
        self.p.journal(dict(when="2026-10-30 09:00"), day="2026-10-30")
        result = self.p.run()
        self.assertErrors(result)
        self.assertTrue(any("out of order" in w for w in result.warnings), result.warnings)

    def test_review_or_done_without_a_journal_row_that_day_warns(self):
        self.p.item("B-002", status="done", updated=DAY)
        self.p.item("B-003", status="review", owner="pr-1", updated=DAY)
        result = self.p.run()
        self.assertIn(f"B-002: done on {DAY} has no journal row that day", result.warnings)
        self.assertIn(f"B-003: review on {DAY} has no journal row that day", result.warnings)
        self.p.journal(dict(item="B-002"), dict(item="B-003, Q-001", role="reviewer", model="opus"))
        result = self.p.run()
        self.assertNotIn(f"B-002: done on {DAY} has no journal row that day", result.warnings)
        self.assertNotIn(f"B-003: review on {DAY} has no journal row that day", result.warnings)

    def test_journal_can_be_disabled(self):
        self.p.journal(dict(role="wizard"))
        self.p.item("B-002", status="done")
        self.p.config({"enabled = true": "enabled = false"})
        result = self.p.run()
        self.assertErrors(result)
        self.assertFalse(any("journal row" in w for w in result.warnings))
        self.assertEqual(result.journal_rows, 0)

    # --- configuration problems

    def test_semantic_statuses_cannot_be_removed(self):
        self.p.config({'statuses = ["idea", "blocked", "ready", "in-progress", "review", "done", "dropped"]':
                       'statuses = ["idea", "ready", "done"]'})
        result = self.p.run()
        self.assertTrue(any("backlog.statuses must include ['blocked', 'dropped', 'in-progress', 'review']" in e
                            for e in result.errors), result.errors)

    def test_unknown_section_and_bad_types_are_errors(self):
        self.p.config({"[issues]": "[extras]\nfoo = 1\n\n[issues]", "stale_days = 14": 'stale_days = "soon"'})
        result = self.p.run()
        self.assertTrue(any("unknown section [extras]" in e for e in result.errors), result.errors)
        self.assertTrue(any("stale_days must be a positive integer" in e for e in result.errors), result.errors)

    def test_malformed_toml_is_one_config_error(self):
        (self.p.project / "process.toml").write_text("[project\n", encoding="utf-8")
        result = self.p.run()
        self.assertTrue(any("cannot read config" in e for e in result.errors), result.errors)

    # --- index

    def test_index_not_written_when_errors(self):
        index = self.p.project / "backlog" / "INDEX.md"
        self.p.run(write=True)
        before = index.read_text(encoding="utf-8")
        self.p.item("B-002", status="blocked")
        self.p.run(write=True)
        self.assertEqual(index.read_text(encoding="utf-8"), before)

    def test_index_orders_by_priority_then_id_and_marks_open_questions(self):
        self.p.question("Q-001", "open")
        self.p.item("B-002", priority="P2", status="idea", questions="Q-001")
        self.p.item("B-003", priority="P0", status="idea")
        text = check.render_index(self.p.run().items, {"Q-001": "open"}, check.load_config(self.p.project / "process.toml"))
        rows = [l for l in text.splitlines() if l.startswith("| [")]
        self.assertEqual([r.split("]")[0][3:] for r in rows], ["B-001", "B-003", "B-002"])  # P0 by id, then P2
        self.assertIn("| Q-001* |", rows[2])

    def test_main_exit_codes_and_summary_line(self):
        self.assertEqual(check.main(["--root", str(self.p.root), "--no-write"]), 0)
        self.p.item("B-002", status="blocked")
        self.assertEqual(check.main(["--root", str(self.p.root), "--no-write"]), 1)


if __name__ == "__main__":
    unittest.main()

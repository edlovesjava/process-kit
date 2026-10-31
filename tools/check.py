#!/usr/bin/env python3
"""Validate a project's tracking files and regenerate project/backlog/INDEX.md.

Usage: python3 -I check.py [--root DIR] [--no-write]

The root is the repository that holds `project/process.toml`. Without `--root` the
current directory is used when it holds `project/process.toml`; otherwise the script
assumes it was copied to `<root>/project/tools/check.py` by the scaffold.

Checks (every one from the source process, plus the activity journal):
  - backlog item front matter has the required keys and values from process.toml
  - ids are unique and match the file name
  - depends_on and questions refer to things that exist
  - `ready` items have all dependencies done and all questions answered
  - `blocked` items have something blocking them
  - `in-progress` / `review` items have an owner
  - items untouched for `stale_days` are reported (warning)
  - questions have a known status
  - activity journal: one `## YYYY-MM-DD` per UTC day, rows with a date-time inside
    that day, known role and model, outcome from the fixed set, integer counts
  - an item in `review` or `done` with no journal row naming it on its `updated` day
    is reported (warning)
Exit status is 1 on any error, 0 otherwise. Warnings never fail the run.

Standard library only; Python 3.11 or newer (tomllib).
"""
from __future__ import annotations

import datetime as dt
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

CONFIG_NAME = "process.toml"
# Statuses the checks themselves reason about. A project may add statuses in
# process.toml but may not remove these; see docs/tailoring.md.
SEMANTIC_STATUSES = {"ready", "blocked", "in-progress", "review", "done", "dropped"}
REQUIRED_KEYS = {"id", "title", "milestone", "priority", "status", "role", "updated"}
KNOWN_SECTIONS = {"project", "backlog", "roles", "questions", "journal", "issues"}


@dataclass
class Config:
    statuses: set[str]
    priorities: list[str]
    milestones: set[str]
    stale_days: int
    roles: dict[str, str]
    question_statuses: set[str]
    journal_enabled: bool
    journal_file: str
    journal_models: set[str]
    journal_outcomes: set[str]
    approver: str = "the approver"
    problems: list[str] = field(default_factory=list)


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    items: dict[str, dict[str, str]] = field(default_factory=dict)
    questions: dict[str, str] = field(default_factory=dict)
    journal_rows: int = 0

    @property
    def exit_code(self) -> int:
        return 1 if self.errors else 0


# ---------------------------------------------------------------- configuration


def load_config(path: Path) -> Config:
    """Read process.toml. Missing or malformed sections become config problems."""
    problems: list[str] = []
    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raw = {}
        problems.append(f"{path.name}: cannot read config: {exc}")

    for section in raw:
        if section not in KNOWN_SECTIONS:
            problems.append(f"{path.name}: unknown section [{section}]")

    def section(name: str) -> dict:
        value = raw.get(name, {})
        if not isinstance(value, dict):
            problems.append(f"{path.name}: [{name}] must be a table")
            return {}
        return value

    def str_list(table: dict, key: str, where: str, default: list[str]) -> list[str]:
        value = table.get(key, default)
        if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
            problems.append(f"{path.name}: {where}.{key} must be a list of strings")
            return default
        return value

    project, backlog, roles = section("project"), section("backlog"), section("roles")
    questions, journal = section("questions"), section("journal")

    statuses = set(str_list(backlog, "statuses", "backlog", sorted(SEMANTIC_STATUSES | {"idea"})))
    missing = SEMANTIC_STATUSES - statuses
    if missing:
        problems.append(f"{path.name}: backlog.statuses must include {sorted(missing)}")
    priorities = str_list(backlog, "priorities", "backlog", ["P0", "P1", "P2"])
    milestones = set(str_list(backlog, "milestones", "backlog", []))
    if not milestones:
        problems.append(f"{path.name}: backlog.milestones must name at least one milestone")
    stale_days = backlog.get("stale_days", 14)
    if not isinstance(stale_days, int) or stale_days < 1:
        problems.append(f"{path.name}: backlog.stale_days must be a positive integer")
        stale_days = 14

    if not roles or not all(isinstance(v, str) for v in roles.values()):
        problems.append(f"{path.name}: [roles] must map each role name to the model it runs on")
        roles = {}

    approver = project.get("approver", "the approver")
    if not isinstance(approver, str):
        problems.append(f"{path.name}: project.approver must be a string")
        approver = "the approver"

    return Config(
        statuses=statuses,
        priorities=priorities,
        milestones=milestones,
        stale_days=stale_days,
        roles=dict(roles),
        question_statuses=set(str_list(questions, "statuses", "questions", ["open", "answered", "superseded"])),
        journal_enabled=bool(journal.get("enabled", True)),
        journal_file=str(journal.get("file", "activity.md")),
        journal_models=set(str_list(journal, "models", "journal", sorted(set(roles.values()) | {"human"}))),
        journal_outcomes=set(
            str_list(journal, "outcomes", "journal", ["done", "partial", "blocked", "failed", "decided", "deferred"])
        ),
        approver=approver,
        problems=problems,
    )


# ---------------------------------------------------------------- parsing


def parse_front_matter(text: str) -> dict[str, str] | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        out[key.strip()] = value.split("#", 1)[0].strip()
    return out


def split_ids(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


def load_questions(path: Path) -> dict[str, str]:
    """Return {Q-ID: status} from questions.md."""
    statuses: dict[str, str] = {}
    current = None
    if not path.exists():
        return statuses
    for line in path.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^## (Q-\d{3})\b", line)
        if h:
            current = h.group(1)
            statuses[current] = "open"
            continue
        s = re.match(r"^- \*\*Status:\*\* (\w+)", line)
        if s and current:
            statuses[current] = s.group(1)
    return statuses


@dataclass
class JournalRow:
    day: dt.date
    when: str
    role: str
    model: str
    item: str
    runs: str
    outcome: str
    human_turns: str
    line_no: int


def table_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_separator(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c) and any(cells)


def load_journal(path: Path, result: Result) -> list[JournalRow]:
    """Parse activity.md: `## YYYY-MM-DD` headings, one table per day."""
    rows: list[JournalRow] = []
    if not path.exists():
        return rows
    name = path.name
    day: dt.date | None = None
    last_day: dt.date | None = None
    seen_header = False
    seen_heading = False  # tables before the first `##` heading document the format and are skipped
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        h = re.match(r"^## (.+)$", line)
        if h:
            seen_header = False
            seen_heading = True
            try:
                day = dt.date.fromisoformat(h.group(1).strip())
            except ValueError:
                result.errors.append(f"{name}:{n}: heading '{h.group(1).strip()}' is not a YYYY-MM-DD date")
                day = None
                continue
            if last_day and day < last_day:
                result.warnings.append(f"{name}:{n}: day {day} is out of order (journal is append-only, newest last)")
            last_day = day
            continue
        if not line.lstrip().startswith("|") or not seen_heading:
            continue
        cells = table_cells(line)
        if is_separator(cells):
            continue
        if not seen_header:
            seen_header = True  # the column header row
            continue
        if day is None:
            result.errors.append(f"{name}:{n}: table row before any valid day heading")
            continue
        if len(cells) < 9:
            result.errors.append(f"{name}:{n}: row has {len(cells)} cells, 9 expected")
            continue
        when = cells[0]
        try:
            stamp = dt.datetime.fromisoformat(when.replace("Z", "+00:00"))
        except ValueError:
            result.errors.append(f"{name}:{n}: '{when}' is not a date-time (YYYY-MM-DD HH:MM)")
            continue
        if stamp.date() != day:
            result.errors.append(f"{name}:{n}: row date {stamp.date()} is not under its heading {day}")
        rows.append(JournalRow(day, when, cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], n))
    return rows


# ---------------------------------------------------------------- checks


def check_items(root: Path, cfg: Config, result: Result, today: dt.date) -> None:
    backlog = root / "project" / "backlog"
    items = result.items
    for path in sorted(backlog.glob("B-*.md")):
        fm = parse_front_matter(path.read_text(encoding="utf-8"))
        if fm is None:
            result.errors.append(f"{path.name}: missing front matter")
            continue
        missing = REQUIRED_KEYS - fm.keys()
        if missing:
            result.errors.append(f"{path.name}: missing keys {sorted(missing)}")
            continue
        item_id = fm["id"]
        if not path.name.startswith(item_id + "-"):
            result.errors.append(f"{path.name}: id {item_id} does not match file name")
        if item_id in items:
            result.errors.append(f"{path.name}: duplicate id {item_id}")
        items[item_id] = fm
        fm["_file"] = path.name
        if fm["status"] not in cfg.statuses:
            result.errors.append(f"{item_id}: unknown status '{fm['status']}'")
        if fm["role"] not in cfg.roles and fm["role"] != "human":
            result.errors.append(f"{item_id}: unknown role '{fm['role']}'")
        if fm["milestone"] not in cfg.milestones:
            result.errors.append(f"{item_id}: unknown milestone '{fm['milestone']}'")
        if fm["priority"] not in cfg.priorities:
            result.errors.append(f"{item_id}: unknown priority '{fm['priority']}'")
        try:
            updated = dt.date.fromisoformat(fm["updated"])
            if (today - updated).days > cfg.stale_days and fm["status"] not in {"done", "dropped"}:
                result.warnings.append(f"{item_id}: not updated since {fm['updated']}")
        except ValueError:
            result.errors.append(f"{item_id}: bad date '{fm['updated']}'")

    for item_id, fm in items.items():
        deps = split_ids(fm.get("depends_on", ""))
        qs = split_ids(fm.get("questions", ""))
        for d in deps:
            if d not in items:
                result.errors.append(f"{item_id}: depends_on unknown item {d}")
        for q in qs:
            if q not in result.questions:
                result.errors.append(f"{item_id}: refers to unknown question {q}")
        unmet = [d for d in deps if d in items and items[d]["status"] != "done"]
        open_qs = [q for q in qs if result.questions.get(q) == "open"]
        status = fm["status"]
        if status == "ready" and (unmet or open_qs):
            result.errors.append(f"{item_id}: ready but blocked by {unmet + open_qs}")
        if status == "blocked" and not (unmet or open_qs):
            result.errors.append(f"{item_id}: blocked with nothing blocking it")
        if status in {"in-progress", "review"} and not fm.get("owner"):
            result.errors.append(f"{item_id}: {status} without an owner")


def check_journal(rows: list[JournalRow], cfg: Config, result: Result) -> None:
    known_roles = set(cfg.roles) | {"human"}
    for r in rows:
        where = f"{cfg.journal_file}:{r.line_no}"
        if r.role not in known_roles:
            result.errors.append(f"{where}: unknown role '{r.role}'")
        if r.model not in cfg.journal_models:
            result.errors.append(f"{where}: unknown model '{r.model}'")
        if r.outcome not in cfg.journal_outcomes:
            result.errors.append(f"{where}: unknown outcome '{r.outcome}'")
        for label, value in (("runs", r.runs), ("human turns", r.human_turns)):
            if value and not value.isdigit():
                result.errors.append(f"{where}: {label} '{value}' is not a whole number")
    # A status change to review or done should leave a trace in the journal that day.
    by_day: dict[dt.date, list[JournalRow]] = {}
    for r in rows:
        by_day.setdefault(r.day, []).append(r)
    for item_id, fm in result.items.items():
        if fm["status"] not in {"review", "done"}:
            continue
        try:
            day = dt.date.fromisoformat(fm["updated"])
        except ValueError:
            continue
        if not any(item_id in r.item for r in by_day.get(day, [])):
            result.warnings.append(f"{item_id}: {fm['status']} on {fm['updated']} has no journal row that day")


# ---------------------------------------------------------------- index


def render_index(items: dict[str, dict[str, str]], questions: dict[str, str], cfg: Config) -> str:
    order = {p: i for i, p in enumerate(cfg.priorities)}
    rows = sorted(items.values(), key=lambda f: (order.get(f["priority"], len(order)), f["id"]))
    lines = [
        "# Backlog index",
        "",
        "Generated by `python3 -I project/tools/check.py`. Do not edit.",
        "",
        "| ID | Title | Milestone | Pri | Status | Role | Depends on | Questions | Updated |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for f in rows:
        qs = ", ".join(
            f"{q}{'' if questions.get(q) == 'answered' else '*'}" for q in split_ids(f.get("questions", ""))
        )
        lines.append(
            f"| [{f['id']}]({f['_file']}) | {f['title']} | {f['milestone']} | {f['priority']} | "
            f"{f['status']} | {f['role']} | {f.get('depends_on', '')} | {qs} | {f['updated']} |"
        )
    lines += ["", "`*` marks a question still open.", ""]
    by_status: dict[str, int] = {}
    for f in items.values():
        by_status[f["status"]] = by_status.get(f["status"], 0) + 1
    lines.append("Counts: " + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items())))
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------- entry points


def run(root: Path, write: bool = True, today: dt.date | None = None) -> Result:
    """Run every check under `root` and return the result. Pure apart from INDEX.md."""
    today = today or dt.date.today()
    result = Result()
    project = root / "project"
    config_path = project / CONFIG_NAME
    if not config_path.exists():
        result.errors.append(f"{config_path.relative_to(root)}: not found (run the scaffold first)")
        return result
    cfg = load_config(config_path)
    result.errors.extend(cfg.problems)

    result.questions = load_questions(project / "questions.md")
    for q, status in result.questions.items():
        if status not in cfg.question_statuses:
            result.errors.append(f"{q}: unknown status '{status}'")

    check_items(root, cfg, result, today)

    if cfg.journal_enabled:
        rows = load_journal(project / cfg.journal_file, result)
        result.journal_rows = len(rows)
        check_journal(rows, cfg, result)

    if write and not result.errors:
        index = project / "backlog" / "INDEX.md"
        index.write_text(render_index(result.items, result.questions, cfg), encoding="utf-8")
    return result


def find_root(argv: list[str]) -> Path:
    if "--root" in argv:
        return Path(argv[argv.index("--root") + 1]).resolve()
    cwd = Path.cwd()
    if (cwd / "project" / CONFIG_NAME).exists():
        return cwd
    return Path(__file__).resolve().parents[2]


def main(argv: list[str]) -> int:
    root = find_root(argv)
    result = run(root, write="--no-write" not in argv)
    for w in result.warnings:
        print(f"warning: {w}")
    for e in result.errors:
        print(f"error: {e}")
    open_count = sum(1 for s in result.questions.values() if s == "open")
    print(
        f"items={len(result.items)} questions_open={open_count} journal_rows={result.journal_rows} "
        f"errors={len(result.errors)} warnings={len(result.warnings)}"
    )
    return result.exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

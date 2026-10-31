#!/usr/bin/env python3
"""Scaffold the process-kit delivery process into a project repository.

Usage:
  python3 -I tools/scaffold.py --target DIR --name NAME [--approver NAME]
                                [--no-agents] [--force] [--dry-run]

Writes, relative to DIR (never overwriting unless --force):
  CLAUDE.md                        process sections with an invariants placeholder; when a
                                   CLAUDE.md already exists the sections go to
                                   project/CLAUDE-process-sections.md for you to merge
  project/                         process.toml, WORKFLOW.md, SITREP.md, questions.md,
                                   decisions.md, milestones.md, activity.md, backlog/
  project/tools/check.py           a copy of the kit's validator (the project owns it)
  docs/adr/ docs/arch/ docs/process/ docs/design/nfrs.md
  .github/workflows/tracking.yml   CI that runs the validator on project/ changes
  .claude/agents/*.md              the role agents, so cloud sessions (which do not load
                                   project plugins) still have them; skip with --no-agents

Placeholders in templates: {{PROJECT_NAME}}, {{APPROVER}}, {{DATE}}.
Standard library only; Python 3.11 or newer.
"""
from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
TEMPLATES = KIT / "templates"
AGENTS = KIT / "agents"
CHECK = KIT / "tools" / "check.py"


@dataclass
class Report:
    written: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def render(text: str, name: str, approver: str, date: str) -> str:
    return text.replace("{{PROJECT_NAME}}", name).replace("{{APPROVER}}", approver).replace("{{DATE}}", date)


def place(target: Path, rel: str, content: str, report: Report, force: bool, dry_run: bool) -> None:
    dest = target / rel
    if dest.exists() and not force:
        report.skipped.append(rel)
        return
    if not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
    report.written.append(rel)


def scaffold(
    target: Path,
    name: str,
    approver: str = "the approver",
    agents: bool = True,
    force: bool = False,
    dry_run: bool = False,
    today: dt.date | None = None,
) -> Report:
    date = (today or dt.datetime.now(dt.timezone.utc).date()).isoformat()
    report = Report()
    target = target.resolve()

    for src in sorted(p for p in TEMPLATES.rglob("*") if p.is_file()):
        rel = src.relative_to(TEMPLATES).as_posix()
        content = render(src.read_text(encoding="utf-8"), name, approver, date)
        if rel == "CLAUDE.md" and (target / "CLAUDE.md").exists() and not force:
            rel = "project/CLAUDE-process-sections.md"
            report.notes.append(
                "CLAUDE.md exists; the process sections were written to "
                "project/CLAUDE-process-sections.md. Merge them into CLAUDE.md and delete the copy."
            )
        place(target, rel, content, report, force, dry_run)

    place(target, "project/tools/check.py", CHECK.read_text(encoding="utf-8"), report, force, dry_run)
    if not dry_run and "project/tools/check.py" in report.written:
        shutil.copymode(CHECK, target / "project" / "tools" / "check.py")

    if agents:
        for src in sorted(AGENTS.glob("*.md")):
            place(target, f".claude/agents/{src.name}", src.read_text(encoding="utf-8"), report, force, dry_run)
    else:
        report.notes.append(
            "Agents were not copied. Enable the process-kit plugin instead, or copy agents/ to .claude/agents/."
        )
    return report


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", required=True, help="repository root to scaffold into")
    ap.add_argument("--name", required=True, help="project name used in the templates")
    ap.add_argument("--approver", default="the approver", help="the one human who decides")
    ap.add_argument("--no-agents", action="store_true", help="do not copy agents/ to .claude/agents/")
    ap.add_argument("--force", action="store_true", help="overwrite files that already exist")
    ap.add_argument("--dry-run", action="store_true", help="print what would be written, write nothing")
    args = ap.parse_args(argv)

    target = Path(args.target)
    if not target.is_dir():
        print(f"error: target {target} is not a directory", file=sys.stderr)
        return 2
    report = scaffold(target, args.name, args.approver, not args.no_agents, args.force, args.dry_run)
    verb = "would_write" if args.dry_run else "written"
    for rel in report.written:
        print(f"{verb}={rel}")
    for rel in report.skipped:
        print(f"skipped={rel} reason=exists")
    for note in report.notes:
        print(f"note: {note}")
    print(f"{verb}_count={len(report.written)} skipped_count={len(report.skipped)}")
    print("next: python3 -I project/tools/check.py   (from the project root)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

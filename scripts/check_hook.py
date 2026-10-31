#!/usr/bin/env python3
"""PostToolUse hook: run the tracking validator after an edit under project/.

Reads the hook payload on stdin, and does nothing unless the edited file lies under
`<project>/project/` and `<project>/project/process.toml` exists. Then runs the
project's own copy of the validator (`project/tools/check.py`, falling back to the kit's)
with `--no-write`, and on errors exits 2 so the output reaches Claude. Any failure of the
hook itself exits 0: the hook must never block work in a project that does not use the kit.

This is the only automation the kit ships. Journal rows are written by hand (see
project/questions.md Q-003 in the kit); a hook that appended them is recorded there as the
alternative.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        edited = payload.get("tool_input", {}).get("file_path")
        cwd = Path(payload.get("cwd") or Path.cwd()).resolve()
        if not edited:
            return 0
        edited_path = Path(edited)
        if not edited_path.is_absolute():
            edited_path = cwd / edited_path
        edited_path = edited_path.resolve()
        project = cwd / "project"
        if not (project / "process.toml").exists() or project not in edited_path.parents:
            return 0
        own = project / "tools" / "check.py"
        kit = Path(__file__).resolve().parents[1] / "tools" / "check.py"
        script = own if own.exists() else kit
        run = subprocess.run(
            [sys.executable, "-I", str(script), "--root", str(cwd), "--no-write"],
            capture_output=True, text=True, timeout=15,
        )
        if run.returncode != 0:
            sys.stderr.write("process-kit validator found errors after this edit:\n" + run.stdout + run.stderr)
            return 2
        return 0
    except Exception:  # noqa: BLE001  the hook must never fail the tool call
        return 0


if __name__ == "__main__":
    sys.exit(main())

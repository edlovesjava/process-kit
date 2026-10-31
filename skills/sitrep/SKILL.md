---
name: sitrep
description: Add a dated handoff entry to project/SITREP.md describing what just happened, what is in flight and what the next session should do first. Use before a session ends with work in flight, after a merge, or when asked for a "handoff" or "sitrep".
allowed-tools: Bash, Read, Edit
---
Write the handoff the next session will read first. Newest entry at the top; keep it
under a screen; detail belongs in the files it links.

1. Gather: `git status -sb`, `git log --oneline -10`, the validator output
   (`python3 -I project/tools/check.py`), open PRs you know about, the questions you
   raised or saw answered, the decisions the approver still owes.
2. Insert directly under the introduction in `project/SITREP.md`, above the previous
   entry:

   ```
   ## YYYY-MM-DD Headline in one line (session or branch name)

   **Why this entry.** One or two sentences.

   **State.** What is merged, what is on which branch or PR, what the validator says.

   **Decisions the approver must make.** Q-IDs and ADRs with their recommendations.

   **What is ready now.** Items by priority, and the one to pick first.

   **Conventions a fresh session must keep.** Only those not already in CLAUDE.md or
   WORKFLOW.md, or the ones most often missed.

   **Do not.** The handful of things that would cost a session to undo.
   ```

3. If you are correcting an earlier entry (a wrong root cause, a changed fact), add a
   dated **Corrected YYYY-MM-DD:** sentence inside that entry. Never silently rewrite it;
   a wrong cause that stood for a session is itself a process finding.
4. Trim or remove old entries whose content now lives in items, questions or notes.
5. Add a journal row for the session's work if none exists for today's dispatches.

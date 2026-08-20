---
name: odin-start-section
description: Start or resume an Odin course section when the user says they are starting a named section, creating only missing progress and notes scaffolding.
---

# Start an Odin section

Read the root and `courses/AGENTS.md`, the repository plan, conventions, and
curriculum map. Inspect `python3 tools/odin/repo_state.py --pretty`, README, the
target path, and analogous section-start history.

Resolve the named section from the curriculum map. Verify its current lesson list
against the official TOP course page and relevant lesson pages when practical;
report source-access failure instead of guessing. Do not infer that the next
mapped section has started.

Plan only missing work:

1. Update README current course/section and date only if it does not already name
   the section.
2. If absent, scaffold `notes.md` with the section heading, current official
   lesson headings, and start metadata matching recent convention. Use
   `tools/odin/scaffold.py section` with `--dry-run` first.
3. If the file exists, preserve it. Never overwrite notes or create lesson/future
   directories.

The operation is idempotent. Keep README progress and notes initialization as
separate commit concerns. If README already says CSS Foundations but its notes are
missing, propose only notes initialization. After edits and validation, follow the
root commit-approval contract and stop before committing.

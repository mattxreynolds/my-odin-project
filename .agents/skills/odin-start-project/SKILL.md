---
name: odin-start-project
description: Start a named formal Odin project, resolving its existing Issue, branch, path, current assignment, progress entry, and initial README without writing project code.
---

# Start an Odin project

Read root and project guidance plus the repository plan, conventions, curriculum
map, and project README template. Inspect `repo_state.py --project "<name>"`,
branches, directories, README,
recent project-start history, and all matching GitHub Issues. Reuse exactly one
pre-created formal-project Issue; never create a duplicate.

Open the current official assignment. Compare it with Issue path, branch, goal,
and acceptance criteria. Report meaningful drift rather than silently adopting
stale Issue prose. If the source is unavailable, disclose that and do not invent
requirements.

Before mutating, present the intended topology and obtain approval for commits and
pushes under the root contract. The normal topology is: update README progress on
`main`; commit and push it; create the canonical project branch from updated main;
create the project directory and initialize README; commit and push that README.
Do not open a PR. Re-check remote state before execution and invalidate approval if
the reviewed diff/topology changed.

Follow every applicable `START:` instruction in the template. Populate only
factual project identity/status/date/URL/path, assignment summaries and objectives,
supported expected technology, and real initial run instructions. Do not invent
features, challenges, decisions, limitations, or retrospective content. Use
`scaffold.py project-readme` with a dry run when helpful; it refuses overwrites.
If the branch, directory, README, progress entry, or Issue already exists, reuse it
and propose only genuinely missing work.

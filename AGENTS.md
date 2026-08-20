# Repository guidance for Codex

This repository is Matt's learning record for The Odin Project (TOP). Read
`ODIN_REPOSITORY_PLAN.md`, then `docs/repository-conventions.md`,
`docs/curriculum-map.md`, and the relevant templates before changing repository
administration. Those files define local structure and naming; the current
official TOP lesson or assignment defines curriculum content.

## Learning boundary

- Automate repository mechanics, scaffolding, factual documentation, validation,
  source verification, Git preparation, and review.
- Do not write exercise or assignment solutions, finish incomplete project code,
  silently repair implementations, or invent learning, challenges, decisions, or
  retrospectives.
- For authored code, explain the apparent intent and misconception, teach the
  concept, and offer progressive hints before replacement code.
- Preserve completed notes as learning history unless Matt explicitly requests a
  correction or cleanup.

## Sources and preservation

- Verify curriculum claims against current pages on `theodinproject.com` or the
  official `TheOdinProject/curriculum` repository when practical. Disclose an
  access failure; never invent current requirements.
- Inspect before editing. Do not overwrite authored material, create future empty
  curriculum directories, create duplicate project Issues, or introduce a root
  JavaScript workspace, root `package.json`, shared runtime dependencies, hooks,
  MCP infrastructure, or nested Git repositories.
- Use `tools/odin/repo_state.py`, `validate_repo.py`, and `scaffold.py` for their
  deterministic jobs. They report or scaffold facts; semantic learning decisions
  remain with Codex.

## Git approval

- Follow the branch and commit conventions in the repository documentation.
- Before a commit or push, inspect status, diffs, analogous history, and remote
  state. Present an ordered plan with exact branch, message, files, purpose, and
  validation, then stop.
- A plain `Approved` authorizes only the exact displayed commits and associated
  pushes while the reviewed state is unchanged. Stage exact paths only; never use
  blanket staging.
- PR creation follows project completion and requires authorization. Merge is a
  separate gate requiring an unambiguous instruction such as `merge it`; verify
  head and checks again before merging.

Use the repository-local `odin-*` skills for the corresponding natural-language
workflows. An audit is always read-only.

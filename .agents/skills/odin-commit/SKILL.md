---
name: odin-commit
description: Plan and execute small repository-conventional Odin commits when the user asks to commit or says Approved after an exact commit plan.
---

# Prepare and execute Odin commits

Read root guidance and commit conventions. Inspect `git status`, staged and
unstaged diffs, current branch, relevant remote state, and recent analogous history.
Split work into the smallest coherent repository concerns; one workflow is not
necessarily one commit. Never use blanket staging.

Before any commit or push, show: what changed; validation; every proposed commit in
order; exact message; exact files; concise purpose; and branch. State that no commit
or push occurred, then stop.

`Approved` authorizes exactly that displayed plan and its disclosed pushes only if
the working-tree diff, index, files, messages, topology, and material remote state
still match. Re-check them immediately. Any mismatch invalidates approval: unstage
nothing destructively, show a revised plan, and stop.

For a valid approval, stage only each commit's explicit paths with
`git add -- <paths>`, inspect the staged diff, commit, then repeat. Push only the
disclosed branches/tags. Commit/push approval never authorizes PR creation or merge.
Merge requires a later unambiguous instruction and fresh PR/head/check verification.

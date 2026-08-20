---
name: odin-repo-audit
description: Perform a strictly read-only audit of Odin repository progress, curriculum mapping, project metadata, documentation, deployment, and mechanical health.
---

# Audit the Odin repository

This skill is strictly read-only. Do not fix, format, scaffold, stage, commit, push,
or change GitHub state. A later request to fix findings is a separate mutation.

Read root guidance and authoritative repository docs. Run `repo_state.py` and
`validate_repo.py`; inspect relevant diffs/history, project Issues, README links,
directories, notes, project READMEs, scripts, deployment evidence, and current
official curriculum sources where practical.

Check root progress against files; project table against directories/READMEs;
curriculum map against created paths; project Issues against map/path/branch rules;
approved statuses and dates; placeholders; links; premature empty directories;
stale active-project state; completed deployment state; applicable build/test
health; course readiness; attribution; obvious secrets/private information; and
meaningful curriculum drift. Do not claim remote/deployment health without checking.

Report each finding with severity (`error`, `warning`, or `info`), area, finding,
evidence, and suggested action. Separate deterministic findings from semantic or
source-dependent judgments. If no findings exist, state what was checked and any
unverified limitations.

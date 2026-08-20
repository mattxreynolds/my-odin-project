---
name: odin-finish-project
description: Verify and administratively finish an authored Odin project, complete factual documentation, gather personal reflection, and prepare its final PR lifecycle.
---

# Finish an Odin project

Read root and project guidance, the Issue, template, conventions, and current
official assignment. Inspect the actual implementation and compare it with current
requirements. Do not implement or silently repair assignment code; explain gaps
and let the user fix them.

Run only applicable commands that exist. Verify build/test/lint, deployment,
accessibility, attribution, secrets, and repository consistency as evidence permits.
Derive objective README facts (stack, structure, implemented features, commands,
testing, deployment configuration, verified accessibility, technical limitations,
and identifiable attribution). Ask concise questions for challenges, investigation,
learning, what went well, alternatives, personal rationale, and retrospective.
Never fabricate those sections or mark an empty retrospective complete.

After user-approved README wording, update project and root documentation in small
separate concerns and run the read-only audit. Present exact commits and pushes for
approval. Only after the project is ready and approved, create one non-draft PR
using `.github/pull_request_template.md`, the conventional project title, verified
facts, user reflection, and `Closes #<issue>`. Do not merge.

Treat `merge it` as a later separate gate. Before an authorized merge, verify the
expected head SHA, checks, and reviewed state. Prefer a merge commit per convention;
never force. Afterward verify main, Issue closure, and branch deletion.

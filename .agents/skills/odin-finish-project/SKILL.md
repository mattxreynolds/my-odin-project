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

Classify the finished output before planning deployment. Use the shared GitHub
Pages site for suitable client-only projects, an independent provider for projects
that need a server, database, secrets, storage, provider-specific behavior, or a
dedicated deployment, and no live deployment for non-runnable coursework. Follow
the deployment policy in the repository plan rather than assuming a provider.

For a shared Pages project, add it to `deploy/pages-projects.json` only when it is
ready to publish, run `tools/odin/build_pages.py` against a temporary output
directory, and verify the curated artifact. The current builder supports static
source projects only; extend it with the actual project-local install, build, and
output behavior when the first build-based project requires it. Do not add root
JavaScript dependencies. Check subpath-safe assets, base paths, and routing as
applicable.

Because the production Pages workflow runs from `main`, do not claim a new live
URL in the project PR. Keep the live demo marked as not deployed until the project
PR is merged, the exact Pages run succeeds, and the production pages and assets
are verified. Then update the project and root READMEs as a separate factual
documentation concern under the normal commit and PR approval gates.

After user-approved README wording, update project and root documentation in small
separate concerns and run the read-only audit. Present exact commits and pushes for
approval. Only after the project is ready and approved, create one non-draft PR
using `.github/pull_request_template.md`, the conventional project title, verified
facts, user reflection, and `Closes #<issue>`. Do not merge.

Treat `merge it` as a later separate gate. Before an authorized merge, verify the
expected head SHA, checks, and reviewed state. Prefer a merge commit per convention;
never force. Afterward verify main, Issue closure, and branch deletion.

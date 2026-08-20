---
name: odin-review-knowledge-check
description: Review Odin knowledge-check answers supplied in conversation, teach through gaps, and prepare approved lesson-scoped notes without doing the learning for the user.
---

# Review a knowledge check

Read the root and `courses/AGENTS.md`. Infer the lesson from the conversation,
active section, notes headings, and curriculum; do not require a URL when this is
reliable. Consult the current official lesson and its knowledge-check intent when
practical, disclosing any source failure.

For every answer, use exactly one classification: **Correct**, **Correct but
incomplete**, **Incorrect**, or **Unclear**. Judge demonstrated understanding, not
keywords.

For anything except **Correct**, identify the reasoning that needs attention and
ask the user to reconsider or expand it with hints or guiding questions. Do not
give a replacement answer and do not edit notes.

After the user demonstrates the required understanding, prepare polished Markdown
that preserves their meaning without adding substantial knowledge or copying TOP.
Show the exact proposed Markdown and stop. Edit `notes.md` only after explicit
approval of that wording. Protect completed notes unless correction was explicitly
requested. Then validate and propose one lesson-scoped knowledge-check commit,
using recent history for wording, under the root commit-approval contract.

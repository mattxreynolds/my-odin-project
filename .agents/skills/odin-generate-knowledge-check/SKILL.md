---
name: odin-generate-knowledge-check
description: Write original, lesson-specific knowledge-check questions for Matt to answer after an Odin lesson, using the current official lesson as the source and withholding answers.
---

# Generate a lesson knowledge check

Read the root and `courses/AGENTS.md`. Resolve the lesson from Matt's request,
the active section, and existing notes; ask for the lesson only if ambiguity
remains. Read the current official TOP lesson, including its overview, teaching
content, and assignment. Follow linked required readings when needed to cover a
stated lesson objective. If a source is unavailable, disclose the gap and ask for
the lesson content rather than guessing its coverage.

Write a short set of original questions that checks the lesson's main ideas and
asks Matt to apply or explain them. Match the lesson's level and scope; do not
turn an assignment or exercise into a solution request. Avoid copying old TOP
questions or lesson prose. Label the set **Personal Knowledge Check** so it is
not presented as official TOP material. Give the questions in conversation, with
the lesson link, and invite Matt to answer in his own words. Do not include an
answer key, model answers, or hints at this stage.

When Matt responds, use `odin-review-knowledge-check` for feedback and the
existing notes-approval workflow. Do not edit `notes.md` while generating
questions. Preserve existing questions and answers, especially in completed
sections.

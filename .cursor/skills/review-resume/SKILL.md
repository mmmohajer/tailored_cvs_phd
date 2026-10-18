---
name: review-resume
description: >-
  Score and fix an existing resume and cover letter against the quality bar and
  research: run check.py, truth pass against the master, score, fix, append to
  review.md. Use when the user says review, score, critique, or check my resume.
---

# Review

Read `rules/00_quality_bar.md` and `rules/05_review.md`.

1. Find the folder (`master/` or `custom_resumes/<slug>/`). Ask if unclear.
2. Render if PDFs are missing or older than the Markdown: `python renderer/scripts/render.py <folder>`.
3. `python renderer/scripts/check.py <folder> --max-pages <limit>`.
4. Truth pass against `master/` by hand (scope words, titles, dates).
5. Score each line; append a round to `<folder>/review.md`.
6. If the user asked for fixes too: fix the lowest line first, re-render, re-check, re-score (3 rounds max). Otherwise stop after scoring.

Report scores, the top 3 fixes (made or recommended), and anything only the person can answer.

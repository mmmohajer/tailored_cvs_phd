---
name: tailor-resume
description: >-
  Build a tailored resume and cover letter for one job description from the master,
  with a keyword list, requirement-to-evidence match report, PDFs, and a review.
  Use when the user says tailor, customize, apply to, resume for <company>, or adds
  a job description under jobs/.
---

# Tailor resume + cover letter

Read `rules/00_quality_bar.md`, `rules/03_tailor.md`, `rules/04_cover_letter.md`.

1. **Master present?** If not, stop and route to `build-master`.
2. **Folders:** `jobs/<slug>/` and `custom_resumes/<slug>/` (create with `python renderer/scripts/new_application.py "<Company>" "<Role>"`). Non-text posting → `python renderer/scripts/extract.py jobs/<slug>`.
3. **Analyze** the posting → top of `custom_resumes/<slug>/match_report.md`, and `keywords.txt`.
4. **Map** requirements to master evidence (strong / partial / gap) in `match_report.md`. Gaps stay gaps.
5. **Write** `resume.md` (selection from the master, posting's terms, level page limit).
6. **Write** `cover_letter.md` and add "Edits for you" to `match_report.md`.
7. **Render:** `python renderer/scripts/render.py custom_resumes/<slug>`
8. **Check:** `python renderer/scripts/check.py custom_resumes/<slug> --max-pages <limit from research/format/length.md>`
9. **Review:** `rules/05_review.md`, append to `custom_resumes/<slug>/review.md`, fix until 9+ or 3 rounds.

Stop. Report: fit summary (strong / partial / gap counts), the gaps, the edits the person should make in the letter, and both PDF paths.

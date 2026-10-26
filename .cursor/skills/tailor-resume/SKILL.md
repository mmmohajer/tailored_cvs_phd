---
name: tailor-resume
description: >-
  Build a custom CV, cover letter, email to one professor, and follow-up plan
  for one PhD position, with a match report, recommender notes, PDFs, and a
  review. Use when the user says tailor, apply to this position, cover letter,
  email a professor, follow up, or adds materials under positions/.
---

# Tailor one position

Read `rules/00_quality_bar.md`, `rules/03_tailor.md`, `rules/04_statement.md`.

1. **Master present?** If not, stop and route to `build-master`.
2. **Folders:** `positions/<slug>/` and `custom_resumes/<slug>/` (create with `python renderer/scripts/new_application.py "<University>" "<Position>"`). Non-text materials → `python renderer/scripts/extract.py positions/<slug>`.
3. **Name the country and route** (`research/countries/which_system.md`) and write that at the top of `custom_resumes/<slug>/match_report.md`, then the program analysis and `keywords.txt`.
4. **Map** requirements to master evidence (strong / partial / gap) in `match_report.md`. Gaps stay gaps.
5. **Write** `cv.md` as a custom CV: selection from the master for this position, not a copy of the master.
6. **Write** `cover_letter.md`, `professor_email.md`, `follow_up.md`, the country-default essay when the page is silent (or the essays the page names), `recommender_notes.md`, and "Edits for you" in `match_report.md`.
7. **Render:** `python renderer/scripts/render.py custom_resumes/<slug>`
8. **Check:** `python renderer/scripts/check.py custom_resumes/<slug> --max-pages <limit from the program, else 2>`
9. **Review:** `rules/05_review.md`, append to `custom_resumes/<slug>/review.md`, fix until 9+ or 3 rounds.

Stop. Report: fit summary (strong / partial / gap counts), the gaps, the professor the email is for, when the one follow-up would go out, the edits only the person can make, and the PDF paths. Do not send the email.

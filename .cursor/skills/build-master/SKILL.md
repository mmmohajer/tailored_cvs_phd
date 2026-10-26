---
name: build-master
description: >-
  Build or update the master academic CV from everything in profile/, using the
  PhD admissions research and rulesets, then render and check it. Use when the
  user says build my CV, build my master, update master, I added transcripts
  or papers, or answers open questions.
---

# Build or update the master CV

Read `rules/00_quality_bar.md`, `rules/01_intake.md`, `rules/02_master.md`.

1. **Intake:** `python renderer/scripts/extract.py profile`, then read `_extracted/_index.md` and every extracted file in full. Report empty or failed files.
2. **New vs update:** if `master/master_resume.md` exists, merge new facts into it; never drop existing true content without asking.
3. **Field and stage:** decide and record in `master/profile_facts.md`.
4. **Research:** read `research/countries/which_system.md` for each country the person is targeting, then `research/format/*`, `research/documents/*`, `research/fields/disciplinary_differences.md`, and matching `research/situations/*`.
5. **Write** `master_resume.md`, `stories.md`, `profile_facts.md`, `open_questions.md` per `rules/02_master.md`.
6. **Ask** the top questions (5 at most) in chat. Write answers into the master. Repeat while answers keep making the research record more specific.
7. **Render and check:**
   - `python renderer/scripts/render.py master/master_resume.md`
   - `python renderer/scripts/check.py master --max-pages 0`
8. **Review** with `rules/05_review.md` (Truth, Evidence, Field fit, Clarity; skip Relevance and Letter). Append to `master/review.md`.

Stop. Report: field and stage chosen, what's strong, open questions left, and the PDF path. Don't start tailoring.

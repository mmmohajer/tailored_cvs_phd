---
name: build-master
description: >-
  Build or update the master resume from everything in profile/, using the research
  and rulesets, then render and check it. Use when the user says build my master
  resume, update master, I added files to profile, or answers open questions.
---

# Build or update the master

Read `rules/00_quality_bar.md`, `rules/01_intake.md`, `rules/02_master.md`.

1. **Intake:** `python renderer/scripts/extract.py profile`, then read `_extracted/_index.md` and every extracted file in full. Report empty or failed files.
2. **New vs update:** if `master/master_resume.md` exists, merge new facts into it; never drop existing true content without asking.
3. **Level and situation:** decide and record in `master/profile_facts.md`.
4. **Research:** read `research/format/*`, `research/sections/*`, the matching `research/levels/*`, and matching `research/situations/*`.
5. **Write** `master_resume.md`, `stories.md`, `profile_facts.md`, `open_questions.md` per `rules/02_master.md`.
6. **Ask** the top questions (5 at most) in chat. Write answers into the master. Repeat while answers keep improving bullets.
7. **Render and check:**
   - `python renderer/scripts/render.py master/master_resume.md`
   - `python renderer/scripts/check.py master --max-pages 0`
8. **Review** with `rules/05_review.md` (Truth, Evidence, Level fit, Clarity; skip Relevance and Letter). Append to `master/review.md`.

Stop. Report: level chosen, what's strong, open questions left, and the PDF path. Don't start tailoring.

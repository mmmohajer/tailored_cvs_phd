---
name: resume-factory
description: >-
  Routes PhD application work: build or update the master academic CV, then for
  one position write a custom CV, cover letter, email to a professor, and
  follow-up plan. Use when the user says PhD, doctoral, cover letter, professor
  email, follow up, academic CV, faculty, admissions, or names a folder under
  positions/ or custom_resumes/.
---

# PhD applications (router)

The output of tailoring is a **custom CV, a cover letter, an email to one professor, and a follow-up plan**. The master CV file is `master/master_resume.md`. The custom CV is not a copy of it.

Pick exactly one skill and follow it:

| The user wants | Skill |
|---|---|
| Build the master CV, add new info, answer open questions | `.cursor/skills/build-master/SKILL.md` |
| A custom CV, cover letter, professor email, and follow-up plan for one position | `.cursor/skills/tailor-resume/SKILL.md` |
| Feedback or a score on an existing CV or statement | `.cursor/skills/review-resume/SKILL.md` |
| Just the PDFs from existing Markdown | `.cursor/skills/render-resume/SKILL.md` |

Resolve state first:

1. `master/master_resume.md` missing → build the master before any tailoring, and tell the user that's why.
2. Tailoring with a call pasted in chat → create the folders with `python renderer/scripts/new_application.py "<University>" "<Position>"` and save the text to `positions/<slug>/position.md` first.
3. Unclear which position → list folders in `positions/` and ask.

Ground rules: `rules/00_quality_bar.md`. Research lives in `research/` and is about doctoral admissions, not industry jobs.

---
name: resume-factory
description: >-
  Routes resume-factory work: build or update the master resume, tailor a resume
  and cover letter to a job description, review, or render PDFs. Use when the user
  says resume, CV, cover letter, master resume, tailor, customize, job description,
  apply to, render resume, or names a folder under jobs/ or custom_resumes/.
---

# Resume factory (router)

"Resume" means resume **and** cover letter.

Pick exactly one skill and follow it:

| The user wants | Skill |
|---|---|
| Build the master, add new info, answer open questions | `.cursor/skills/build-master/SKILL.md` |
| A resume + cover letter for a job (a posting in `jobs/`, pasted text, a company name) | `.cursor/skills/tailor-resume/SKILL.md` |
| Feedback or a score on an existing resume / letter | `.cursor/skills/review-resume/SKILL.md` |
| Just the PDFs from existing Markdown | `.cursor/skills/render-resume/SKILL.md` |

Resolve state first:

1. `master/master_resume.md` missing → build the master before any tailoring, and tell the user that's why.
2. Tailoring with a posting pasted in chat → create the folders with `python renderer/scripts/new_application.py "<Company>" "<Role>"` and save the text to `jobs/<slug>/job_description.md` first.
3. Unclear which job → list folders in `jobs/` and ask.

Ground rules: `rules/00_quality_bar.md`.

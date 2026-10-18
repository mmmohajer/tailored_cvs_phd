# Folder structure

```
.cursor/rules/resume-factory.mdc   always-on rule: resume = resume + cover letter, no invention
.cursor/skills/                    resume-factory (router), build-master, tailor-resume, review-resume, render-resume
research/                          evidence, graded A–D, cited by source ID
rules/                             these rulesets
renderer/
  templates/                       document.html, resume.md, cover_letter.md
  styles/                          classic.css, minimal.css, fonts/
  scripts/                         extract.py, render.py, check.py, new_application.py
profile/                 (private) the person's raw inputs, any format
  _extracted/            (private) plain text made by extract.py
master/                  (private) master_resume.md, stories.md, profile_facts.md, open_questions.md, review.md
jobs/<slug>/             (private) job_description.(txt|md|pdf|docx), _extracted/
custom_resumes/<slug>/   (private) resume.md/.html/.pdf, cover_letter.md/.html/.pdf,
                                   keywords.txt, match_report.md, review.md
examples/                          four fictional people, end to end
tests/                             tests for the scripts
```

`(private)` folders are gitignored except their `README.md`. Never commit real personal data.

Slug: lowercase, hyphens inside a part, underscore between company and role: `acme-corp`, `acme-corp_backend-engineer`. The same slug is used in `jobs/` and `custom_resumes/`.

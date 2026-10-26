# Folder structure

```
.cursor/rules/resume-factory.mdc   always-on rule: custom CV, cover letter, professor email, follow-up plan; no invention
.cursor/skills/                    router, build-master, tailor, review, render
research/                          PhD admissions evidence, graded A–D, cited by source ID
                                   countries/ is read before the US defaults
rules/                             these rulesets
renderer/
  templates/                       document.html, resume.md (CV), cover_letter.md, professor_email.md, follow_up.md
  styles/                          classic.css, minimal.css, fonts/
  scripts/                         extract.py, render.py, check.py, new_application.py
profile/                 (private) the person's raw inputs, any format
  _extracted/            (private) plain text made by extract.py
master/                  (private) master_resume.md (the full CV), stories.md, profile_facts.md,
                                   open_questions.md, review.md
positions/<slug>/       (private) the call: admissions page or vacancy, faculty list, prompts, _extracted/
custom_resumes/<slug>/   (private) cv.md, cover_letter.md, professor_email.md, follow_up.md,
                                   plus PDFs, recommender_notes.md, keywords.txt, match_report.md, review.md
examples/                          earlier job-application samples; not the PhD pattern
tests/                             tests for the scripts
```

`(private)` folders are gitignored except their `README.md`. Never commit real personal data.

Slug: lowercase, hyphens inside a part, underscore between university and position: `university-of-toronto`, `university-of-toronto_computer-science`. The same slug is used in `positions/` and `custom_resumes/`.

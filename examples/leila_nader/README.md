# Leila Nader

A fictional PhD applicant. Nothing here is a real person, university, or paper. Do not copy these facts into a real application.

This folder is the pattern for one position:

- `master/master_resume.md` is the full CV
- `custom_resumes/harbor-university_programming-languages/` holds the custom CV, cover letter, professor email, follow-up plan, and, because this fictional page is a silent US committee route, `statement.md`

Render it with:

```bash
python renderer/scripts/render.py examples/leila_nader/custom_resumes/harbor-university_programming-languages
python renderer/scripts/check.py examples/leila_nader/custom_resumes/harbor-university_programming-languages --master examples/leila_nader/master
```

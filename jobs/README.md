# jobs/

One folder per application: `jobs/<slug>/`, with the job description inside as `.txt`, `.md`, `.pdf`, or `.docx`. Gitignored except this README.

Create the folder (and its matching output folder) with:

```bash
python renderer/scripts/new_application.py "Acme Corp" "Backend Engineer"
# → jobs/acme-corp_backend-engineer/ and custom_resumes/acme-corp_backend-engineer/
```

Paste the whole posting, including the company's "about us" and any application instructions. The agent uses them for the cover letter.

# Resume Factory

A Cursor agent that writes strong, honest resumes and cover letters. You give it whatever you have about your career; it builds a **master resume**, then turns the master into a **tailored resume and cover letter** for each job you apply to, as styled PDFs.

Everything it decides is based on the evidence in `research/`, and it never invents a job, skill, date, or number you didn't give it.

> Throughout this repo, "resume" means **resume and cover letter**.

## How it works

```
profile/  ──►  master/  ──►  custom_resumes/<company>/
 (anything      (single         resume.pdf + cover_letter.pdf
  you have)      source of       + match report + review
                 truth)
                    ▲
               jobs/<company>/
               (job description)
```

1. **You add your information** to `profile/`, in any format.
2. **The agent builds your master resume**: every role, result, project, and skill, written to the research, plus questions for anything missing.
3. **You add a job description** to `jobs/<company>/`.
4. **The agent tailors** a resume and cover letter from the master to that job, shows which requirements you meet and which are gaps, renders PDFs, and reviews them.

## Setup (once)

Requires Python 3.10+ and [Cursor](https://cursor.com).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

WeasyPrint (the PDF engine) needs Pango. On macOS: `brew install pango`. On Ubuntu/Debian: `sudo apt install libpango-1.0-0 libpangoft2-1.0-0`. Other systems: [WeasyPrint install guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).

Check it works by rendering the example:

```bash
python renderer/scripts/render.py examples/jordan_rivera/master/master_resume.md
```

## Step 1: add your information

Put anything about your career in `profile/`: old resumes (PDF, Word, text, Markdown), a LinkedIn PDF export, performance reviews, project notes, or a plain text file where you just write about yourself. One file or twenty, it reads all of them.

More detail is better: numbers, team sizes, tools, what changed because of your work. See `profile/README.md` for prompts that help.

## Step 2: build your master resume

In Cursor's agent chat:

> Build my master resume.

The agent reads everything, decides your level (internship, entry, intermediate, senior, staff) and situation (career switcher, gap, bootcamp), writes `master/master_resume.md`, and asks you questions about anything missing or vague. Answer them; better answers mean stronger bullets.

You get `master/master_resume.pdf`, plus `stories.md` (longer stories for cover letters and interviews) and `open_questions.md`.

Read the master carefully. It's the source for everything after, so fix anything that isn't exactly right.

## Step 3: add a job description

Either paste the posting in chat:

> Tailor my resume for this job: <paste>

or create the folders and drop the file in:

```bash
python renderer/scripts/new_application.py "Acme Corp" "Backend Engineer"
# then save the posting as jobs/acme-corp_backend-engineer/job_description.txt (or .pdf / .docx / .md)
```

> Tailor my resume for acme-corp_backend-engineer.

## Step 4: get your tailored resume and cover letter

`custom_resumes/<company>/` will contain:

| File | What it is |
|---|---|
| `resume.pdf` | Tailored resume (from `resume.md`) |
| `cover_letter.pdf` | Tailored cover letter (from `cover_letter.md`) |
| `match_report.md` | Each job requirement → your evidence, or "gap"; plus edits only you can make to the letter |
| `keywords.txt` | The posting's key terms, used to check coverage |
| `review.md` | Scores and fixes from the review pass |

**Make the "Edits for you" changes in the cover letter.** Research shows AI-polished letters lose their value when they read as generic, and time spent personalizing the draft is linked to getting hired (`research/cover_letter/ai_and_signal.md`).

## Other things you can ask

- "Review my resume for acme-corp_backend-engineer."
- "I got a promotion / finished a project, update my master." (add notes to `profile/` first or just tell it)
- "Render it with the minimal style."

## Commands the agent uses (you can too)

```bash
python renderer/scripts/extract.py profile                       # any format → text
python renderer/scripts/render.py custom_resumes/<slug>          # Markdown → HTML + PDF
python renderer/scripts/check.py custom_resumes/<slug> --max-pages 1
python renderer/scripts/new_application.py "Company" "Role"
pytest                                                           # script tests
```

## What's in the repo

| Path | Purpose |
|---|---|
| `research/` | Evidence on resumes and cover letters by level and situation, graded A–D with sources |
| `rules/` | Step-by-step rulesets the agent follows |
| `.cursor/skills/`, `.cursor/rules/` | How Cursor's agent picks up the workflow |
| `renderer/` | Markdown templates, CSS styles, and the Python scripts |
| `profile/`, `master/`, `jobs/`, `custom_resumes/` | Your data (gitignored) |
| `examples/` | Four fictional people (new grad, career switcher, intermediate, staff) taken through the whole flow |

## Privacy

Your folders (`profile/`, `master/`, `jobs/`, `custom_resumes/`) are in `.gitignore`. If you fork this repo publicly, your data stays local. Double-check before you ever force-add those paths.

## Honesty

The agent will not add skills you don't have, change titles or dates, or make up metrics, even to match a posting. Gaps are reported to you in `match_report.md` so you can decide whether to apply, learn the skill, or address it in the letter.

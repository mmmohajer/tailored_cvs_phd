# PhD Application Studio

A Cursor agent that prepares honest PhD applications. You give it whatever you have about your study and research; it builds a **master academic CV**, then for each position writes a **custom CV, a cover letter, an email to one professor, and a follow-up plan**.

Everything it decides is based on the evidence in `research/`, and it never invents a degree, grade, lab, paper, advisor, or number you didn't give it.

> The master file is still named `master_resume.md` so the renderer can find it. It is an academic CV, not an industry resume.

## How it works

```
profile/  ──►  master/  ──►  custom_resumes/<position>/
 (transcripts,   (full CV,       custom CV + cover letter
  papers, notes)  source of       + professor email + follow-up plan
                  truth)
                    ▲
               positions/<university_position>/
               (the call, faculty, prompts)
```

1. **You add your information** to `profile/`, in any format.
2. **The agent builds your master CV**: every degree, project, paper, and method, written to the research, plus questions for anything missing.
3. **You add a position** to `positions/<university_position>/`: the admissions page or vacancy, faculty you are considering, and the essay prompts.
4. **The agent writes four files for that position:** a custom CV, a cover letter, an email to one professor, and a follow-up plan. The same text is not reused with the university's name swapped. It shows which requirements you meet and which are gaps, notes who can write letters, renders PDFs, and reviews them. It does not send the email.

## Setup (once)

Requires Python 3.10+ and [Cursor](https://cursor.com). There are no API keys: the agent runs inside Cursor, and the scripts run on your machine.

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

WeasyPrint (the PDF engine) needs Pango. On macOS: `brew install pango`. On Ubuntu/Debian: `sudo apt install libpango-1.0-0 libpangoft2-1.0-0`.

**Windows**

1. Install [MSYS2](https://www.msys2.org/) with the default options. In the **MSYS2 UCRT64** shell run `pacman -S mingw-w64-ucrt-x86_64-pango`, then close it.
2. In Command Prompt, from this folder:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

If you see `cannot load library`, run `set WEASYPRINT_DLL_DIRECTORIES=C:\msys64\ucrt64\bin` and try again. Old `.doc`, `.rtf`, `.odt`, and `.pages` files are read with macOS `textutil`; on Windows, save them as `.docx` or PDF first. WSL works too: follow the Linux steps.

Other systems: [WeasyPrint install guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).

Check that rendering works (this sample is an older job CV, used only to test the script):

```bash
python renderer/scripts/render.py examples/jordan_rivera/master/master_resume.md
```

## Step 1: add your information

Put anything about your study and research in `profile/`: transcripts, old CVs, theses, papers, posters, a previous statement, or a plain text file where you describe your projects. One file or twenty, it reads all of them.

More detail is better: the question, your role, the method, the advisor, and what came of it. See `profile/README.md` for prompts that help.

## Step 2: build your master CV

In Cursor's agent chat:

> Build my master CV.

The agent reads everything, decides your field and stage (undergraduate, master's, or returning from work), writes `master/master_resume.md`, and asks you questions about anything missing or vague. Answer them; better answers mean a more specific statement later.

You get `master/master_resume.pdf`, plus `stories.md` (longer accounts of projects) and `open_questions.md`.

Read the master carefully. It's the source for everything after, so fix anything that isn't exactly right.

## Step 3: add a position

Either paste the admissions page or vacancy in chat:

> Tailor my application for this position: <paste>

or create the folders and drop the files in:

```bash
python renderer/scripts/new_application.py "University of Toronto" "Computer Science"
# then save the page as positions/university-of-toronto_computer-science/position.md (or .pdf / .docx / .txt)
```

> Tailor my application for university-of-toronto_computer-science.

## Step 4: get the four documents

`custom_resumes/<position>/` will contain:

| File | What it is |
|---|---|
| `cv.pdf` | Custom CV for this position, not a copy of the master |
| `cover_letter.pdf` | Cover letter for this position |
| `professor_email.md` | Email to one professor. You send it. The agent does not |
| `follow_up.md` | One reminder if they do not reply, then stop |
| `match_report.md` | Each requirement → your evidence, or "gap"; plus edits only you can make |
| `recommender_notes.md` | Who can write recommendation letters. The agent does not write those letters |
| `review.md` | Scores and fixes from the review pass |

**Make the "Edits for you" changes before you send anything**, especially the sentence about which of the professor's papers you have actually read.

A research proposal or other essay is added only when that position asks for it.

## Other things you can ask

- "Review my statement for university-of-toronto_computer-science."
- "I finished a thesis / a paper was accepted, update my master." (add the file to `profile/` first or just tell it)
- "Render it with the minimal style."

## Commands the agent uses (you can too)

```bash
python renderer/scripts/extract.py profile                       # any format → text
python renderer/scripts/render.py custom_resumes/<slug>          # Markdown → HTML + PDF
python renderer/scripts/check.py custom_resumes/<slug> --max-pages 2
python renderer/scripts/new_application.py "University" "Program"
pytest                                                           # script tests
```

## What's in the repo

| Path | Purpose |
|---|---|
| `research/` | Evidence on PhD admissions, graded A–D with sources |
| `rules/` | Step-by-step rulesets the agent follows |
| `.cursor/skills/`, `.cursor/rules/` | How Cursor's agent picks up the workflow |
| `renderer/` | Markdown templates, CSS styles, and the Python scripts |
| `profile/`, `master/`, `positions/`, `custom_resumes/` | Your data (gitignored) |
| `examples/` | An earlier job-application walkthrough. It is not the pattern for PhD applications |

## Privacy

Your folders (`profile/`, `master/`, `positions/`, `custom_resumes/`) are in `.gitignore`. If you fork this repo publicly, your data stays local. Double-check before you ever force-add those paths.

## Honesty

The agent will not add a method you have not used, change a grade, advisor, date, or author order, or invent a paper or a faculty match. Gaps are reported in `match_report.md` so you can decide whether to apply, take a course, or address the gap in the cover letter. The agent drafts the professor email and does not send it.

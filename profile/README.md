# profile/

Put everything about your study and research here. This folder is gitignored (except this README).

A description written from the files already in this folder is in `about_me.md`. That file is private and is not committed.

**Accepted:** `.pdf`, `.docx`, `.txt`, `.md`, `.html`, and on macOS also `.doc`, `.rtf`, `.pages`. Scanned PDFs (photos of paper) can't be read; save a text version instead. That includes scanned transcripts.

**One file or many.** Subfolders are fine. The agent reads all of it.

## What helps most

- Transcripts, with the grading scale visible
- Old CVs and any previous statement of purpose
- Theses, papers, posters, abstracts, and the author order on each
- A short note per research experience: advisor, lab or group, dates, the question, what you did, what came of it
- Syllabi or course lists for methods sequences the programs will care about
- Test scores you already have (GRE, TOEFL, IELTS), only if you want them considered
- A plain `about_me.txt` written however you like

## Prompts if you're writing from scratch

For each degree:

- Degree, field, university, city and country, start and end month/year
- GPA exactly as printed, and the scale
- Thesis title and advisor, if any

For each research experience:

- Your role, the group, the advisor, the city, the dates
- The question the project was asking
- What you did yourself, as opposed to the team
- What came of it: a number, a poster, a draft, a technique you can now run
- Papers or posters: full author list, venue, year, and status (published, in press, under review, draft)

Also: jobs, teaching, languages, awards, and which programs or faculty you are considering.

Estimates are fine. Say so ("about 8 months") and the agent will keep them labeled as estimates.

Run `python renderer/scripts/extract.py profile` to see what the agent will read.

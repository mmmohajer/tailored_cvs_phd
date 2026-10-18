# profile/

Put everything about your career here. This folder is gitignored (except this README).

**Accepted:** `.pdf`, `.docx`, `.txt`, `.md`, `.html`, and on macOS also `.doc`, `.rtf`, `.pages`. Scanned PDFs (photos of paper) can't be read; save a text version instead.

**One file or many.** Subfolders are fine. The agent reads all of it.

## What helps most

- Old resumes and CVs, any age
- LinkedIn profile exported as PDF (Profile → More → Save to PDF)
- Performance reviews, promotion documents, a "brag document"
- Project notes, READMEs, links to GitHub, portfolio, talks, papers
- A plain `about_me.txt` written however you like

## Prompts if you're writing from scratch

For each job:

- Title, company, city (or remote), start and end month/year
- What the team or product did, and how big it was (users, revenue, team size)
- 3–5 things you built, fixed, or improved. For each: what was wrong before, what you did, and what changed after, with numbers if you have them (time saved, latency, cost, errors, users, revenue)
- What you led, what you shared with others, who you mentored
- Tools and languages you actually used there

Also: education (degree, school, year, GPA if recent), courses and certifications, projects outside work, awards, and what kind of role you want next.

Estimates are fine. Say so ("about 30%") and the agent will keep them labeled as estimates.

Run `python renderer/scripts/extract.py profile` to see what the agent will read.

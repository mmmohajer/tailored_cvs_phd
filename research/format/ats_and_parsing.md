# ATS and parsing

An Applicant Tracking System (ATS) stores applications, parses resumes into fields, and lets recruiters search, filter, and rank. The popular claim that "75% of resumes are rejected by robots" has no study behind it.

## Findings

- **ATSs are nearly universal at large employers.** 97.4% of Fortune 500 companies had a detectable ATS in 2026; Workday alone is used by more than 40%. [S08, C]
- **Automatic rejection on content or formatting is rare.** 23 of 25 recruiters (92%) said their ATS does not auto-reject for formatting, content, or design. 2 of 25 had content rules switched on (a match-score threshold, a required-skills count). Knockout questions (work authorization, license, location) were used by all of them. [S04, C, small sample]
- **Filtering and ranking on exact criteria is common, and it costs qualified people.** Over 90% of employers use their systems to filter or rank candidates. 88% agreed qualified high-skill candidates are screened out because they do not match the *exact criteria* in the job description (94% for middle-skill). [S05, B]
- **Gaps are a common filter.** Almost half of surveyed companies screened out resumes with a gap of more than six months. [S05, B]
- **Columns are less risky than they used to be, but not risk free.** At least 15% of CVs use columns. One major parser raised well-rendered column CVs from 62% to 90% after a rebuild, so about 1 in 10 still came out badly. Text inside images, tables that scramble reading order, and contact details in page headers/footers break parsing. [S09, C; S04, C]
- **Keyword stuffing backfires with humans.** The worst-performing resumes showed keyword stuffing; keywords should appear in context because a person reads the result. [S01, C]

## What the agent does

- Single column, real text, no tables for layout, no images, no text boxes. Contact details in the body, not the PDF header/footer. `check.py` verifies the name and email are readable in the PDF text.
- Use the job description's **exact wording** for skills and titles you truly have ("PostgreSQL", not only "Postgres"; "Django REST Framework", not only "DRF"). Spell out an acronym once with the full term. This answers S05's exact-criteria filtering.
- Put each keyword inside a bullet that proves it, not in a hidden or stuffed list (S01).
- Standard section names: Summary, Skills, Experience, Projects, Education. Parsers and humans both look for them.
- Never add a skill, title, or certification the person does not have to pass a filter. A missing requirement goes in `match_report.md` as a gap.
- Answer knockout questions honestly; they are outside the resume, but mention work authorization in the master if it is a common question for the person.

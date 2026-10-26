# Tailor one PhD position

Input: `positions/<slug>/` with the call, faculty list, and any prompts. Output: `custom_resumes/<slug>/`.

Slug: `university` or `university_program`, created by `python renderer/scripts/new_application.py "University" "Program"`.

## Steps

1. **Check the master exists and is current.** If `master/master_resume.md` is missing, stop and run the master build first.
2. **Read the position.** Run `python renderer/scripts/extract.py positions/<slug>` when it isn't plain text. Read it fully, including faculty names, required documents, word limits, test policy, and whether a supervisor must already have agreed.
3. **Name the country and the route** using `research/countries/which_system.md`. Read that country's file. Write at the top of `match_report.md`:
   - Country, route (committee, supervisor-first, or advertised post), and which country file was used.
   - University, department, degree, deadline if stated, funding note if stated, required documents, page or word limits, test policy.
   - The 3 things the instructions stress (methods, a subfield, a population, teaching, a language).
   - If the country has no file, say which closest pattern was used and that it is unverified (`research/countries/unlisted.md`).
4. **Write `keywords.txt`:** one term per line, the program's own words for methods, topics, and requirements (10–25 lines). These are a coverage check, not a stuffing list. Use the program's spelling.
5. **Map requirements to evidence** in `match_report.md`: requirement → evidence in the master (quote the entry) → `strong`, `partial`, or `gap`.
6. **Gaps are reported, not filled.** For each gap, say whether something adjacent and true can be shown or whether it stays a gap. If a required method, language, or degree is missing, say whether applying still makes sense.
7. **Choose field rules** from the program, then from the country file, then from `research/fields/disciplinary_differences.md`.
8. **Write the custom CV as `cv.md`.** It is a selection from the master for this position, not a copy of `master_resume.md`.
   - Same format as `renderer/templates/resume.md`.
   - Headline: the person's research area, aligned with this position's words only when the work actually matches.
   - Same institutions, titles, advisors, dates, and author orders as the master.
   - Page one proves the position's main requirements. Drop projects, courses, and jobs that do not.
   - Research interests are chosen for this position. Use an interest from the master when the opening is about it. Otherwise use machine learning or other work actually in the master. Do not add a method that is only an interest.
   - Light rewording may use the position's terms. Meaning, numbers, and scope stay identical.
   - Cut to the length in `research/format/length.md` and `research/format/cv_structure.md`, or the position's shorter limit. The usual target is two pages. Keep research experience, publications, and a Languages section when the master has them. Education first. The matching research and any papers start on page one. Reverse chronological inside a section. Awards from the master stay. References are the people who agreed. A bando that requires Europass is noted in the match report; the person exports that file.
9. **Write `cover_letter.md`, `professor_email.md`, and `follow_up.md`** with `04_statement.md`. Also write the country-default essay in `research/statement/which_essay.md` when the page is silent. When the page names its essays, write those instead of the country default.
10. **Write `recommender_notes.md`** with `research/documents/recommendations.md`.
11. **Render, check, review:** `06_render.md`, then `05_review.md`.

## Never

- Never add a method, course, or paper to match a keyword the person does not have.
- Never change a degree, advisor, date, GPA, or author order to look closer to the program.
- Never copy sentences from the position page into the CV, the cover letter, or the email.
- Never name a faculty member whose work is not in the materials, and never claim they have agreed to supervise.
- Never edit the master during tailoring. New facts go to the master first (with the person's confirmation), then into the CV.

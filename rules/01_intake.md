# Intake: read everything in `profile/`

## Goal

Every fact the person supplied, from every file, available as plain text, with nothing silently skipped.

## Steps

1. Run `python renderer/scripts/extract.py profile`.
2. Read `profile/_extracted/_index.md`. For each row:
   - `ok`: read the extracted text in full.
   - `EMPTY`: a scanned or image-only file. Tell the person and ask for a text version or a typed summary. This matters for transcripts.
   - `FAILED`: tell the person which file and the error; suggest saving as `.docx` or `.pdf`.
3. Read every extracted file completely. Inputs can be one file or many: old CVs, transcripts, theses, papers, posters, syllabi, a LinkedIn export, research statements from a previous cycle, a plain "about my research" note. All count.
4. Build a working list of facts by type: degrees (school, country, dates, GPA and scale, thesis title), research roles (group, advisor, location, dates, the person's role), papers and posters (authors, venue, year, status), methods, languages, test scores, jobs, awards, and target programs if they named any.
5. **Resolve conflicts, don't pick silently.** When two sources disagree (a GPA, a graduation date, author order), record both in `master/open_questions.md` and ask which is right.
6. Note the source file for any fact that might be questioned later (the master keeps a short source note in an HTML comment where useful).

## Never

- Never skip a file because another file "seems newer."
- Never guess grades, author order, test scores, or dates from context.
- Never convert a grading scale without a document that already did the conversion.
- Never read files outside `profile/` for personal facts (except the person's answers in chat, which are written into the master).

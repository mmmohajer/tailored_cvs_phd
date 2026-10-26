# Review

Runs after every render. Writes to `review.md` in the same folder (`master/review.md` or `custom_resumes/<slug>/review.md`). **Append-only:** each round adds a dated section; never rewrite an earlier round.

## Steps

1. **Mechanical:** run `python renderer/scripts/check.py <folder> --max-pages <limit>`. Any FAIL is fixed before scoring. Use `0` for the master. Use the position's page cap for the custom CV and cover letter; if the position is silent, use `2`.
2. **Truth pass:** read `cv.md` (or `master_resume.md`), `cover_letter.md`, and `professor_email.md` against the master. Check author order, paper status, advisor names, grades, and dates by hand. The follow-up plan must not add a reply, a meeting, or a fact that is not already in those files. `check.py` only catches numbers and the organization named in each experience entry.
3. **Score** with the table in `00_quality_bar.md`. Write each score and one sentence of why.
4. **Fix** the lowest line first, re-render, re-check, re-score. Stop at 9+ on every line, or after 3 rounds, then tell the person what's left.
5. **Look at the PDF**, not only the Markdown: awkward page breaks, a heading alone at the bottom of a page, an entry split across pages, a cover letter that runs past one page.

## Review section template

```
## Round N — YYYY-MM-DD

check.py: PASS | FAIL (what)

| Line | Score | Why |
|---|---|---|
| Truth | | |
| Relevance | | |
| Evidence | | |
| Field fit | | |
| Clarity | | |
| Letter | | |

Fixes made:
- ...

Left for the person:
- ...
```

## Banned phrases (CV, cover letter, and email)

Rewrite any of these into a specific fact or delete it:

- responsible for, duties included, helped with (with no task), worked on, utilized, leveraged (as filler)
- passionate about, ever since I was a child, this has been my dream, I have always been fascinated
- I believe I would be a great fit, I am confident that I would contribute, world-class, cutting-edge, renowned faculty
- results-driven, detail-oriented, team player, synergy
- To whom it may concern, References available upon request

## Common fails

- Page one of the CV is coursework or an unrelated job, with the research on page two.
- A method listed in skills with no project or course showing it.
- A paper with the wrong author position, or a draft labeled as published.
- A custom CV that still contains a project this position does not need.
- A cover letter or professor email that could be sent to any department, or that renames faculty from a different application.
- A follow-up plan with more than one reminder, or a claim that the professor has already replied.
- A US statement of purpose sent to a country that asked for a research proposal or a short motivation letter.
- A grade converted onto another country's scale, or a photo and personal details the instructions never requested.
- Faculty named whose papers the person has not read and has not been asked about.
- A second essay the program never requested.

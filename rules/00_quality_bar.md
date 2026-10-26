# Quality bar

Applies to every step. For each position the output is a **custom CV, a cover letter, an email to one professor, and a follow-up plan**. When the page is silent, also write the country-default essay in `research/statement/which_essay.md`. When the page names its essays, write those instead. The master file is still named `master_resume.md`. The custom CV is `custom_resumes/<slug>/cv.md`, and it is not a copy of the master.

## Non-negotiables (any one fails the output)

1. **No invention.** Every institution, degree, grade, lab, advisor, title, date, method, paper, authorship, and number exists in `master/`. The master itself only contains what came from `profile/` or the person's answers. When something is missing, ask in `master/open_questions.md`. Never fill the gap with a plausible paper, GPA, or faculty name.
2. **No inflation.** "Assisted" never becomes "led." A middle-author paper is not written as first author. A draft is not "under review." Estimates stay labeled as estimates ("about 8 months") the way the person gave them.
3. **Error-free.** Spelling of names, paper titles, and programs; grammar; tense; dates. The cover letter and the professor email are read as writing, not only as a list of facts.
4. **Parseable.** One column, real text, standard section names, contact details in the body. `check.py` passes.
5. **Within length.** The program's limit first. If it is silent, the country file in `research/countries/`, then `research/format/length.md`.
6. **Tailored to this position.** The custom CV, cover letter, professor email, and follow-up plan are written for one opening. A file for another university is not reused with the names swapped.
7. **Private.** Personal data stays in gitignored folders. Never copy real personal data into `examples/`, commits, or chat summaries beyond what the task needs.
8. **Only the essays the page or the country default calls for.** A silent page still gets that country's statement, proposal, or motivation letter. Do not add a diversity statement, a teaching statement, or a second proposal on top of that. Do not state a race, ethnicity, disability, or family status the person did not give you. [S12, D]

## Scoring (review step)

Score 1–10 on each; **9+ on every line to pass**:

| Line | 9–10 looks like |
|---|---|
| Truth | Every claim traces to the master; `check.py` fact trace is clean; authorship and paper status are exact |
| Relevance | Education and the strongest research on page one match what this program says it wants |
| Evidence | Research entries name the question, the person's role, and a concrete outcome |
| Field fit | Country route, document genre, order, and methods match `research/countries/` and then the field file |
| Clarity | A faculty reader can see the degree, the research, and any paper titles without hunting |
| Letter | The cover letter is specific to this opening; the professor email cites one real overlap and does not ask for a place that was not offered; the follow-up plan is one reminder and then a stop |

Fix the lowest line first. Re-score after every change. A CV that reads as one research direction beats a CV with perfect bullets pointing at five unrelated fields.

## Where decisions come from

- **Research grade A/B:** hard rules.
- **Grade C/D:** defaults. Departing from one is allowed when the program or the person asks; say why in `match_report.md`.
- **The program's instructions win** over defaults.
- **The person's explicit wishes win** over defaults, except for the non-negotiables above.

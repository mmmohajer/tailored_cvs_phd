# Quality bar

Applies to every step. "Resume" always means **resume and cover letter**.

## Non-negotiables (any one fails the output)

1. **No invention.** Every employer, title, date, degree, skill, tool, number, and scope word ("led," "owned") exists in `master/`. The master itself only contains what came from `profile/` or the person's answers. When something is missing, ask in `master/open_questions.md`; never fill the gap with a plausible guess.
2. **No inflation.** "Contributed" never becomes "led." A team result is not written as a solo result. Estimates stay labeled as estimates ("~30%") the way the person gave them.
3. **Error-free.** Spelling, grammar, tense, dates, and punctuation are consistent. ([S10, A] in `research/format/layout_and_writing.md`.)
4. **Parseable.** One column, real text, standard section names, contact details in the body. `check.py` passes.
5. **Within length.** Page limits from `research/format/length.md` for the person's level.
6. **Tailored.** Each tailored resume and letter is built for one posting; nothing generic ships.
7. **Private.** Personal data stays in gitignored folders. Never copy real personal data into `examples/`, commits, or chat summaries beyond what the task needs.

## Scoring (review step)

Score 1–10 on each; **9+ on every line to pass**:

| Line | 9–10 looks like |
|---|---|
| Truth | Every claim traces to the master; `check.py` fact trace is clean |
| Relevance | Every bullet on page one proves something the posting asks for |
| Evidence | Most bullets carry a result (number or concrete outcome) and the how |
| Level fit | Length, order, and scope language match the level file in `research/levels/` |
| Clarity | Skimmable in 7 seconds: titles, companies, dates, and the top results stand out |
| Letter | Specific reason for this company, one real story, honest gap handling, no boilerplate |

Fix the lowest line first. Re-score after every change. Cohesion of the whole document beats any single line: a resume that reads as one clear story wins over one with perfect bullets that point in five directions.

## Where decisions come from

- **Research grade A/B:** hard rules.
- **Grade C/D:** defaults. Departing from one is allowed when the posting or the person asks; say why in `match_report.md`.
- **The person's explicit wishes win** over defaults, except for the non-negotiables above.

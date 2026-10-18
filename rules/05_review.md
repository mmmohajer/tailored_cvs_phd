# Review

Runs after every render. Writes to `review.md` in the same folder (`master/review.md` or `custom_resumes/<slug>/review.md`). **Append-only:** each round adds a dated section; never rewrite an earlier round.

## Steps

1. **Mechanical:** run `python renderer/scripts/check.py <folder> --max-pages <limit>`. Any FAIL is fixed before scoring.
2. **Truth pass:** read every line of `resume.md` and `cover_letter.md` against the master. Check scope words, titles, dates, and numbers by hand too (`check.py` only catches numbers and employers).
3. **Score** with the table in `00_quality_bar.md`. Write each score and one sentence of why.
4. **Fix** the lowest line first, re-render, re-check, re-score. Stop at 9+ on every line, or after 3 rounds, then tell the person what's left.
5. **Look at the PDF**, not only the Markdown: awkward page breaks, a lone line on page two, an entry split across pages, overflowing contact line.

## Review section template

```
## Round N — YYYY-MM-DD

check.py: PASS | FAIL (what)

| Line | Score | Why |
|---|---|---|
| Truth | | |
| Relevance | | |
| Evidence | | |
| Level fit | | |
| Clarity | | |
| Letter | | |

Fixes made:
- ...

Left for the person:
- ...
```

## Banned phrases (resume and letter)

Rewrite any of these into a specific fact or delete it:

- responsible for, duties included, helped with, worked on, utilized, leveraged (as filler)
- results-driven, detail-oriented, team player, self-starter, go-getter, hard-working, dynamic, synergy
- passionate about, excited to apply, I am confident that, I believe I would be a great fit
- fast-paced environment, wear many hats, think outside the box
- proven track record (unless followed by the record), extensive experience (say how much)
- To whom it may concern, References available upon request

## Common fails

- A bullet on page one that proves nothing the posting asks for.
- Skills listed with no bullet or project showing them.
- Mixed date formats ("Jan 2022" and "01/2023").
- Summary that could belong to anyone.
- Letter paragraph that repeats a resume bullet word for word.
- Second page with only a few lines on it: cut to one page or add real, relevant content from the master.

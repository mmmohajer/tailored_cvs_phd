# Master CV

The master is the single source of truth. The custom CV, cover letter, and professor email are a **selection** from it, never an addition to it.

The file is named `master_resume.md` so `render.py` and `check.py` find it. It is an academic CV.

## Files in `master/`

| File | Holds |
|---|---|
| `master_resume.md` | Everything: every degree, research role, paper, presentation, job, and method. Same Markdown format as `renderer/templates/resume.md`, so it renders. No length limit. |
| `stories.md` | 3–8 longer accounts for the statement: the question, what the person did, what resulted, which skills it proves. |
| `profile_facts.md` | Field, degree stage (undergraduate, master's, returning from work), target countries and programs, GPA scale, test scores they chose to share, languages, preferences. |
| `open_questions.md` | What the agent needs from the person. Each question says why it matters. Numbers here are **not** facts (`check.py` ignores this file). |

## Steps

1. Run intake (`01_intake.md`).
2. **Decide the field and stage** from the person's history. Record situation flags: returning from industry, international credentials, weak grades, no publications, a gap, a field switch. Record them in `profile_facts.md`.
3. **Read the research** that applies: `research/format/*`, `research/documents/*`, `research/fields/disciplinary_differences.md`, and any matching `research/situations/*` file.
4. **Write `master_resume.md`:**
   - Header: name, a headline with the research area (not a job title), contact line.
   - Education, research, publications, and the other sections in `research/documents/academic_cv.md`.
   - Keep every true entry. Tailored CVs choose among them.
5. **Write `stories.md`** from the strongest research, one story per project worth telling in a statement.
6. **Write `open_questions.md`** for everything missing or weak, most valuable first. Typical questions:
   - "Your notes say you worked in the Rivera lab. What was the question, and what did you do yourself?"
   - "The transcript shows 3.42/4.00 and your draft CV shows 3.5. Which should the file use?"
   - "Is the 2024 poster first author, and was it peer reviewed or a lab meeting?"
   - "You have no publication listed. Is there a thesis or a draft you want described, and what is its real status?"
7. **Ask the person** the top questions in chat (5 at most at a time). Write every answer into the master. Repeat until the open questions that block a specific statement are answered or the person declines.
8. **Render and check:** `python renderer/scripts/render.py master/master_resume.md` and `python renderer/scripts/check.py master --max-pages 0`.
9. **Review** with `05_review.md` (truth, evidence, field fit, clarity). The master is not scored for relevance to one program; it has no program yet.

## Rules

- Bullets in the master are already specific and true. Tailoring only selects, reorders, trims, and rewords lightly.
- A number appears in the master exactly as the person gave it.
- Authorship and paper status are decided here, with the person, once.
- Updating later: add new projects, papers, and grades to the master first, then re-tailor.

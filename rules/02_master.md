# Master resume

The master is the single source of truth. Every tailored resume and cover letter is a **selection** from it, never an addition to it.

## Files in `master/`

| File | Holds |
|---|---|
| `master_resume.md` | Everything: every role, every strong bullet (more than any one resume needs), all projects, education, skills. Same Markdown format as `renderer/templates/resume.md`, so it renders. No length limit. |
| `stories.md` | 3–8 longer stories for cover letters and interviews: Situation, what the person did, Result with numbers, skills it proves. |
| `profile_facts.md` | Level, years of experience, target roles, location and remote preference, work authorization (only if shared), links, preferences (e.g. keep graduation year, preferred name). |
| `open_questions.md` | What the agent needs from the person. Each question says why it matters. Numbers here are **not** facts (`check.py` ignores this file). |

## Steps

1. Run intake (`01_intake.md`).
2. **Decide the level** with the person's history: internship, entry/new grad, intermediate, senior, staff. Add situation flags: career switcher, bootcamp/self-taught, employment gap. Record in `profile_facts.md`.
3. **Read the research** that applies: `research/format/*`, `research/sections/*`, the matching `research/levels/*` file, and any matching `research/situations/*` file.
4. **Write `master_resume.md`:**
   - Header: name, a headline for the person's main target, contact line.
   - Summary: one version for the main target.
   - Skills: everything real, grouped (`research/sections/skills.md`), each traceable to a bullet or project.
   - Experience: every role in reverse chronological order. Rewrite each duty as a result using `research/sections/experience_bullets.md`. Keep every true variant worth having; tailored resumes choose among them.
   - Projects, Education, and other sections per `research/sections/*`.
   - Use the section order for the person's level from `research/sections/order.md`.
5. **Write `stories.md`** from the strongest achievements.
6. **Write `open_questions.md`** for everything missing or weak, most valuable first. Typical questions:
   - "Your notes say you 'improved performance' on the billing service. Do you know by how much, or before/after numbers?"
   - "Two sources list different end dates for Acme (Mar 2023 vs May 2023). Which is right?"
   - "Was the migration your project, or were you one of several engineers on it?"
   - "There's a gap from Jun 2021 to Feb 2022. Do you want to label it? Anything you did during it (courses, freelance, caregiving) is your choice to share."
7. **Ask the person** the top questions in chat (5 at most at a time). Write every answer into the master. Repeat until the open questions that block strong bullets are answered or the person declines.
8. **Render and check:** `python renderer/scripts/render.py master/master_resume.md` and `python renderer/scripts/check.py master --max-pages 0`.
9. **Review** with `05_review.md` (truth, clarity, level fit). The master isn't scored for relevance; it has no job yet.

## Rules

- Bullets in the master are already polished and true; tailoring only selects, reorders, trims, and rewords lightly.
- A number appears in the master exactly as the person gave it, with "~" if it is an estimate.
- Scope words are decided here, with the person, once.
- Updating later: add new roles, results, and projects to the master first, then re-tailor.

# Tailor a resume to one job

Input: `jobs/<slug>/` with a job description. Output: `custom_resumes/<slug>/`.

Slug: `company` or `company_role`, created by `python renderer/scripts/new_application.py "Company" "Role"`.

## Steps

1. **Check the master exists and is current.** If `master/master_resume.md` is missing, stop and run the master build first.
2. **Read the job description.** Run `python renderer/scripts/extract.py jobs/<slug>` when it isn't plain text. Read it fully.
3. **Analyze the posting** and write the top of `match_report.md`:
   - Role title, level the posting implies, location / remote, must-haves, nice-to-haves, responsibilities, domain, any explicit application instructions (cover letter yes/no, page limit, portfolio).
   - The 3 requirements that matter most, in the order the posting stresses them.
4. **Write `keywords.txt`:** one per line, the posting's exact terms for skills, tools, and practices (10–25 lines). Use the posting's spelling.
5. **Map requirements to evidence** in `match_report.md`, as a table: requirement → evidence in the master (quote the bullet or project) → status: `strong`, `partial`, or `gap`.
6. **Gaps are reported, not filled.** For each gap, say whether something adjacent and true can be shown (a related tool, a course in progress) or whether it stays a gap. If many must-haves are gaps, say so plainly and suggest whether to apply.
7. **Choose the level rules:** use the posting's level when it differs from the person's (a senior person applying to a mid-level role gets mid-level length but keeps true scope).
8. **Write `resume.md`** from the master:
   - Same format as `renderer/templates/resume.md`.
   - Headline: the posting's title if the person's work matches it; otherwise the person's real target title.
   - Summary rewritten for this job (`research/sections/header_and_summary.md`).
   - Skills reordered: the posting's must-haves first, in its spelling.
   - Experience: same roles, titles, and dates as the master. Pick and reorder bullets so the 3 key requirements are proven on page one. Light rewording is allowed to use the posting's terms; meaning, numbers, and scope stay identical.
   - Projects: only those that prove a requirement.
   - Cut until it fits the page limit. Cut least-relevant bullets first, oldest roles' bullets second.
9. **Write the cover letter** with `04_cover_letter.md`, unless the posting says not to.
10. **Render, check, review:** `06_render.md`, then `05_review.md`.

## Never

- Never add a skill to match a keyword the person doesn't have.
- Never change a title, company, or date to look closer to the posting.
- Never copy sentences from the job description into bullets.
- Never edit the master during tailoring. New facts found during tailoring go to the master first (with the person's confirmation), then into the resume.

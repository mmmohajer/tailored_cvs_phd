# Examples

Four **fictional** people (names, companies, schools, and numbers are all invented), each taken through the whole flow. Together they cover every level band and situation the research describes.

| Person | Level / situation | Raw input formats | Job | Pages |
|---|---|---|---|---|
| `priya_shah/` | Entry / new grad (1 internship) | `.txt` draft resume, `.md` notes | Corvid Analytics, Junior Software Engineer | 1 |
| `elena_torres/` | Career switcher (7 yrs teaching) + bootcamp | `.docx` teaching resume, `.txt` notes | Brightboard Learning, Junior Full-Stack Developer | 1 |
| `jordan_rivera/` | Intermediate (4+ yrs backend) | `.md` old resume, `.txt` notes | Lumen Pay, Backend Engineer | 1 |
| `samuel_okafor/` | Staff (13+ yrs) + labeled career break | `.pdf` old resume, `.md` brag doc | Quillstack, Staff Software Engineer | 1 (limit 2) |

Each folder has the same shape:

| Stage | Files |
|---|---|
| Raw input | `profile/` |
| Master | `master/master_resume.md` (+ PDF), `stories.md`, `profile_facts.md`, `open_questions.md` |
| Job | `jobs/<slug>/job_description.txt` |
| Tailored | `custom_resumes/<slug>/`: resume, cover letter, keywords, match report, review |

## What each one teaches

- **Priya:** Education first with GPA, projects carrying evidence, no summary, a cover letter built on the posting's own question.
- **Elena:** the switcher order (Projects above Experience), rewriting a teaching job for results instead of hiding it, labeling coursework-only skills, the old domain as an advantage.
- **Jordan:** a duty-style resume turned into results; tailoring by reordering bullets; honest gaps (Kafka, Terraform) that stay gaps.
- **Samuel:** Selected Impact up top, staff archetype, compressing old roles, a one-line career break, two pages as a ceiling rather than a target (`review.md` shows the cut from a near-empty page 2), and a cover letter placeholder the agent refuses to fill because only Samuel can answer it.

Every `match_report.md` ends with "Edits for you": what only the person can add. Every `review.md` lists what the truth pass removed.

## Re-render and check

```bash
for p in priya_shah elena_torres jordan_rivera samuel_okafor; do
  python renderer/scripts/render.py examples/$p/master/master_resume.md
  python renderer/scripts/render.py examples/$p/custom_resumes/*/
done

python renderer/scripts/check.py examples/samuel_okafor/custom_resumes/quillstack_staff-software-engineer-developer-platform \
  --master examples/samuel_okafor/master --max-pages 2
```

Use `--max-pages 1` for the other three.

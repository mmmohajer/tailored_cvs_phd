# Application portals

## Findings

- **Doctoral admissions are run by departments, not by a central recruiter with a keyword robot.** In the CGS survey, graduate-school staff said academic units owned doctoral admissions about 78% of the time. [S06, B]
- **No study in this review shows that a doctoral portal auto-rejects CVs for columns, fonts, or missing keywords.** That claim belongs to industry applicant-tracking marketing. Do not import it.
- **The first screen is still mechanical.** Programs reported using transcripts, test scores, letters, and language scores to thin the pool before faculty spent time on statements. [S06, B; consistent with S07, B]
- **Forms repeat the CV.** Degree, GPA, dates, and test scores typed into Slate, ApplyWeb, GradCAS, or a university portal have to match the CV and the transcript exactly. A mismatch is a fact conflict, not a style choice.

## What the agent does

- Produce a single-column PDF with selectable text. The person uploads that PDF. The agent also keeps the Markdown, which is what gets edited.
- When the person pastes portal questions into `positions/<slug>/`, answer those questions in `match_report.md` with facts from the master, inside the character limit. Do not keyword-stuff the CV to game a score the portal has not been shown to compute.
- GPA, dates, degree titles, and test scores are copied from the master, which copied them from the person. If the portal asks for a 4.0-scale GPA and the transcript uses another scale, ask. Never convert a grade by guesswork.
- If a form asks about work authorization, citizenship, or demographic categories, the person answers it. The agent does not infer or fill those fields.

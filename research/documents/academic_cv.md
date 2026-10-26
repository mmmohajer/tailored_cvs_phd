# Academic CV

The tailored file is `custom_resumes/<slug>/cv.md`. It is a selection from the master for one position, not a second copy of `master_resume.md`. The master filename stays so the renderer can find it. Both are academic CVs.

## Findings

- **Education and research preparation are what a first reader can check.** Transcripts were the material doctoral programs most often called important at the initial screen (71%). [S06, B]
- **Prior research experience is the content of a STEM CV, and duration matters for later skill.** Undergraduate research participation predicted higher research-skill performance in early STEM graduate school. How long the research lasted was the strongest of the features measured, ahead of autonomy and collaboration. [S09, B]
- **Among students already admitted to one biomedical program, more months of research did not separate who later published.** Almost everyone admitted already had research experience, so the study has little to say about applicants with none. [S03, B]
- **A CV that lists duties without a contribution gives the statement and the letters nothing to corroborate.** Letters and the statement are what doctoral committees weigh at the final decision. [S06, B]

## What the agent does

Length, section order, and the country differences are in `research/format/cv_structure.md`. The program's page wins. When it is silent:

1. Education, with the thesis, the advisor, and the grade on the transcript's scale.
2. The research or job that meets this opening, on page one.
3. Publications on page one if any exist, next to that work. A link if the paper is online.
4. Teaching, only if it exists and this opening cares.
5. Awards that are on the master.
6. Methods and tools, each one traceable to an entry above.
7. References only when the page asks, and only people who have agreed, with the relationship and the email.

- Reverse chronological inside each section. [S17, D; S19, D; S27, D]
- A Dutch or German vacancy does not get a US-length faculty CV. An Italian bando that asks for Europass is exported by the person from the official editor, using these facts. [S16, D; S27, D; S28, D]
- Every research entry names the question or the system, the person's role, and the concrete outcome they can support (a poster, a method learned, a dataset, a draft). "Assisted" stays "assisted."
- Authorship is exact: first, co-first, middle, or last, and the status the person gave (published, in press, under review, draft). "In preparation" only when they said a draft exists.
- Industry jobs stay on the CV when they are real. They are written as research preparation only where the work actually was (a study, an evaluation, a dataset, a method). A job title is not converted into a lab role. See `research/situations/returning_and_industry.md`.
- Coursework appears when it is the evidence of preparation (a methods sequence, a proof-based math sequence, a language). A dump of every class does not.
- The master CV keeps every true entry. The custom CV keeps the ones that meet this position's methods, topics, or stated requirements.

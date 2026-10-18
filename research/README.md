# Research

What the agent knows about strong resumes and cover letters, and how sure it is.

Most resume advice online is opinion repeated until it sounds like fact. This folder keeps claims separate from evidence, so the rules in `rules/` only treat strong evidence as hard requirements.

## Evidence grades

| Grade | What it is | How the agent uses it |
|---|---|---|
| **A** | Controlled or field experiment, large sample, usually peer reviewed or a public working paper | Hard rule |
| **B** | Large employer survey or large-dataset report from a neutral body | Hard rule unless the job posting says otherwise |
| **C** | Vendor study (the author sells resume services), simulation, or small sample | Default, overridable |
| **D** | Hiring-side guidance or practitioner books: recruiters, hiring managers, engineering leaders | Default, explain when used |

Every claim cites a source ID like `[S05]`. Full references are in `sources.md`.

## Map

| Folder | Covers |
|---|---|
| `format/` | Length, ATS and parsing, layout, writing quality, personal details |
| `sections/` | Section order, header and summary, skills, experience bullets, projects, education |
| `levels/` | Internship, entry / new grad, intermediate, senior, staff |
| `situations/` | Career switchers, bootcamp and self-taught, employment gaps |
| `cover_letter/` | When it matters, structure, AI and the signal problem |

## How each file is written

1. **Findings**: what the evidence says, with grade and source.
2. **What the agent does**: the concrete behavior the finding implies.

## Updating

When you add a source: give it the next `S##` ID in `sources.md`, note the year and the sample, grade it, then change the findings that depend on it. Re-check numbers from yearly surveys (NACE, Jobscan) every year. Last full check: October 2026.

This research is US/Canada focused. Norms differ elsewhere (photos are common on German CVs, for example). Say so in the master when the target market differs.

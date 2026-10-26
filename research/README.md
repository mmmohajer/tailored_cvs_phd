# Research

What the agent knows about applying to PhD programs, and how sure it is.

Most admissions advice online is faculty lore repeated until it sounds like a finding. This folder keeps claims separate from evidence, so the rules in `rules/` only treat strong evidence as hard requirements.

## Evidence grades

| Grade | What it is | How the agent uses it |
|---|---|---|
| **A** | Meta-analysis or other large multi-sample peer-reviewed study | Hard rule |
| **B** | Peer-reviewed study, or a large survey from a neutral body such as the Council of Graduate Schools. Single-university studies of students already admitted are included, with that limit stated in the finding | Hard rule unless the program's instructions say otherwise |
| **C** | Vendor survey (ETS administers the GRE), small corpus, or commentary built on a thin sample | Default, overridable |
| **D** | Faculty essays, graduate-school career guidance, or a legal constraint on what an application may ask | Default. The program's current prompt, length, and required documents override it |

Every claim cites a source ID like `[S06]`. Full references are in `sources.md`.

## Map

| Folder | Covers |
|---|---|
| `countries/` | How the file changes by country and by route (committee, supervisor-first, advertised post). Read this before the other folders |
| `format/` | CV length and section order by country, writing, and what application portals actually do |
| `documents/` | Academic CV, cover letter, professor email and follow-up, statement of purpose when a position asks for one, research record, recommendation letters, fit with faculty |
| `fields/` | How disciplines weigh different parts of the file, inside a country |
| `situations/` | Applicants coming from industry, grades and gaps, no publications, international applicants |
| `statement/` | Which essays to write, structure, and voice, when the country file has not already chosen a different genre |

## How each file is written

1. **Findings**: what the evidence says, with grade and source.
2. **What the agent does**: the concrete behavior the finding implies.

## Updating

When you add a source: give it the next `S##` ID in `sources.md`, note the year and the sample, grade it, then change the findings that depend on it. Re-check the ETS/NAGAP testing figures each year. The CGS holistic-review survey is from 2015; treat its GRE percentages as a picture of that year, not of today. Last full check: October 2026.

Most of the grade A and B studies (S01–S09) are from the United States. They do not automatically describe the UK, Germany, the Netherlands, or anywhere else. `countries/` says what transfers. Countries without a file are handled in `countries/unlisted.md`, not by copying the US statement.

Professional doctorates (MD, JD, PsyD) and taught master's programs use different criteria. Say so when the person is applying to one of those instead.

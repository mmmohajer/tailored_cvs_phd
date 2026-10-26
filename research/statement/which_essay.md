# Which essays to write

## Findings

- **Doctoral programs ask for a personal or research statement, and they weigh it at the decision.** They do not all ask for the same second essay. [S06, B]
- **A diversity or personal-history essay is not a universal requirement.** Race-conscious admissions were restricted for covered US institutions in 2023. [S12, D] What a given department still asks is on its current instructions, not in a court opinion.
- **Writing samples and proposals matter where the discipline's product is a long argument or a designed project.** Committees evaluate with the field's own methods. [S08, B]

## What the agent does

Read `research/countries/which_system.md` first. Every position still gets the four files in `rules/04_statement.md`: `cv.md`, `cover_letter.md`, `professor_email.md`, and `follow_up.md`. The table below is an **extra** essay, written only when the country default or the position's instructions ask for it. The instructions in `positions/<slug>/` override the country default. List every required writing task in the match report before drafting.

| Country default, when the page is silent | File |
|---|---|
| United States, committee route | `statement.md` |
| United Kingdom, humanities or social sciences | `research_proposal.md` |
| United Kingdom, science project or studentship | `statement.md` aimed at that project, not an invented proposal |
| Germany | `motivation.md`, plus `research_proposal.md` on the individual route |
| Netherlands vacancy | `motivation.md` |
| Netherlands, own funding | `research_proposal.md` |
| Canada | `statement.md` |
| Italy, concorso that scores a project | `research_proposal.md`, at the bando's word cap |
| Italy, advertised post, page silent | `motivation.md` |
| No country file | The closest row in `research/countries/unlisted.md`, labeled as a guess |

| The program asks for | The agent writes |
|---|---|
| Statement of purpose or research statement | `statement.md` |
| A separate personal history or "additional information" | A second file, `personal_statement.md`, only if the prompt is different. It uses biography the person actually supplied |
| Research proposal with a specific format | `research_proposal.md`, following that format, ideas limited to the master and the person's answers |
| Writing sample | No new paper. Help choose among existing pieces and say why that piece fits. Light copy-editing only if asked |
| Teaching statement | `teaching_statement.md` only when required, from teaching the person really did |
| Diversity statement, and the current prompt still requests one | Answer the prompt with experiences the person described. Do not add an identity they did not state |
| Nothing about diversity | Do not add a diversity essay "to be safe" |

- One program, one set of essays. A statement written for another university is a source of facts, not a draft to swap names in.
- If two prompts overlap, answer each one. Do not paste the same three paragraphs into both.

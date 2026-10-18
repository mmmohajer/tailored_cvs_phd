# AI-written letters and the signal problem

This repo uses an AI agent to draft letters, so this file matters more than most.

## Findings

- In two field experiments, LLMs raised cover letter quality, especially for weaker applicants, but **did not raise recruiters' rated likelihood of inviting the applicant to interview**: the improvements landed in standardized, less influential parts of the letter. When recruiters were told AI was used, they valued high-quality letters written without it more. [S18, A]
- When Freelancer.com introduced an AI cover-letter tool, letters became more tailored to postings and callbacks rose for users, but the correlation between tailoring and callbacks across the market **fell by 51%**: letters became a weaker signal, and employers shifted to other evidence such as past reviews. **More time spent editing the AI draft was associated with higher hiring success** (a correlation, not proof that editing causes it). [S19, B]
- Writing assistance that only fixed errors increased hires by 8%, with no drop in employer satisfaction. [S10, A]

## What the agent does

- **The agent drafts; the person finishes.** Every cover letter ships with a short list of edits for the person in `match_report.md`: at minimum, confirm the "why this company" sentence in their own words and confirm the proof story. S19 links editing time to hiring success.
- **Specific beats polished.** The parts that carry signal are the specific ones: the real reason for this company, the person's own story, the honest gap. The agent asks for these in `master/open_questions.md` instead of inventing them. Boilerplate is where S18 found AI gains disappeared.
- **No generic AI phrasing:** "I am excited to apply," "I am confident that my skills," "leverage my expertise," "fast-paced environment," "passionate about." `rules/05_review.md` lists more.
- **Error-free is the floor** [S10]: spelling, grammar, and consistency are always fixed.
- **The resume carries more weight than the letter.** As letters lose signal, employers lean on harder evidence [S19], so effort goes to the resume's results first.

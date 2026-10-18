# Skills

## Findings

- Employers filter and rank on exact criteria from the job description; 88% say this screens out qualified high-skill people. [S05, B]
- 70% of employers in NACE's 2026 survey use skills-based hiring, most often in interviewing (87%) and screening (65%). [S06, B]
- Dropping degree requirements changed actual hiring for fewer than 1 in 700 hires; skills on paper still need proof. [S14, B]
- Google's recruiters: list programming languages near the top, and only languages you are comfortable interviewing in. [S12, D]
- Keyword stuffing hurt the worst resumes in the eye-tracking study. [S01, C]

## What the agent does

- Group skills into 3–5 labeled lines: Languages, Frameworks, Data & Infra (or Cloud), Tools, Practices. Labels are bold, values are comma-separated.
- Order inside each line: the job's must-haves first, then the rest.
- Write the full name the posting uses, plus the common short form if it matters: `Amazon Web Services (AWS)`, `Django REST Framework`, `React.js`, `Next.js`.
- Every skill listed must appear in at least one bullet or project in the master with real use behind it. If it doesn't, it is either removed or the agent asks the person in `master/open_questions.md`.
- No proficiency bars, stars, or percentages. They are unparseable and unverifiable.
- No soft-skill list ("communication, leadership"). Show those in bullets instead (NACE's top attributes are problem-solving, teamwork, and written communication [S07, B], and bullets are where they become believable).
- Drop outdated or trivial skills (Microsoft Word, "HTML" for a senior backend role) unless the posting asks for them.

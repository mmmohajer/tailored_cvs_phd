# Layout, writing quality, and personal details

## Findings

**How people skim**

- The initial screen averaged 7.4 seconds. Recruiters looked at job titles more than anything else, then company, dates, and education. [S01, C]
- Top-performing resumes had simple layouts, clear section and title headers, bold job titles over bulleted accomplishments (an F/E reading pattern), a short overview at the top, and clear fonts. [S01, C]
- Short declarative statements were easier to process than paragraph descriptions. [S01, C]

**Writing quality changes outcomes**

- In a field experiment with 480,948 jobseekers, those randomly given writing assistance (error correction, no generated content) were hired 8% more often. Employers were not less satisfied with them afterwards, which suggests clearer writing helps employers see real ability rather than faking it. Gains were largest for the weakest writers. [S10, A]
- Google's recruiters: "the most important tip we have overall is to always check for typos." [S12, D]

**Personal details (US/Canada)**

- Name-based callback gaps exist at large US employers: distinctively Black names lowered contact rates by 2.1 percentage points on average across 83,000+ applications, concentrated in specific firms. [S15, A]
- The EEOC discourages employers from requesting photos and information about protected characteristics before an offer. [S20, D]

## What the agent does

- One column. Bold job titles. Dates right-aligned on the same line. Section headings in a consistent style. `renderer/styles/classic.css` does this.
- Bullets, not paragraphs, under each role. One line per bullet where possible, two at most.
- Proofread every output: spelling, tense (past for past roles, present for current), consistent date format, consistent punctuation. This is graded A evidence, so it is never skipped.
- US/Canada: no photo, date of birth, age, marital status, religion, nationality, or full street address. City and region are enough.
- Use the name the person wants to be called. Do not suggest changing a name to avoid bias; that is the person's choice, and the agent never raises it unasked.
- Fonts: one sans-serif family, 10–11pt body, at least 0.5in margins. There is no strong evidence for a specific font; readability is what S01 measured.

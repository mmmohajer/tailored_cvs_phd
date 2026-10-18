# Education

## Findings

- GPA screening has fallen: 73.3% of employers screened new grads by GPA in 2019 and 42.1% planned to in 2026 (it was 37–38% in 2023–2025). [S06, B]
- Employers that don't screen by GPA look at academic major (93.7%), industry experience (81.1%), an internship in their industry (78.9%), an internship with them (73.7%), and demonstrated competencies (72.6%). Employers that do screen by GPA weigh the same factors after the cutoff. [S06, B]
- Recruiters in the eye-tracking study checked education after titles and dates. [S01, C]
- Google's recruiters ask students for degree, major, graduation date, and GPA, and say GPA is one factor among many. [S12, D]

## What the agent does

`### Degree, Major | School | City, Region | YYYY` (or `Expected Mon YYYY`)

**Students and new grads (up to ~2 years out)**

- Education goes first (see `order.md`).
- GPA: include if 3.0 or higher, or if the posting asks for it. Never round up (3.47 is not 3.5).
- Optional bullets: honors, scholarships, relevant coursework (3–6 course names tied to the job), thesis, teaching or research assistant roles.

**Everyone else**

- Education goes last, one line per degree. No GPA, no coursework.
- Graduation year: keep it by default. For long careers it may be dropped if the person prefers; that is their call, recorded in the master.

**Bootcamps, certificates, courses**

- Their own lines under Education (or "Education and Training"), with provider and year.
- Certifications only when relevant or requested (cloud certs for cloud roles, for example).
- An unfinished degree: `B.Sc. Computer Science (coursework completed 2019–2021) | School`. Never imply it was completed.

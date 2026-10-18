# Match report — Quillstack, Staff Software Engineer (Developer Platform)

## The posting

- **Level implied:** staff, first Staff hire on the platform. Samuel: staff, Architect archetype with Tech Lead work. → up to 2 pages, Summary + Selected Impact on page one (`research/levels/staff.md`). The relevant content fits one full page, so it stays at one rather than padding (`research/format/length.md`).
- **Location:** remote in Canada or Toronto. Matches.
- **Top 3 requirements:** (1) leading migrations across many teams, (2) building CI/CD platforms for many teams, (3) deep Kubernetes in production. Strong written communication runs through all of them.
- **Archetype the posting wants:** Architect ("set the multi-year technical direction"), the same as Samuel's current role.
- **Instructions:** resume and cover letter; "tell us about a migration you led and what you'd do differently."

## Requirements → evidence

| Requirement | Evidence in master | Status |
|---|---|---|
| 10+ years, recent Staff scope | 13+ years; Staff since Mar 2022 | strong |
| Deep Kubernetes in production | 140 services to AWS EKS; Kubernetes operators in Go | strong |
| Terraform / IaC | Golden-path Terraform modules | strong |
| CI/CD platforms for many teams | Shared CI/CD adopted by 25 teams; golden paths | strong |
| Leading multi-team migrations | 140-service migration, RFC + weekly guild | strong |
| Written communication (RFCs, design docs) | Migration RFC, ownership RFC, ~50 design docs reviewed a year, meetup talk | strong |
| AWS | EKS | strong |
| Reliability: ownership, on-call, incident review | Ownership + on-call RFC; sev-1s 14 → 5 | strong |
| Mentor senior engineers | 6 mentored, 3 promoted to senior | strong (mentored toward senior; growing Staff engineers not shown yet) |
| Nice: Go or Python | Platform CLI and operators | strong |
| Nice: OpenTelemetry | prototype only | gap (not claimed) |
| Nice: Backstage / developer portal | none | gap |
| Nice: fintech / accounting | Northpoint Bank fraud and payments (2014–2019) | partial: finance, not accounting, and not recent |

**Fit:** 10 strong, 1 partial, 2 gaps (both nice-to-haves). Strong apply.

## Choices made

- Headline swaps AWS for CI/CD: requirement 2 matters more here, and AWS appears throughout.
- Architecture review moved up the Staff role: the posting asks to "help run architecture review."
- Career break shown as one labeled line with real dates, per Samuel's wish and `research/situations/employment_gap.md`.
- Older roles (Northpoint Software Engineer, Pixelgrove) kept as title lines without bullets (`research/levels/staff.md`: compress old detail).
- PostgreSQL dropped from skills; nothing in this posting needs it.
- Kafka not listed (no evidence yet; master open question 1).

## Edits for you (cover letter)

1. **"What I'd do differently" (required by the posting):** the letter has a placeholder. Only you can answer it. One or two honest sentences, for example something you'd sequence differently, a team you'd have brought in earlier, or a cost you underestimated. **Don't send the letter until this is filled.**
2. **The opening:** it connects Quillstack's problem to your current role with facts only. If Tidewater's platform was also fragmented when you took it on (several deploy paths, multiple CI systems), say so; your brag doc doesn't describe its 2022 state, so the agent didn't claim it.
3. **Mentoring Staff engineers:** the posting wants someone to grow future Staff engineers. If any of your mentees are on that path, one clause here helps.

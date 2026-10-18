# Jordan Rivera
Backend Engineer | Python · Django · PostgreSQL
Toronto, ON | jordan.rivera@example.com | (555) 010-0199 | [linkedin.com/in/jordan-rivera-dev](https://linkedin.com/in/jordan-rivera-dev) | [github.com/jrivera-dev](https://github.com/jrivera-dev)

## Summary

Backend engineer with 4+ years building Python and Django services for health tech and logistics. Cut booking API p95 latency from ~900 ms to ~250 ms and built a reminder pipeline that sends ~150,000 messages a week and reduced clinic no-shows by 18%.

## Skills

- **Languages:** Python, SQL, TypeScript, JavaScript
- **Frameworks:** Django, Django REST Framework, Celery, FastAPI, React.js
- **Data & Infra:** PostgreSQL, MySQL, Redis, Docker, Amazon Web Services (AWS: ECS, RDS, S3)
- **Practices:** CI/CD with GitHub Actions, automated testing with pytest, zero-downtime database migrations, on-call and runbooks, mentoring

## Experience

### Software Engineer | Northwind Health | Remote | Mar 2024 – Present

- Cut p95 latency of the appointment booking API from ~900 ms to ~250 ms by adding Redis caching for clinic availability and removing three N+1 queries in the Django ORM.
- Built the appointment reminder pipeline on Celery and Redis, sending ~150,000 SMS and email reminders a week; clinics reported 18% fewer no-shows in the first quarter after launch.
- Co-led the zero-downtime migration of the appointment service from MySQL to PostgreSQL with one other engineer, writing the cutover plan and the dual-write and backfill scripts.
- Supported a booking platform used by ~300 clinics, joining the on-call rotation and writing 6 runbooks for the booking service.
- Mentored 2 engineering interns through their projects; one received a return offer.
- Built internal tools in TypeScript for the support team.

### Junior Software Engineer | Brightpath Logistics | Toronto, ON | Jul 2022 – Feb 2024

- Built a carrier webhook integration processing ~40,000 tracking events a day, with idempotent handling and automatic retries.
- Raised test coverage of the tracking service from 35% to 80% by writing its pytest suite.
- Cut release time from ~2 hours to 15 minutes by moving deployments from manual scripts to GitHub Actions.
- Built Django REST Framework APIs for shipment tracking used by the customer portal.

### Software Engineering Intern | Brightpath Logistics | Toronto, ON | May 2021 – Aug 2021

- Built an internal React.js dashboard that showed the operations team late shipments.

## Projects

### Transit Delay Bot | Python, FastAPI, PostgreSQL | [github.com/jrivera-dev/transit-delay-bot](https://github.com/jrivera-dev/transit-delay-bot)

- Telegram bot that posts transit delays for subscribed routes, used by ~1,100 people.

## Education

### B.Sc. Computer Science | Lakeshore University | Toronto, ON | 2022

<!--
Sources: profile/notes.txt (all numbers), profile/old_resume.md (titles cross-checked).
GPA 3.4 kept out by preference (more than 2 years since graduating).
"Co-led" agreed with Jordan: two engineers; Jordan owned the cutover plan and scripts.
-->

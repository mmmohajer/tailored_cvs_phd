# Jordan Rivera
Backend Engineer
Toronto, ON | jordan.rivera@example.com | (555) 010-0199 | [linkedin.com/in/jordan-rivera-dev](https://linkedin.com/in/jordan-rivera-dev)

October 17, 2026

Hiring Team
Lumen Pay

Dear Hiring Team,

I'm applying for the Backend Engineer role on your Payments Platform team. I've spent the last two and a half years building backend systems for clinics at Northwind Health, and Lumen Pay serves the same independent clinics from the other side: getting them paid. Your team cares "about correctness first, then speed," and I'd like to bring the habits I've built around safe migrations and idempotent processing to the services that move money.

The work closest to yours is a migration I co-led. Northwind's appointment service had to move from MySQL to PostgreSQL while ~300 clinics kept booking. With one other engineer, I wrote the cutover plan and the dual-write and backfill scripts, and we finished with zero downtime. Moving live data without downtime takes the same planning your team needs for payment and ledger data.

Your posting asks for reliable asynchronous workflows. I built Northwind's reminder pipeline on Celery and Redis, which sends ~150,000 reminders a week; clinics reported 18% fewer no-shows after launch. Before that, at Brightpath Logistics, I built a carrier webhook integration with idempotent handling and retries for ~40,000 events a day, and raised the tracking service's test coverage from 35% to 80%. I haven't worked with Kafka or Terraform yet. I have run the same retry and idempotency patterns in Celery, and I'd expect to pick up your tooling quickly.

I'd welcome a conversation about how I could help the Payments Platform team. Thank you for your time.

Sincerely,
Jordan Rivera

# Stories

## 1. The slow booking API

- **Situation:** Northwind Health's appointment booking API had p95 latency around 900 ms; clinics' front desks felt it during busy hours.
- **What I did:** Profiled the slowest endpoints, added Redis caching for clinic availability, and removed three N+1 queries in the Django ORM.
- **Result:** p95 dropped to about 250 ms.
- **Proves:** performance work, Redis, Django ORM, PostgreSQL, ownership.

## 2. Reminders that cut no-shows

- **Situation:** Clinics lost revenue and slots to missed appointments; reminders were manual.
- **What I did:** Built a reminder pipeline on Celery and Redis that schedules SMS and email reminders.
- **Result:** ~150,000 reminders a week; clinics reported 18% fewer no-shows in the first quarter after launch.
- **Proves:** asynchronous task queues, reliability at volume, product impact.

## 3. MySQL to PostgreSQL with zero downtime

- **Situation:** The appointment service needed to move from MySQL to PostgreSQL without interrupting bookings at ~300 clinics.
- **What I did:** With one other engineer; I wrote the cutover plan and the dual-write and backfill scripts.
- **Result:** Migration completed with zero downtime.
- **Proves:** data migrations, risk planning, PostgreSQL, collaboration.

## 4. Carrier webhooks at Brightpath

- **Situation:** Shipment tracking depended on carrier events arriving reliably.
- **What I did:** Built a webhook integration with idempotent processing and automatic retries.
- **Result:** Handles ~40,000 tracking events a day.
- **Proves:** event-driven integration, idempotency, reliability.

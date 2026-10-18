# Match report — Lumen Pay, Backend Engineer (Payments Platform)

## The posting

- **Level implied:** intermediate (3+ years). Jordan: intermediate, 4+ years. → 1–2 pages; 1 page fits everything relevant.
- **Location:** Toronto, hybrid 2 days. Matches Jordan's preference.
- **Top 3 requirements:** (1) PostgreSQL including live migrations, (2) reliable async workflows with retries and idempotency, (3) Python with Django or FastAPI in production.
- **Instructions:** resume plus a short cover letter "telling us why Lumen Pay." → letter written.

## Requirements → evidence

| Requirement | Evidence in master | Status |
|---|---|---|
| 3+ years backend Python | Jul 2022 – present, Python throughout | strong |
| Django or FastAPI in production | Django + DRF at Northwind and Brightpath; FastAPI in Transit Delay Bot (side project) | strong |
| PostgreSQL incl. live migrations | Co-led zero-downtime MySQL → PostgreSQL migration | strong |
| Task queues / event streaming | Celery reminder pipeline, ~150,000/week | strong (Celery); Kafka is a gap |
| AWS | ECS, RDS, S3 at Northwind | partial: listed in skills; no bullet shows AWS depth |
| Testing culture | Coverage 35% → 80% with pytest | strong |
| Retries, idempotency | Carrier webhooks, idempotent handling + retries | strong |
| On-call, observability | On-call rotation, 6 runbooks | partial: on-call yes; no observability work in master |
| Review code, grow newer engineers | Mentored 2 interns | strong |
| Nice: payments / fintech / ledger | none | gap |
| Nice: Kafka | none (Jordan confirmed) | gap |
| Nice: Terraform / IaC | none (Jordan confirmed) | gap |
| Nice: health or wellness software | Northwind Health, clinics | strong |

**Fit:** 9 strong, 2 partial, 3 gaps (all three are nice-to-haves). Recommend applying.

## Choices made

- Migration bullet moved to the top of Northwind: it is requirement 1.
- Headline adds Celery (requirement 2).
- Summary leads with async workflows and the migration instead of latency.
- Dropped the TypeScript internal-tools bullet (proves nothing this posting asks for).
- Kafka and Terraform are **not** added anywhere; the letter names the gap in one sentence.

## Gaps and what to do

- **Payments domain:** the clinic connection is the honest bridge (used in the letter). No payments claims.
- **Kafka / Terraform:** nice-to-haves. If Jordan wants, a small Terraform-deployed version of Transit Delay Bot would turn one gap into evidence.
- **AWS depth and observability:** see open questions in the master; if Jordan set up metrics, dashboards, or alerts at Northwind, that becomes a bullet.

## Edits for you (cover letter)

1. **Why Lumen Pay:** the opening uses the clinic connection and a quote from the posting. Replace it with your own reason if you have a better one (you use Lumen Pay, know someone there, read their engineering blog).
2. **Proof story:** if no bookings were lost during the migration and you know that for sure, say so; it's a stronger line than "without downtime," but it isn't in the master yet.
3. **Kafka / Terraform sentence:** keep it, soften it, or delete it; your call.
4. Read the whole letter aloud once and change any sentence that doesn't sound like you.

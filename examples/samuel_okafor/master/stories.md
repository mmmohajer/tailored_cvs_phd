# Stories

## 1. 140 services onto Kubernetes

- **Situation:** Tidewater's 140 services ran on self-managed VMs.
- **What I did:** Wrote the migration RFC, ran a weekly migration guild, and did the first 10 migrations myself as templates for other teams.
- **Result:** 140 services moved to AWS EKS over 5 quarters; infrastructure cost down 31% (~$2.4M a year, finance's figure); deploys went from roughly weekly per service to ~40 a day across the org.
- **Proves:** multi-team, multi-quarter execution; Kubernetes; leading through documents and examples, not authority.

## 2. Service ownership and on-call

- **Situation:** Not yet described (open question 2).
- **What I did:** Wrote the service ownership and on-call RFC, adopted org-wide in 2023.
- **Result:** Sev-1 incidents fell from 14 in 2023 to 5 in 2024, alongside other reliability work.
- **Proves:** org-level change through writing, reliability.

## 3. Golden paths

- **Situation:** Setting up a new service took about 2 weeks.
- **What I did:** Built golden-path templates with Terraform modules, GitHub Actions, and Argo CD.
- **Result:** New-service setup down to 1 day.
- **Proves:** developer experience, infrastructure as code.

## 4. Growing senior engineers

- **What I did:** Mentored 6 engineers.
- **Result:** 3 were promoted to senior.
- **Proves:** leverage through people.

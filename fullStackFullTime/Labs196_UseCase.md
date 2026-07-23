# Labs196 — Client Platform Use Case

**Role:** Senior Fullstack Developer  
**Company:** Labs196 (Real Estate & Finance IT)  
**Period:** Jan 2024 – Present (approx. 2.5 years)  
**Stack:** React.js, Next.js, TypeScript, TailwindCSS, Node.js (Express), Python, MongoDB, Firebase, JWT, Sumsub, HubSpot, Stripe, AWS (Amplify, EKS), Docker, Bitbucket CI/CD

---

## Company Context

Labs196 operates in the real estate and finance technology space. The business sells regulated investment and property-related products to retail and institutional clients. Internally, sales, compliance, and operations teams need visibility into pipeline health, KYC status, and payment activity.

My work centered on two surfaces:

1. **Client-facing product sites** — branded Next.js experiences where prospects browse offerings, complete onboarding, pass KYC/AML checks, and transact.
2. **Internal Admin Portal** — a React dashboard for sales KPI tracking, user/compliance review, and operational reporting.

Behind both sat a **Node.js REST API layer** (with supporting Python microservices for ETL and data processing), a **dual-database architecture** (MongoDB + Firebase), and integrations with **Sumsub**, **HubSpot**, **Stripe**, and **Firebase Auth**.

---

## Product Use Case: Regulated Investment Onboarding Platform

### What the product does

A unified digital onboarding and transaction platform for real estate and finance products. A typical end-to-end flow:

```
Prospect lands on product site (Next.js)
        ↓
Creates account (Firebase Auth → JWT issued by Node API)
        ↓
Browses investment/property products (MongoDB-backed catalog)
        ↓
Starts application → HubSpot deal/contact created automatically
        ↓
Completes KYC/AML (Sumsub SDK + webhook callbacks)
        ↓
Compliance review in Admin Portal (admin JWT + RBAC)
        ↓
Payment via Stripe (PCI-compliant, server-side intent creation)
        ↓
Status synced across MongoDB, Firebase real-time state, HubSpot
        ↓
Sales team sees updated KPIs in Admin Portal
```

### Why this architecture

| Layer | Choice | Reason |
|-------|--------|--------|
| Client UI | Next.js + TypeScript + Tailwind | SEO for product pages, fast iteration from Figma, SSR for marketing content |
| Admin UI | React.js + TypeScript | Rich dashboards, sales KPI widgets, compliance queues |
| API | Node.js (Express) REST | Single integration hub for Sumsub, HubSpot, Stripe webhooks |
| Auth | Firebase Auth + JWT | Firebase handles identity; Node issues scoped JWTs for API/admin vs user roles |
| Primary data | MongoDB | Flexible schemas for applications, documents, semi-structured product data |
| Real-time state | Firebase / Firestore | Live KYC status, notification badges, session-adjacent UI state |
| Compliance | Sumsub (KYC/AML) | Regulatory requirement before funds move |
| CRM | HubSpot | Sales pipeline, deal stages, marketing attribution |
| Payments | Stripe | PCI scope reduction via server-side payment intents |
| Infra | AWS Amplify (frontend), EKS + Docker (backend), Bitbucket CI/CD | Repeatable deploys, containerized services |

### User vs Admin separation

- **End users** authenticate through Firebase, receive a short-lived JWT, and can only access their own application data and product catalog endpoints.
- **Admins** authenticate through the same identity layer but receive JWTs with elevated claims (`role: admin`, `scope: compliance | sales | ops`). Admin routes enforce RBAC middleware before any MongoDB query runs.
- **Service-to-service** calls (webhooks from Sumsub/Stripe) use HMAC signature verification, not user JWTs.

---

## How We Achieved SLA (94% Production Issue Resolution Rate)

SLA here meant: **production defects triaged, root-caused, and resolved or mitigated within the agreed window** — not just uptime. We tracked resolution in Jira with severity labels (P0–P3).

### 1. Severity-based response targets

| Severity | Definition | Target |
|----------|------------|--------|
| P0 | Payments blocked, KYC pipeline down, auth failure | Acknowledge < 30 min, fix or rollback < 4 hrs |
| P1 | Single integration degraded (HubSpot sync lag, webhook backlog) | Same business day |
| P2 | UI defect, non-blocking admin issue | 1–2 business days |
| P3 | Cosmetic, backlog | Next sprint |

### 2. Ownership model

- I owned **production support for live services** — first responder for backend/API and full-stack defects.
- QA filed reproducible tickets with environment, user role, and request IDs.
- Product prioritized P0/P1 in daily standups; sales flagged client-impacting issues through a dedicated Slack channel.

### 3. Operational practices that moved the needle

**Structured triage checklist (every P0/P1):**
1. Is it auth, integration, data, or deploy-related?
2. Check API health, EKS pod status, recent Amplify/EKS deploys.
3. Pull correlation ID from logs; trace MongoDB document + HubSpot contact + Sumsub applicant ID.
4. Decide: hotfix, feature flag off, or rollback.

**Deploy safety (contributed to ~40% deployment time reduction):**
- Bitbucket pipelines: lint → test → Docker build → EKS rollout.
- AWS Amplify preview builds for Next.js before production promote.
- Rollback playbook documented per service; no manual SSH deploys.

**Dual-database discipline:**
- MongoDB = source of truth for business records.
- Firebase = derived real-time/UI state only.
- Webhook handlers write MongoDB first, then push to Firebase — never the reverse.

**Integration resilience:**
- Webhook endpoints return 200 fast, process async via internal queue/retry.
- HubSpot calls batched and rate-limit aware.
- Sumsub status polled as fallback when webhooks lag beyond threshold.

**QA partnership:**
- QA owned regression on KYC happy path + payment sandbox before each release.
- Shared test accounts for admin vs user roles reduced "works on my machine" cycles.

### 4. Metrics we reported

- **94% SLA resolution rate** — issues closed within severity window over a rolling quarter.
- **Deployment time −40%** — after Next.js architecture cleanup and pipeline automation.
- **Mean time to acknowledge (MTTA)** for P0/P1 tracked weekly in Jira dashboards.

---

## Biggest Production Issues and How We Handled Them

### Issue 1: Sumsub webhook delays left users stuck in "Pending Verification"

**Symptom:** Users completed document upload in the Sumsub widget, but the client UI stayed on "Under Review" for 30+ minutes. Sales saw stale HubSpot deal stages.

**Root cause:** Sumsub webhooks occasionally arrived out of order or were dropped during a brief EKS ingress misconfiguration. Our handler processed the first `pending` event but missed the final `approved` event. Firebase showed stale state; MongoDB was correct only after manual poll.

**Fix:**
- Webhook handler became **idempotent** (keyed on `applicantId + inspectionId + status`).
- Added a **scheduled reconciliation job** (Python cron on EKS) that polls Sumsub for any application stuck > 15 minutes.
- MongoDB updated first; Firebase sync ran as a second step.
- Admin Portal gained a "Force refresh KYC" action for compliance team.

**Lesson:** Never trust a single webhook delivery for regulated workflows. Always have poll-based reconciliation.

---

### Issue 2: MongoDB ↔ Firebase drift broke real-time dashboards

**Symptom:** Admin Portal showed "Verified" in one panel and "Pending" in another. Client notification badges disagreed with account settings page.

**Root cause:** Early implementation wrote verification status to Firebase from the client after Sumsub callback, while the API wrote to MongoDB. Race conditions and partial client writes caused drift.

**Fix:**
- Enforced **write path rule**: only the Node API writes business state; clients read from API or Firebase listeners fed by API.
- Migration script backfilled MongoDB as canonical; Firebase documents rebuilt from MongoDB snapshots.
- Added a nightly **consistency audit** job flagging mismatches to Slack.

**Lesson:** Dual-database works when roles are strict — MongoDB owns truth, Firebase owns presentation speed.

---

## Databricks ETL Pipeline — Data Processing & Analysis

Operational data lived in **MongoDB** as semi-structured documents (nested KYC payloads, variable product fields, webhook audit blobs). Sales and compliance needed **structured, joinable, reporting-ready tables** — not raw JSON. Direct MongoDB aggregation was too slow for month-end exports and cross-source joins (HubSpot deal stage + Sumsub status + Stripe payment in one view).

We built a **Python ETL layer on Databricks (PySpark)** that ran on a nightly schedule (with an on-demand trigger before stakeholder reviews).

### Pipeline flow

```
MongoDB (operational)          HubSpot / Stripe exports (CSV/API snapshots)
        │                                    │
        └──────────────┬─────────────────────┘
                       ▼
              Databricks Bronze (raw ingest)
         — append-only JSON/Parquet, ingestion timestamps
                       ▼
              Databricks Silver (cleansed)
         — flatten nested docs, type coercion, dedupe by _id
                       ▼
              Databricks Gold (business metrics)
         — funnel, KPIs, compliance SLA tables
                       ▼
         Python export job → MongoDB reporting collections
                       ▼
              Admin Portal dashboards + CSV exports
```

### Source data we ingested

| Source | What it contained | Shape in MongoDB |
|--------|-------------------|------------------|
| `applications` | User applications per product | Semi-structured: `userId`, `productId`, `status`, nested `steps[]`, `metadata` |
| `kyc_events` | Sumsub webhook audit trail | Unstructured blobs: `applicantId`, `reviewStatus`, `rejectLabels[]`, raw payload |
| `payments` | Stripe intent references | Semi-structured: `amount`, `currency`, `stripePaymentId`, `applicationId` |
| `hubspot_sync_log` | CRM sync outcomes | Log-style: `contactId`, `dealId`, `stage`, `syncedAt`, `error` |
| `products` | Catalog / fund metadata | Mixed: flat fields + nested `terms`, `geoRestrictions` |

HubSpot deal snapshots and Stripe settlement summaries were pulled separately and landed in Bronze as **structured CSV/Parquet** alongside the MongoDB dumps.

### Transform logic (Silver layer)

PySpark jobs did the heavy lifting:

1. **Flatten nested MongoDB documents** — e.g. `steps.kyc.completedAt` promoted to typed columns instead of querying dot-notation at read time.
2. **Map unstructured → semi-structured** — Sumsub `rejectLabels` arrays normalized to a single `rejection_reason` column; unknown labels bucketed to `other`.
3. **Deduplication** — `row_number() OVER (PARTITION BY application_id ORDER BY updated_at DESC)` to keep latest record per application when webhook replays created duplicates.
4. **Schema validation** — rows failing type checks (bad dates, null `productId`) quarantined to a `silver_quarantine` table for ops review instead of breaking the job.
5. **Cross-source joins** — `applications` ⋈ `kyc_events` ⋈ `payments` ⋈ `hubspot_deals` on `application_id` / `user_id` / `hubspot_contact_id`.

Example of what a **cleansed application row** looked like after Silver:

| Column | Example value |
|--------|---------------|
| `application_id` | `app_8f3c2a1b` |
| `user_id` | `usr_44e91d00` |
| `product_id` | `prod_reit_income_2024` |
| `product_name` | `Metro Income REIT Fund` |
| `application_status` | `funded` |
| `kyc_status` | `approved` |
| `kyc_completed_at` | `2024-11-14 09:22:11` |
| `payment_amount_usd` | `25000.00` |
| `payment_status` | `succeeded` |
| `hubspot_deal_stage` | `closedwon` |
| `days_signup_to_kyc` | `2` |
| `days_kyc_to_payment` | `5` |
| `ingested_at` | `2024-11-15 02:00:00` |

### Gold layer — metrics & analysis outputs

Gold tables were purpose-built for the Admin Portal and leadership exports:

| Gold table | Purpose | Key columns / grains |
|------------|---------|----------------------|
| `daily_funnel` | Conversion by stage | `date`, `product_id`, `signups`, `kyc_started`, `kyc_approved`, `payments_initiated`, `funded` |
| `kyc_sla_daily` | Compliance turnaround | `date`, `median_hours_to_approve`, `pct_stuck_over_24h`, `top_reject_reason` |
| `sales_kpi_weekly` | Sales team dashboard | `week`, `rep_region`, `deals_created`, `deals_closed`, `total_funded_usd` |
| `product_performance` | Product comparison | `product_id`, `applications`, `approval_rate`, `avg_ticket_usd`, `drop_off_stage` |
| `integration_health` | Ops visibility | `date`, `hubspot_sync_failures`, `sumsub_webhook_lag_p95_sec` |

A simplified **funnel row** in `daily_funnel` looked like:

```
date: 2024-11-14 | product: Metro Income REIT | signups: 48 | kyc_started: 41 | kyc_approved: 36 | funded: 22
→ conversion signup→funded: 45.8%
```

### How data reached the Admin Portal

Databricks did not serve the UI directly. A **Python export microservice** (scheduled after Gold jobs completed):

1. Read Gold tables from Databricks SQL / Delta Lake.
2. Write slim aggregates into MongoDB `reporting_*` collections (indexed for dashboard queries).
3. Node.js REST API exposed `/admin/metrics/*` endpoints consumed by the React Admin Portal.

This kept the live app fast — dashboards queried pre-aggregated reporting collections, not raw `applications` with 50KB nested documents.

### Why Databricks instead of only MongoDB aggregation

| Problem | MongoDB-only approach | Databricks approach |
|---------|----------------------|---------------------|
| Nested KYC payloads | Slow `$unwind` + `$lookup` at scale | Spark flatten once, reuse across tables |
| Cross-source joins | HubSpot/Stripe data not in MongoDB | Bronze ingest from all sources, join in Silver |
| Month-end exports | Timeouts on 100k+ doc scans | Gold tables materialized; export in minutes |
| Historical trends | Hard to snapshot daily | Partitioned Delta tables by `date` |
| Data quality | Bad rows fail silently in app | Quarantine table + Slack alert on quarantine count spike |

### Tie-in to production issues

The same pipeline directly supported **Issue 1** and **Issue 2** remediation:

- **`integration_health`** surfaced Sumsub webhook lag (p95) — we spotted the stuck-KYC spike before sales complained.
- **Nightly consistency audit** (Issue 2) compared MongoDB canonical status vs Firebase snapshot counts; mismatches fed a small Bronze table that the ETL job flagged in `integration_health`.
- After fixing write-path rules, we re-ran Silver/Gold for affected date ranges so Admin KPIs backfilled correctly without manual spreadsheet fixes.

### Interview one-liner (ETL)

> "We ran PySpark on Databricks to flatten semi-structured MongoDB application and KYC data, join it with HubSpot and Stripe snapshots, and materialize Gold funnel and compliance SLA tables. A Python export job loaded those aggregates into MongoDB reporting collections that powered the Admin sales KPI dashboard — so leadership got daily conversion and funded-volume metrics without hammering the operational database."

---

## Architecture Diagram (Simplified)

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT SURFACES                          │
│  Next.js Product Sites          React Admin Portal              │
│  (public + authenticated)       (admin JWT + RBAC)              │
└───────────────┬─────────────────────────────┬───────────────────┘
                │                             │
                ▼                             ▼
┌───────────────────────────────────────────────────────────────────┐
│              Node.js Express REST API (EKS / Docker)              │
│  JWT middleware │ RBAC │ Webhook routers │ Stripe intents         │
└───┬─────────┬──────────┬────────────┬──────────────┬──────────────┘
    │         │          │            │              │
    ▼         ▼          ▼            ▼              ▼
 MongoDB  Firebase   Sumsub      HubSpot          Stripe
 (truth)  (realtime) (KYC/AML)   (CRM)           (payments)
    │
    ▼
 Databricks (PySpark): Bronze → Silver → Gold
    │
    ▼
 Python export → MongoDB reporting_* → Admin KPI dashboards
```

---

## Interview Talking Points (STAR-ready)

### Dual database architecture
**Situation:** Needed fast client UX and reliable reporting on regulated application data.  
**Task:** Design storage without duplicating business logic.  
**Action:** MongoDB for canonical records; Firebase for real-time UI; API-only writes; nightly consistency audit.  
**Result:** Improved scalability and reporting readiness; eliminated most state drift after reconciliation job.

### 94% SLA resolution
**Situation:** Fast-paced product environment with shifting priorities and live client money/compliance flows.  
**Task:** Own production triage without burning out the team.  
**Action:** Severity matrix, Jira discipline, QA partnership, rollback playbooks, async integration patterns.  
**Result:** 94% of production issues resolved within SLA window; deploy time cut ~40%.

### PCI + KYC compliance
**Situation:** Platform handled payments and identity verification for finance products.  
**Task:** Keep PCI scope small and KYC auditable.  
**Action:** Stripe server-side intents only; Sumsub SDK for capture; no card data on our servers; webhook idempotency and audit logs in MongoDB.  
**Result:** Secure workflows across full stack without custom card handling.

### Databricks ETL for sales & compliance reporting
**Situation:** Operational data in MongoDB was semi-structured and slow to aggregate; sales needed daily funnel and funded-volume KPIs.  
**Task:** Build a reliable pipeline from raw app/KYC/payment data to dashboard-ready metrics.  
**Action:** PySpark jobs on Databricks (Bronze → Silver → Gold), flatten nested docs, dedupe webhook replays, join HubSpot/Stripe; Python export to MongoDB `reporting_*` collections.  
**Result:** Admin Portal loaded pre-aggregated metrics in seconds; month-end stakeholder exports dropped from manual pulls to scheduled CSV from Gold tables.

---

## Tech Summary (Quick Reference)

| Area | Technologies |
|------|----------------|
| Frontend | React.js, Next.js, TypeScript, TailwindCSS, Figma → production UI |
| Backend | Node.js (Express), Python microservices, REST APIs |
| Auth | Firebase Auth, JWT, RBAC (user vs admin) |
| Data | MongoDB (primary), Firebase/Firestore (real-time), Databricks (PySpark ETL), Delta Lake Gold tables |
| Integrations | Sumsub (KYC/AML), HubSpot (CRM), Stripe (payments) |
| DevOps | Git, Bitbucket, AWS Amplify, Docker, AWS EKS, CI/CD pipelines |
| Process | Jira, QA collaboration, production support ownership |

---

## Key Metrics (from tenure)

- **~40%** reduction in deployment time (Next.js architecture + CI/CD automation)
- **94%** SLA resolution rate on production issue triage
- Dual database architecture improving scalability, consistency, and reporting readiness
- Databricks ETL pipeline delivering daily funnel, KYC SLA, and sales KPI tables to Admin dashboards

---

*Document prepared for interview prep and stakeholder storytelling. Aligns with resume experience at Labs196, Jan 2024 – Present.*

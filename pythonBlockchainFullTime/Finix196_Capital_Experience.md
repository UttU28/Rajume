# Finix196 Capital — Data Science Specialist

**Jan 2024 – Feb 2025 · On-Site, TX · Contract**

---

## Company

Finix196 Capital is a **financial services** firm focused on **real-world asset (RWA) tokenization** — especially real estate and capital-markets products. Investors, advisors, and internal ops teams need trustworthy numbers for **pipeline health**, **onboarding/KYC status**, **funded volume**, and **tokenized-asset performance**. Bad or late data blocks decisions; the job was to turn messy operational sources into **model-ready and dashboard-ready** datasets.

---

## My Role

I was the **Data Science Specialist** supporting analytics and data pipelines for the capital / tokenization platform — **Python** ETL, **Azure Databricks**, curated reporting tables, and stakeholder-facing metrics.

**I contributed to:**

- **Python ETL / feature pipelines** — extract, cleanse, join operational data for investment and onboarding analytics
- **Azure Databricks (PySpark)** — Bronze → Silver → Gold style jobs for reporting-ready tables
- **Stakeholder metrics** — funnel, KYC/SLA, funded volume, and capital-ops KPIs for internal dashboards
- **Data quality** — dedupe, schema validation, quarantine bad rows, reconcile webhook/event replays
- **Azure data services** — Azure SQL / storage-backed curated outputs consumed by APIs and dashboards
- **Observability for data jobs** — job health, failure alerts, and faster detection when pipelines broke
- **Partnering with engineering** — APIs and frontends that served curated metrics (not ad-hoc spreadsheet pulls)

**Under senior guidance for:** metric definitions, compliance-sensitive fields, and production data access — I implemented and operated pipelines, not solo-owned product policy.

**App / product teams owned:** client and admin UI, primary product APIs, and business metric sign-off.

---

## Team


| Group | How we interact |
| ----- | --------------- |
| **Data / analytics** | Pipeline design, metric definitions, dashboard consumers |
| **Platform / backend engineers** | APIs that read curated tables; Azure infra for Databricks and storage |
| **Product / sales ops** | Which KPIs matter for capital pipeline and tokenization status |
| **Compliance** | What can appear in reports; retention and access for sensitive fields |
| **Leadership** | Daily/weekly funded-volume and funnel reviews |


On-site in **Texas** — close loop with ops and engineering on metric accuracy and pipeline SLAs.

---

## How Work Reaches Me

- **Jira** — pipeline features, data bugs, new metric requests
- **Job alerts** — Databricks / Azure Monitor failures on scheduled ETL
- **Slack / Teams** — “numbers look wrong” from sales ops or leadership
- **PR reviews** — notebook and Python job changes before promote

**Priority:** broken production metrics and missed SLA windows first, then new features and backfills.

**Triage flow:** alert or ticket → Databricks run history / logs → source vs curated table check → fix transform or backfill → re-validate dashboard numbers.

---

## Platform Stack


| Tool | Job |
| ---- | --- |
| **Python / Pandas** | ETL scripts, validation, export jobs |
| **Azure Databricks / PySpark** | Batch transforms, Bronze → Silver → Gold |
| **Azure SQL / Blob** | Curated stores and raw/landing zones |
| **MongoDB / operational DBs** | Source application and event data (as applicable) |
| **Grafana / Azure Monitor** | Pipeline and job health visibility |
| **Azure DevOps** | CI for notebooks/jobs, promote across envs |
| **Internal dashboards** | Consume Gold / reporting collections for KPIs |


**Single cloud (Azure)** for this engagement — Databricks + Azure data services as the analytics backbone. Distinct from LABS196 Innovations multicloud platform work later.

---

## Where Data Flows

```
Operational sources (apps, CRM/payment events, onboarding status)
        │
        ▼
Azure Databricks
  Bronze  → land raw / near-raw extracts
  Silver  → cleanse, flatten, dedupe, validate
  Gold    → funnel, KYC SLA, funded-volume aggregates
        │
        ├── Azure SQL / reporting collections
        ├── Python export jobs → dashboard APIs
        └── Stakeholder exports (scheduled CSV / views)
```


| Layer | Where | Who owns |
| ----- | ----- | -------- |
| Source systems | Product DBs / SaaS | Product + backend |
| Databricks jobs | Azure | Data Science + platform |
| Curated tables | Azure SQL / reporting stores | Data Science |
| Dashboards / APIs | App layer | Engineering (+ my metric contracts) |


---

## CI/CD & Job Promotion


| Layer | Tool |
| ----- | ---- |
| **Git** | Azure DevOps Repos (or GitHub — org-dependent) |
| **CI + promote** | **Azure DevOps Pipelines** for job/notebook validation |


```
PR / merge
  → lint / unit checks on Python transforms
  → run job in Dev / Test against sample data
  → validate row counts + key metrics vs expected
  → promote schedule to Prod
  → watch first Prod run + dashboard sanity check
```

### What I worked on in pipelines

- Scheduled Databricks jobs and on-demand backfills
- Validation gates before promoting transform changes
- Post-run checks — row counts, null rates, KPI deltas vs prior day

---

## Monitoring


| Layer | Tool | Purpose |
| ----- | ---- | ------- |
| Job runs | **Databricks** run history | Failed stages, duration, skew |
| Platform | **Azure Monitor** | Cluster/job infra alerts |
| Metrics sanity | Dashboards + spot checks | KPI jumps/drops after deploys |


**Key outcome:** faster detection when overnight ETL failed or Gold tables drifted — ops and leadership were not discovering bad numbers only in Monday reviews.

**Incident flow:**

```
Alert (job fail / stale Gold table)
  → Databricks logs (which stage)
  → Source freshness check
  → Fix transform or re-run / backfill
  → Confirm dashboard KPIs
```

---

## Core Deliverables

**Problem:** capital and tokenization ops needed daily funnel and funded-volume metrics; ad-hoc pulls were slow and inconsistent.

**What we did:**

- Standardized **Python + Databricks** ETL into curated Gold tables
- Defined metric contracts with product/sales ops
- Exported slim aggregates for dashboards and stakeholder reviews

**Result:** repeatable daily metrics instead of manual spreadsheet rebuilds; clearer SLA on when numbers are “official.”

---

## Data Quality & Reconciliation

**Targets for critical capital reporting paths:**

- Overnight jobs complete before morning ops review
- Dedupe webhook/event replays so KPIs are not double-counted
- Quarantine bad rows instead of silently corrupting Gold

**What I helped automate:**

- Validation rules (schema, null thresholds, primary-key uniqueness)
- Reconciliation jobs for stuck or delayed onboarding/status events
- Documented backfill runbooks for missed windows

---

## Values & Secrets



### Non-secret config (safe in Git / pipeline variables)


| Value | Source |
| ----- | ------ |
| Job schedule, cluster size | Platform + data standards |
| Table names, metric definitions | Docs / shared config |
| Environment name | Pipeline variable groups |


### Secrets (never in Git)


| Secret | Store | Access |
| ------ | ----- | ------ |
| DB connection strings | **Azure Key Vault** | Job identity / managed identity |
| API keys (CRM/payment exports) | **Key Vault** | Referenced in pipeline / Databricks secrets |


**Interview one-liner:**

> "At Finix196, sensitive capital and investor-adjacent data stayed in Key Vault-backed connections — pipelines used managed identity, and metric definitions were signed off with compliance and product before they hit leadership dashboards."

---

## What I Built & Improved

1. **Databricks ETL** — Bronze/Silver/Gold jobs for investment funnel and tokenization ops metrics
2. **Python export layer** — curated aggregates for dashboards and stakeholder exports
3. **Data quality gates** — dedupe, schema checks, quarantine paths
4. **Faster failure detection** — job monitoring so broken overnight runs were caught before morning reviews
5. **Metric contracts** — shared definitions with sales ops and engineering consumers
6. **Azure DevOps promotion** — safer path from Dev transforms to Prod schedules

---

## Testing & Pipeline Validation

**Job changes:**

- Unit-style checks on transform helpers
- Dev/Test run on sample extracts before Prod
- Compare key KPI totals vs prior trusted run

**How I validated my own changes:**

- Run notebook/job in lower env first
- Spot-check Silver row samples and Gold aggregates
- Confirm dashboard widgets match Gold
- For backfills: document window and re-verify downstream consumers

---

## Why It Matters

Tokenization and capital ops live or die on **trusted daily numbers**. If funnel or funded-volume metrics are late or double-counted, leadership and advisors make decisions on noise. This role connected **Python data science work** directly to **business reporting reliability** — not notebook demos.

---

## Interview Shortcuts



### 30 seconds

> "Data Science Specialist at Finix196 Capital — RWA tokenization and capital analytics on Azure. I built Python and Databricks ETL into Gold tables for funnel, KYC SLA, and funded-volume metrics, with data-quality gates and Azure DevOps promotion so leadership dashboards stayed accurate and on time."



### 2 minutes

> "Finix196 Capital focuses on real-world asset tokenization — mostly real estate and capital products. My job as Data Science Specialist was to turn operational sources into reliable analytics.
>
> I built Azure Databricks pipelines in a Bronze → Silver → Gold pattern: land extracts, cleanse and dedupe, then publish aggregates for funnel health, onboarding SLA, and funded volume. Python export jobs fed dashboards and stakeholder exports so sales ops stopped rebuilding spreadsheets by hand.
>
> A big part of the work was data quality — schema checks, quarantine, and reconciling event replays so KPIs were not inflated. We monitored job health so overnight failures were caught before morning reviews. Secrets and DB access went through Azure Key Vault with managed identity. Azure DevOps gated promote of transform changes from Dev to Prod."



### STAR bullets

**Databricks ETL / Gold metrics**

- *Situation:* Leadership needed daily capital funnel and funded-volume metrics; pulls were manual
- *Task:* Automate trustworthy curated tables
- *Action:* PySpark Bronze/Silver/Gold + Python export to reporting stores
- *Result:* Repeatable daily KPIs for ops and stakeholder reviews

**Data quality**

- *Situation:* Webhook/event replays double-counted metrics
- *Task:* Keep Gold accurate
- *Action:* Dedupe keys, quarantine bad rows, reconciliation jobs
- *Result:* Stable KPI totals stakeholders could trust

**Pipeline monitoring**

- *Situation:* Overnight job failures discovered too late
- *Task:* Faster detection before morning reviews
- *Action:* Databricks run monitoring + Azure Monitor alerts + sanity checks on Gold
- *Result:* Broken runs caught and backfilled before ops standup

**Promotion / Azure DevOps**

- *Situation:* Transform changes risked Prod metric drift
- *Task:* Safer promote path
- *Action:* Dev/Test validation, row-count and KPI delta checks, then Prod schedule update
- *Result:* Fewer bad deploys into leadership-facing numbers



### Likely follow-ups


| Question | Hint |
| -------- | ---- |
| What is Finix196? | Capital / RWA tokenization — real estate investing tech |
| Your title? | **Data Science Specialist** (contract, on-site TX) |
| Main tools? | **Python**, **Azure Databricks / PySpark**, Azure SQL/Blob, Azure DevOps |
| Bronze/Silver/Gold? | Land → cleanse/dedupe → business aggregates |
| Who defined KPIs? | Product / sales ops + leadership; I implemented pipelines |
| Secrets? | **Azure Key Vault** + managed identity — never in Git |
| Finix196 vs LABS196? | Finix196 = Azure analytics/data science for capital metrics. LABS196 Innovations = later Sr. Python Blockchain / multicloud platform work |
| Delta Dental? | Not on LinkedIn/resume for this window — use **Finix196 Capital** |



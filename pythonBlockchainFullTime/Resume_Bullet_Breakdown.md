# Resume Bullet Breakdown — Who Said What / What I Did

Line-by-line breakdown of every resume bullet for **Finix196 Capital** and **LABS196 Innovations**.

Format per bullet:
- **Resume point** — exact bullet text
- **Who decided / directed** — who was above you, who set the rules
- **What I did** — your hands-on work in short

---

# Finix196 Capital — Data Science Specialist (Jan 2024 – Feb 2025)

**Your level:** Mid-level IC on data/analytics  
**Above you:** Engineering leads, product/sales ops for metric definitions, compliance  
**Peers:** Backend engineers, dashboard consumers, other data contributors

---

## Bullet 1 — Databricks ETL / RWA capital metrics

**Resume:**
> Built Python and Azure Databricks (PySpark) ETL pipelines for a real-world asset (RWA) tokenization capital platform, producing Bronze/Silver/Gold tables for investment funnel, KYC/SLA, and funded-volume analytics consumed by internal dashboards.

| | |
|---|---|
| **Leadership / product said** | We need daily funnel, KYC SLA, and funded-volume numbers — not spreadsheet rebuilds. |
| **Engineering said** | Sources live in operational DBs/events; dashboards will read curated stores. |
| **I did** | Implemented PySpark Bronze→Silver→Gold jobs and Python transforms that published those KPIs. |

---

## Bullet 2 — Python export / reporting stores

**Resume:**
> Developed Python export and validation jobs that curated reporting-ready datasets into Azure SQL and reporting stores, replacing manual spreadsheet pulls for sales ops and leadership reviews.

| | |
|---|---|
| **Sales ops said** | Morning reviews need trusted exports; stop hand-pulling. |
| **I did** | Built scheduled Python export/validation into Azure SQL / reporting collections. |

---

## Bullet 3 — Data quality

**Resume:**
> Implemented data quality controls including schema validation, deduplication of event/webhook replays, and quarantine paths so Gold KPIs stayed accurate for capital and onboarding metrics.

| | |
|---|---|
| **Seniors said** | Webhook replays double-count; quarantine bad rows — don't silently corrupt Gold. |
| **I did** | Added schema checks, dedupe keys, quarantine paths, and reconciliation helpers. |

---

## Bullet 4 — Pipeline monitoring

**Resume:**
> Contributed to pipeline monitoring with Databricks run health and Azure Monitor alerts, improving detection of overnight ETL failures before morning stakeholder reviews.

| | |
|---|---|
| **Ops said** | Catch overnight failures before standup. |
| **I did** | Wired run-health checks and Azure Monitor alerts; triaged failed jobs and backfills. |

---

## Bullet 5 — Azure DevOps promotion

**Resume:**
> Supported promotion of transform changes through Azure DevOps pipelines across Dev/Test/Prod, with row-count and KPI delta checks before updating production job schedules.

| | |
|---|---|
| **Platform said** | Promote Dev→Test→Prod; validate before touching Prod schedules. |
| **I did** | Ran validation gates (row counts, KPI deltas) and updated Prod job schedules safely. |

---

## Bullet 6 — Key Vault / secrets

**Resume:**
> Secured data-store credentials with Azure Key Vault and managed identity patterns for Databricks and pipeline access, following standards set by engineering and compliance.

| | |
|---|---|
| **Compliance + engineering said** | No DB secrets in Git; managed identity + Key Vault. |
| **I did** | Configured Key Vault references and job identities per their standards. |

---

# LABS196 Innovations — Sr. Python Blockchain Developer (Feb 2025 – Present)

**Your level:** Senior IC on platform team (startup)  
**Above you:** Platform/staff engineers, platform leadership, compliance (GxP), security  
**Peers:** App teams, data pipeline owners, other platform engineers

---

## Bullet 1 — Multicloud EKS/AKS & Helm

**Resume:**
> Collaborated with platform and compliance teams as a Sr. Python Blockchain Developer to support a multicloud strategy across AWS and Azure, helping deploy and maintain Python-backed and Kubernetes workloads on EKS and AKS with Helm across Dev, Test, UAT, QA, and Production for regulated lab, research, and tokenization-adjacent platform services.

| | |
|---|---|
| **Platform leadership said** | Multicloud AWS + Azure is the strategy. All envs (Dev → Prod) must follow the env ladder. Compliance must sign off on GxP-validated paths. |
| **I did** | Deployed/maintained Python-backed and K8s workloads on EKS and AKS with Helm across all envs. |

---

## Remaining Labs196 bullets

Same ownership pattern as before: staff/platform engineers set GitOps, Rancher/Entra ID, Terraform/Ansible, observability, GxP retention, and on-call standards — you implement, operate, and improve hands-on.

---

# Quick comparison

| | **Finix196 Capital** | **LABS196 Innovations** |
|---|----------------------|-------------------------|
| **Title** | Data Science Specialist | Sr. Python Blockchain Developer |
| **Focus** | Python/Databricks capital analytics | Multicloud platform + Python/blockchain-adjacent services |
| **Cloud** | Azure-centric analytics | AWS + Azure |
| **Compliance flavor** | Capital/investor-adjacent data access | GxP / FDA-aligned |

---

# Interview tip

When asked "what did **you** do vs the team?":

> "At Finix196, product and compliance signed off metric definitions — I owned the Databricks/Python pipelines and quality gates. At LABS196 Innovations, staff engineers set GitOps and GxP rules — I own hands-on cluster, pipeline, and platform work."

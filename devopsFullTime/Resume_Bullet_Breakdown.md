# Resume Bullet Breakdown — Who Said What / What I Did

Line-by-line breakdown of every DevOps resume bullet for **Delta Dental** and **Labs196**.

Format per bullet:
- **Resume point** — exact bullet text
- **Who decided / directed** — who was above you, who set the rules
- **What I did** — your hands-on work in short

---

# Delta Dental — DevOps Engineer (Jan 2024 – Feb 2025)

**Your level:** Mid-level IC on platform team  
**Above you:** Platform manager/lead, senior DevOps engineers (incl. California), compliance, security  
**Peers:** Other DevOps engineers, app teams (claims, enrollment, portals)

---

## Bullet 1 — AKS production & 99.9% availability

**Resume:**
> Collaborated with a distributed platform team, including California-based engineers, to support production Azure Kubernetes Service (AKS) clusters running containerized claims and payor workloads behind Azure Application Gateway, helping maintain 99.9% availability for member eligibility and claims processing services.

| | |
|---|---|
| **Platform leadership / seniors said** | AKS is the production standard for claims and payor services. 99.9% availability is the SLA target for eligibility and claims paths. Application Gateway is the approved ingress. |
| **I did** | Kept prod AKS healthy day to day: checked cluster/node health, supported deploys, triaged incidents with CA + GA teammates, coordinated with app teams when claims/eligibility services broke. |

---

## Bullet 2 — Monitoring & MTTD 30 → 5 min

**Resume:**
> Contributed to centralized monitoring and alerting using Application Insights, Azure Monitor, and Grafana dashboards, integrated with Azure Front Door health probes and gateway metrics, supporting a team reduction in mean time to detect (MTTD) from 30 minutes to 5 minutes across claims adjudication and enrollment workflows.

| | |
|---|---|
| **Seniors / platform lead said** | We need one place to see claims and enrollment health. MTTD is too high — target ~5 min. |
| **I did** | Built/configured Grafana dashboards and alert rules, wired App Insights + Azure Monitor + Front Door/gateway metrics. Team outcome: MTTD dropped ~30 min → ~5 min. |

---

## Bullet 3 — Legacy → AKS migration, 40% utilization

**Resume:**
> Assisted in migrating legacy applications to cloud-native AKS on Azure, working with senior DevOps engineers to improve resource utilization by 40% for the member enrollment and provider portal platforms.

| | |
|---|---|
| **Senior DevOps said** | Move enrollment and provider portal off VMs to AKS. Right-size CPU/memory. |
| **I did** | Migrated workloads; right-sized requests/limits; tuned node pools with seniors. |

---

## Bullet 4 — Canary releases, 75% fewer incidents

**Resume:**
> Supported canary release rollouts through Azure DevOps pipelines with Application Gateway traffic splitting under senior guidance, contributing to a 75% reduction in deployment-related incidents for the member self-service portal.

| | |
|---|---|
| **Senior DevOps said** | Use canary via App Gateway — start at 10% traffic, watch Grafana/App Insights, promote or rollback. |
| **I did** | Supported pipeline stages and traffic weight changes under guidance. |

---

## Bullet 5 — DR RPO 10 / RTO 30

**Resume:**
> Helped automate backup and disaster recovery (DR) for Azure SQL and cloud-hosted data services, supporting team targets of RPO 10 minutes and RTO 30 minutes for critical claims transaction processing systems.

| | |
|---|---|
| **Leadership said** | Claims systems need aggressive RPO/RTO. Automate backup/DR. |
| **I did** | Backup workflows and runbooks for Azure SQL aligned to those targets. |

---

## Bullet 6 — HIPAA / Key Vault

**Resume:**
> Supported HIPAA-aligned security practices using Azure Key Vault for encryption and key rotation of member PHI and claims data at rest and in transit, following standards set by senior engineers and the compliance team.

| | |
|---|---|
| **Compliance + seniors said** | PHI/claims data must use Key Vault. Do not invent your own security model. |
| **I did** | Applied Key Vault in infra/pipeline configs per their standards. |

---

# Labs196 — Sr. DevOps Engineer (Feb 2025 – Present)

**Your level:** Senior IC on platform team  
**Above you:** Platform/staff engineers, compliance (GxP), security  

Same ownership pattern: staff/platform set GitOps, Rancher/Entra ID, Terraform/Ansible, observability, GxP retention, and on-call standards — you implement and operate.

---

# Quick comparison

| | **Delta Dental** | **Labs196** |
|---|------------------|-------------|
| **Title** | DevOps Engineer | Sr. DevOps Engineer |
| **Cloud** | Azure only | AWS + Azure |
| **Compliance** | HIPAA | GxP/FDA |

---

# Interview tip

> "Seniors and compliance set the standards — canary design, DR targets, HIPAA at Delta, GxP and GitOps rules at Labs196. My job was to implement, automate, monitor, and operate."

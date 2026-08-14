# Delta Dental — DevOps Engineer

**Jan 2024 – Feb 2025 · On-Site, GA**

---

## Company

Delta Dental is a **dental insurance and benefits** organization. Members, providers, and payors depend on digital services for **eligibility checks**, **claims processing**, **enrollment**, and **self-service portals**. Platform downtime directly impacts members waiting on claims status and providers verifying coverage — so **99.9% availability** on critical paths was a real target, not a slide deck number.

---

## My Role

I was on the **platform team** supporting production **Azure Kubernetes Service (AKS)** clusters for **healthcare workloads** — containerized **claims and payor services** behind **Azure Application Gateway**.

**I contributed to:**

- Production **AKS** cluster stability for claims, enrollment, and portal services
- **Observability** — Application Insights, Azure Monitor, Grafana dashboards
- **Canary releases** via **Azure DevOps** + Application Gateway traffic splitting
- **AKS migration** — legacy VM apps to cloud-native Kubernetes
- **DR/backup automation** for **Azure SQL** and cloud-hosted data services
- **HIPAA-aligned** security with **Azure Key Vault**
- **On-call** and incident response for production platform services

**Under senior guidance for:** canary rollout design, DR targets, and HIPAA control standards — I implemented and supported, not solo-owned policy.

**App teams owned:** application code, container images, and service-specific K8s manifests.

---

## Team


| Group                                                   | How we interact                                          |
| ------------------------------------------------------- | -------------------------------------------------------- |
| **Platform team** (GA + **California-based engineers**) | Distributed team; shared on-call, pipeline work, AKS ops |
| **Senior DevOps engineers**                             | Canary design, migration strategy, DR architecture       |
| **Application teams**                                   | Claims, enrollment, provider portal, member self-service |
| **Compliance**                                          | HIPAA requirements for PHI and claims data               |
| **Security**                                            | Key Vault standards, least-privilege access, encryption  |


Distributed team across **Georgia and California** — async coordination, shared runbooks, bridge calls for P0/P1 incidents.

---

## How Work Reaches Me

- **Azure DevOps** — pipeline failures, release requests, work items
- **Jira** — infra tasks, incidents, migration work
- **On-call alerts** — Azure Monitor, Application Insights, Grafana alert rules
- **Slack / Teams** — incident bridges with app teams

**Priority:** member-impacting production issues first (eligibility, claims processing, enrollment), then planned migrations and pipeline improvements.

**Triage flow:** alert → Application Insights / Grafana → Azure Monitor logs → Application Gateway / Front Door metrics → runbook → coordinate with app team → fix or rollback canary.

---

## Platform Stack


| Tool                          | Job                                                            |
| ----------------------------- | -------------------------------------------------------------- |
| **AKS**                       | Runs containerized claims, payor, enrollment, portal workloads |
| **Azure Application Gateway** | Ingress, TLS termination, **canary traffic splitting**         |
| **Azure Front Door**          | Global routing, health probes, edge availability               |
| **Azure DevOps**              | CI/CD pipelines — build, test, deploy to AKS                   |
| **Application Insights**      | App-level telemetry, distributed tracing, error tracking       |
| **Azure Monitor**             | Platform metrics, alerts, log aggregation                      |
| **Grafana**                   | Dashboards for claims adjudication and enrollment workflows    |
| **Azure Key Vault**           | Encryption keys, secrets for PHI/claims data                   |
| **Azure SQL**                 | Claims transaction and member data stores                      |


**Single cloud (Azure)** — unlike Labs196 multicloud. Everything runs in Azure-native services.

---

## Interview Shortcuts

### 30 seconds

> "DevOps Engineer on the platform team at Delta Dental — production AKS for healthcare claims and payor workloads behind Application Gateway. Azure DevOps for CI/CD with canary releases, Application Insights and Grafana for monitoring — we cut MTTD from 30 minutes to 5. Helped migrate legacy apps to AKS, automated Azure SQL DR with 10-minute RPO, and supported HIPAA-aligned Key Vault practices."

### Likely follow-ups


| Question                  | Hint                                                                                      |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| What is HIPAA here?       | PHI + claims data; Key Vault encryption, least privilege, compliance-set standards        |
| CI/CD tool?               | **Azure DevOps Pipelines** — CI and CD together, including canary stages                  |
| How does canary work?     | App Gateway splits traffic; Grafana/App Insights watch; promote or rollback weights       |
| MTTD improvement?         | App Insights tracing + Grafana dashboards + Front Door/Gateway health integration         |
| RPO/RTO?                  | **10 min / 30 min** for critical claims transaction systems                               |
| Delta vs Labs196?         | Delta = Azure-only, HIPAA, Azure DevOps canary. Labs196 = multicloud, GxP, Argo CD GitOps |

---

*Full deep-dive (CI/CD, canary, DR, STAR bullets) was restored for interview prep — see also `thisText.md` Additional work at Delta Dental and the DevOps resume bullets.*

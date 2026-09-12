# Delta Dental — Full Stack Engineer

**Jan 2024 to Jan 2025 · On-Site, GA**

---

## Company

Delta Dental is a **dental insurance and benefits** organization. Members, providers, and payors depend on digital services for **eligibility**, **claims**, **enrollment**, and **self-service portals**. If eligibility or claims is down, members wait and providers cannot verify coverage. **99.9% availability** on those paths was a real target.

This role is **full stack on Azure**, not DevOps-only and not a .NET shop story unless they ask about skills. Daily work was **Python FastAPI / Flask** and **Node.js REST**, **Angular** and **React** TypeScript portals, **AKS**, **HIPAA**, **OWASP**, reviews, and pairing on promotion.

**Single cloud: Azure.** No AWS on this job.

---

## My Role

I was a **Full Stack Engineer**, on-site in Georgia, on claims / enrollment / portal work with a distributed platform team (GA + California).

**I implemented and reviewed:**

- **Python FastAPI / Flask** and **Node.js REST APIs** for member eligibility and claims, with automated tests before **AKS** promotion
- **Angular** and **React.js TypeScript** features for member enrollment and provider self-service portals
- **Code reviews** and **design reviews**: OOAD, SOLID, **OWASP**, HIPAA-aligned secure coding with **Azure Key Vault** for PHI / claims in **Azure SQL**

**I helped with:**

- **Migration** of enrollment and provider portal stack (Angular, React, Python, Node) from legacy hosting to cloud-native **AKS**, about **40%** better resource utilization, API contracts kept
- **Canary** releases and **environment promotion** through **Azure DevOps**, **Terraform**, Git workflows, branching; about **75%** fewer deployment-related incidents on the self-service portal
- Monitoring: **Application Insights**, **Azure Monitor**, **Grafana**; **MTTD** from **30 minutes** to **5 minutes**
- **Root cause analysis** and **vulnerability assessments** with Risk and Compliance

**Under senior / platform guidance for:** canary design, DR targets, HIPAA control standards. I implemented and reviewed; I did not own enterprise HIPAA policy.

**I did not own alone:** AKS cluster platform as the sole owner, Front Door global design, or “I invented 99.9%.” Those were team targets I contributed to.

**No C# / ASP.NET Web API delivery on this job.** Resume lists those as skills. Here the APIs are Python and Node.

---

## The Story — Portals on Azure

Members check eligibility and claims. Providers use enrollment and self-service. We were moving **legacy hosted** apps onto **AKS** behind **Application Gateway** and **Front Door**, without breaking API contracts or UI routing.

```
Member / provider browser
        |
        v
Azure Front Door (health, edge)
        |
        v
Application Gateway (TLS, canary split)
        |
        v
AKS
  Angular / React portals
  Python FastAPI / Flask + Node REST
        |
        v
Azure SQL (claims / member data)
Azure Key Vault (secrets, keys for PHI)
```

**Why migrate:** better utilization (we saw about **40%**), repeatable deploys, same contracts so enrollment and provider routing did not break.

**Why canary:** cut blast radius. Azure DevOps + Gateway traffic split. Team saw about **75%** fewer deploy-related incidents on the member self-service portal.

**Why OWASP + HIPAA + Key Vault:** PHI and claims. Input validation, auth, logging in reviews. Secrets not in config. Risk and Compliance on vulnerability assessments.

---

## Team

| Group | How we interact |
| ----- | --------------- |
| **Platform team** (GA + California) | Pipelines, AKS, shared on-call style coordination |
| **Senior platform / DevOps** | Canary design, migration strategy |
| **App / portal engineers** | Eligibility, claims, enrollment, provider UI |
| **QA** | Regression on KYC-like portal paths and claims happy path |
| **Risk / Compliance** | HIPAA, vulnerability assessments |
| **Security** | Key Vault, least privilege |

On-site **Georgia**, async with California. Azure DevOps work items, Jira, Teams for incidents.

---

## How Work Reaches Me

- **Azure DevOps** — pipeline failures, release, PRs
- **Jira** — portal features, defects, migration tasks
- **Alerts** — Application Insights, Azure Monitor, Grafana
- **Risk / Compliance** — vulnerability findings to review in code

**Priority:** member-impacting eligibility / claims / enrollment first, then migration and pipeline work.

**Triage:** alert -> Insights / Grafana -> Gateway / Front Door metrics -> was it code, config, or canary -> fix or rollback with the app team.

---

## Platform Stack

| Tool | Job |
| ---- | --- |
| **Angular / React / TypeScript** | Enrollment and provider / member portals |
| **Python FastAPI / Flask, Node.js** | Eligibility and claims REST APIs |
| **AKS** | Containerized portal and API workloads |
| **Application Gateway / Front Door** | Ingress, TLS, canary, edge health |
| **Azure DevOps / Terraform / Git** | CI/CD, IaC, branching, promotion |
| **Application Insights / Azure Monitor / Grafana** | MTTD, RCA |
| **Azure Key Vault / Azure SQL** | Secrets and PHI / claims data |
| **OOAD, SOLID, OWASP** | Reviews and secure coding |

---

## What I Built and Improved

1. Eligibility / claims APIs (Python + Node) with tests before AKS promote
2. Angular / React TypeScript portal features; contracts kept through promotion
3. Reviews with OOAD, SOLID, OWASP, HIPAA + Key Vault
4. Helped migrate portals to AKS (~40% utilization)
5. Canary + Azure DevOps + Terraform (~75% fewer deploy incidents on that portal)
6. Monitoring that supported MTTD 30 min to 5 min; RCA; vulnerability assessments with Risk/Compliance

---

## Testing and How I Validated Changes

- API automated tests before AKS promotion
- Portal: routing still matches old contracts after migrate
- Canary: watch Gateway metrics; rollback if error rate spikes
- Security: Key Vault usage, no secrets in repo, OWASP checks in review (injection, auth, logging)
- RCA: Insights traces, not guesswork

---

## Why It Matters (this JD)

This is the **Azure + Angular + React + REST + HIPAA + reviews + promotion** story. Use it for: cloud (compute, networking, platform), CI/CD, Terraform, Git, environment promotion, OWASP, vulnerability assessments, RCA, OOAD/SOLID, working with Risk/Compliance. Pair with Labs196 for **AI agents**. Do not mix AWS into this job.

---

## Interview Shortcuts

### 30 seconds

> "Full Stack Engineer at Delta Dental, on-site Georgia, about a year. Member eligibility and claims APIs in Python FastAPI/Flask and Node, Angular and React TypeScript portals. We moved that stack to AKS on Azure behind Application Gateway and Front Door. I did reviews with OOAD, SOLID, OWASP, and HIPAA using Key Vault. I helped with canary and Azure DevOps promotion, monitoring, RCA, and vulnerability assessments with Risk and Compliance."

### 2 minutes

> "Delta Dental is dental insurance. If eligibility or claims is down, members and providers feel it. Target on those paths was 99.9% availability. Everything was Azure, not AWS.
>
> I implemented and reviewed Python and Node REST APIs for eligibility and claims, with tests before AKS promotion. I shipped Angular and React TypeScript features on enrollment and provider self-service without breaking routing or API contracts.
>
> The migration was legacy hosting to AKS. We kept service boundaries. Utilization improved about 40%. Canary through Azure DevOps and Application Gateway traffic splitting; the team saw about 75% fewer deploy-related incidents on the member self-service portal.
>
> I treated reviews as part of the job: OOAD, SOLID, OWASP, HIPAA, Key Vault for PHI in Azure SQL. Monitoring with Application Insights, Azure Monitor, Grafana supported MTTD going from 30 minutes to 5 minutes. When something broke I led RCA on the code or design side and worked vulnerability findings with Risk and Compliance.
>
> I was not the platform owner for the whole AKS estate. I was a full stack engineer on the portals and APIs, pairing with platform on promotion."

### STAR

**Migration**

- Situation: enrollment and provider portals on legacy hosting
- Task: help move to AKS without breaking contracts
- Action: keep Angular/React routing and Python/Node APIs stable; promote through Azure
- Result: ~40% utilization; same contracts
- Learning: migration success is “users still hit the same APIs,” not “we are on Kubernetes”

**Deploy safety**

- Situation: too many deploy-related incidents
- Task: safer promotion
- Action: canary, Azure DevOps, Terraform, branching
- Result: ~75% fewer deploy incidents on that portal
- Learning: traffic split plus rollback beats a big-bang Friday

**Security / HIPAA**

- Situation: PHI and claims in Azure SQL
- Task: reviews that actually catch issues
- Action: OWASP + HIPAA + Key Vault in design/code review; vulnerability assessments with Risk/Compliance
- Result: secrets and PHI handling had a bar, not heroics
- Learning: Key Vault and input validation are the story, not “we are HIPAA certified because of me”

**Detection**

- Situation: slow to notice portal/API issues
- Task: contribute to monitoring
- Action: Insights, Azure Monitor, Grafana
- Result: team MTTD 30 min to 5 min
- Learning: MTTD is a team metric; I contributed, I did not personally invent Azure Monitor

### Likely follow-ups

| Question | Hint |
| -------- | ---- |
| Title / dates? | Full Stack Engineer, on-site GA, Jan 2024 to Jan 2025 |
| AWS? | **No.** Azure only |
| C# / ASP.NET? | **Skills only.** This job is Python, Node, Angular, React |
| 99.9% / 40% / 75% / MTTD? | Team outcomes I contributed to; do not say “I alone” |
| Front Door vs Gateway? | Front Door = edge/health; Gateway = ingress, TLS, canary |
| vs Labs196? | Delta = Azure healthcare portals. Labs196 = product + AI agents, AWS and Azure |

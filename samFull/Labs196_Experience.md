# Labs196 — Sr. Full Stack Engineer / Technical Lead

**Feb 2025 to Present · Hybrid, TX**

---

## Company

Labs196 is a **real estate and finance technology** shop. The business sells regulated investment and property-related products. Sales, compliance, and ops need visibility into pipeline, KYC, and payments. Internally, product and ops also wanted to **automate messy loops**: find events, clean records, draft outreach, and keep a human in the loop before anything sends.

Two workstreams sat on the same team:

1. **Product platform** — client-facing sites and an internal Admin Portal (onboarding, KYC, payments, KPIs)
2. **AI agents / MCP** — manager agent, specialist agents, shared tool layer, human approval gates

Users of (1) are **prospects, sales, compliance**. Users of (2) are **internal**: product, ops, outreach, backend. Reliability and **guardrails** matter more than a clever prompt. A bad scrape can poison CRM-shaped data; a Gmail send without review is irreversible.

---

## My Role

I am a **Sr. Full Stack Engineer / Technical Lead**. I am a **working lead**, not a people manager. I report into / work **with product and architecture leads**. I own technical leadership on **assigned** AI and product workstreams: specs, reviews, critical-path code, and pairing with DevOps on promotion.

**I owned:**

- Technical leadership on assigned parallel workstreams: turn business needs into **technical specifications** for APIs and UI (with product and architecture leads)
- **Code reviews, design reviews, technical validations** so those workstreams stay on OOAD, SOLID, automated testing, coding standards, versioning, documentation
- **Manager agent** (Azure OpenAI **GPT-4o**) — plan, pick tools, route to specialists, human-in-the-loop gates
- **Shared Python / TypeScript tool layer** — search, scrape, DB, Gmail as callable tools with schemas and retries; **Hugging Face** extraction before MongoDB
- **MCP servers** and bots that extend LLM capabilities with custom tools, file systems, and APIs
- **Admin Portal** (React.js / Next.js TypeScript, Tailwind, Figma, RBAC) including KPI tracking and agent-run monitoring
- **Python microservices** and **Node.js REST APIs** over **MongoDB** and **Firebase**; **Stripe**, **HubSpot**, **Sumsub** with PCI-aligned secure coding

**I partnered on:**

- DevOps: **GitHub Actions**, Bitbucket, **Terraform**, Docker on **EKS / AKS**, **environment promotion** across **Dev, Test, UAT, Prod**
- Root cause analysis with **Prometheus** and **CloudWatch**
- Event Finder / Email Formation agent behavior with the team (I owned routing, tools, and the send gate)

**I did not own alone:** org-wide architecture sign-off, people management, product definition of “what counts as an event,” outreach copy standards, MongoDB schema sign-off (backend), KYC legal policy, or Stripe PCI program ownership.

---

## The Story — Two Workstreams

### Workstream A — Product platform

Prospects browse offerings, apply, pass KYC, pay, and get reviewed. Sales and compliance live in the Admin Portal.

```
Prospect lands on product site (Next.js)
        |
        v
Account (Firebase Auth -> JWT from Node API)
        |
        v
Catalog (MongoDB)
        |
        v
Application -> HubSpot deal/contact
        |
        v
KYC/AML (Sumsub SDK + webhooks)
        |
        v
Compliance review in Admin Portal (RBAC)
        |
        v
Payment (Stripe, server-side intents, PCI-aware)
        |
        v
MongoDB source of truth; Firebase for live UI state; HubSpot synced
        |
        v
Sales KPIs in Admin Portal
```

**Why this split:** MongoDB is the business record. Firebase is derived real-time UI state. Webhooks write MongoDB first. Admins get elevated JWT claims; users only see their own data. Stripe intents stay server-side so we do not widen PCI scope.

### Workstream B — Multi-agent / MCP

Product and ops wanted one “agent” to find events, clean data, and draft outreach. That is four jobs with different failure modes.

```
User / ops request
        |
        v
Manager agent (GPT-4o)     <- I owned this
  plan, pick tools, route
        |
        |-- Event Finder (GPT-4o-mini)
        |     search + scrape tools
        |     structured event list
        |
        |-- Data Refinement
        |     cleaner + HF field extraction
        |     DB tools -> MongoDB
        |
        +-- Email Formation (GPT-4o)
              Gmail drafts
              X  no send until manager / human approval
```

**Why a manager, not one mega-prompt:** discovery is cheap and noisy. Refinement must be schema-strict. Email must not send itself. MCP servers expose tools (file system, APIs) so agents do not invent side effects.

**Reliability:** structured tool I/O, retries, logs. Deterministic work (DB write, clean, scrape fetch) stays in Python/TS tools, not in prompts.

---

## Team

| Group | How we interact |
| ----- | --------------- |
| **Product / architecture leads** | Specs, scope, API and UI contracts; I am a working lead under them |
| **Product / ops** | What an event is; when a workflow is done |
| **Backend** | MongoDB / SQL schemas for refined records |
| **Outreach** | Email drafts; they review; I own the send gate |
| **DevOps** | CI/CD, Terraform, EKS/AKS, Dev/Test/UAT/Prod promotion |
| **QA / sales** | Portal defects, KPI needs, Jira |
| **Other engineers** | Reviews I lead; they add tools on the shared layer without rewriting manager prompts |

Hybrid **Texas**. Jira + Slack. PR reviews on APIs, UI, agent tools, pipelines.

---

## How Work Reaches Me

- **Jira** — features, agent routing bugs, portal defects, pipeline issues
- **Slack** — “finder returned junk,” “KYC webhook lag,” “UAT will not promote”
- **PR reviews** — I lead reviews on assigned workstreams
- **DevOps** — pipeline failures, environment triage in Dev/Test/UAT/Prod

**Priority:** anything that **writes to DB**, **moves money**, **sends email**, or **blocks promotion**. Prompt wording is later.

**Triage:** logs (tool name / correlation id) -> schema vs scrape vs manager mis-route vs deploy -> fix the **contract, tool, or pipeline**, then rerun the same case.

---

## Platform Stack

| Tool | Job |
| ---- | --- |
| **React.js / Next.js / TypeScript / Tailwind** | Product sites, Admin Portal, agent-run monitoring |
| **Node.js REST** | Integration hub: Sumsub, HubSpot, Stripe webhooks |
| **Python** | Microservices, agent tools, ETL-ish processing |
| **MongoDB / Firebase** | Source of truth vs live UI state |
| **Azure OpenAI GPT-4o / GPT-4o-mini** | Manager, email; finder |
| **Ollama / Hugging Face** | Local / extraction tools |
| **MCP servers** | Tools, files, APIs for agents |
| **Stripe / HubSpot / Sumsub** | Payments, CRM, KYC/AML |
| **EKS / AKS, Docker, Terraform** | Runtime and IaC |
| **GitHub Actions / Bitbucket** | CI/CD, promotion Dev -> Prod |
| **Prometheus / CloudWatch** | RCA |

No **C# / ASP.NET** delivery on this job. Those are resume **skills**, not this workstream.

---

## What I Built and Improved

1. Specs and technical leadership on assigned AI + product streams (with product and architecture leads)
2. Review bar: OOAD, SOLID, tests, versioning, docs
3. Manager agent + MCP/bots + human gates
4. Shared tool layer + HF extractor before MongoDB
5. Admin Portal + Figma-to-production UI with RBAC
6. Node + Python APIs; Stripe / HubSpot / Sumsub
7. Promotion path with DevOps across Dev, Test, UAT, Prod; RCA

---

## Testing and How I Validated Changes

- Portal: role checks (user vs admin), webhook HMAC, Stripe sandbox, KYC happy path with QA
- Agents: fixture URLs; schema reject vs write; manager must not call Gmail send on “find events”; approval gate: draft exists, send does not fire
- HF extractor: held-out snippets before wiring as a MongoDB-front tool
- Promote: pipeline green in Dev/Test/UAT before Prod; rollback playbook with DevOps

---

## Why It Matters (this JD)

This is **hands-on Technical Lead** work: parallel AI and product streams, reviews, REST APIs, React/Next, Azure OpenAI, cloud (EKS/AKS), CI/CD, promotion, RCA. It is **AI inside the product** (agents, MCP, LLMs) plus **delivery** (specs, quality, DevOps partner). It is not “I managed the org” and not “I only wrote prompts.”

---

## Interview Shortcuts

### 30 seconds

> "At Labs196 I am a Sr. Full Stack Engineer and Technical Lead, hybrid in Texas. Working lead, not a people manager. I work with product and architecture leads. I own technical leadership on assigned AI and product workstreams: specs, code and design reviews, the React/Next admin portal, Node and Python APIs with Stripe, HubSpot, and Sumsub, and a multi-agent setup where I owned the GPT-4o manager, the shared tool layer, MCP-style tools, and a human gate before Gmail send. I partner with DevOps on GitHub Actions, Terraform, EKS and AKS, and promotion across Dev, Test, UAT, and Prod."

### 2 minutes

> "Labs196 is real estate and finance tech. Two streams: a regulated onboarding platform, and internal agent automation.
>
> On the platform, prospects apply, pass Sumsub KYC, pay with Stripe, and land in HubSpot. I built React and Next TypeScript UIs including the Admin Portal from Figma, with RBAC. Node REST is the integration hub. Python microservices sit next to MongoDB as source of truth and Firebase for live UI state. Webhooks write MongoDB first.
>
> On AI, product wanted one agent to find events, clean data, and email. We split it. I owned the manager on GPT-4o: plan, pick tools, route. Mini model for finder with search and scrape tools. I built refinement with a Hugging Face extractor before MongoDB. Outreach drafts Gmail; I put a manager approval gate on send. Shared tools have schemas, retries, logs so other people can add a tool without rewriting prompts. MCP servers expose tools and files to those agents.
>
> I lead reviews on assigned streams so OOAD, SOLID, tests, and branching stay consistent. I am not the architecture org owner. When promotion or a pipeline breaks, I pair with DevOps and I have led RCA with Prometheus and CloudWatch."

### STAR

**Leadership without being the boss**

- Situation: parallel AI and product work, architecture lead already in place
- Task: technical leadership on assigned streams
- Action: specs with product; reviews; critical-path code; tool-layer pattern others can extend
- Result: streams ship with a consistent bar; I do not pretend I run the department
- Learning: working lead means contracts and reviews, not status meetings

**Ambiguity — Event Finder**

- Situation: “find relevant events” had no schema
- Task: usable output for later agents
- Action: event contract with product/ops; tools not a blob of text; refine before MongoDB
- Result: structured lists the manager can route
- Learning: output contract first, then tools, then prompts

**Irreversible GenAI**

- Situation: email agent could send
- Task: stop silent send
- Action: Gmail drafts only; manager/human approval gate
- Result: generate is not send
- Learning: put the gate in software, not in a prompt that says “please don’t send”

**Platform reliability**

- Situation: KYC/payments/auth are P0
- Task: triage without guessing
- Action: correlation ids, Mongo first then Firebase, webhook 200-fast + async process
- Result: you can tell auth vs integration vs deploy
- Learning: dual-db discipline prevents “Firebase was truth” incidents

### Likely follow-ups

| Question | Hint |
| -------- | ---- |
| Your title? | Sr. Full Stack Engineer / Technical Lead, hybrid TX, Feb 2025 to Present |
| People manager? | No. Working lead under product and architecture leads |
| What did you own? | Specs on assigned streams, reviews, manager agent, tool layer, MCP, Admin Portal, Node/Python APIs, integrations |
| GPT-4o vs mini? | 4o = manager + email. Mini = finder |
| MCP? | Servers that expose tools, files, APIs so agents do not invent side effects |
| C# / ASP.NET here? | **No.** Skills on the resume. This job is Python, Node, React, Next |
| Stripe / PCI? | Server-side intents; I do not claim I own the PCI program |
| Environments? | Dev, Test, UAT, Prod with DevOps |
| Labs196 vs Delta Dental? | Labs196 = product + AI agents, AWS and Azure. Delta = Azure dental portals, HIPAA, AKS migration |

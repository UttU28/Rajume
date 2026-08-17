# Reusable Prompt: Work Experience Story Generator

Use this prompt for **any** role or company. Fill in the `[PLACEHOLDERS]` at the bottom, then paste the full block into an AI chat or use it as your own writing guide.

---

## The Prompt (copy everything below this line)

You are helping me write a clear, interview-ready **work experience story** for one job. Write in **first person**, as if I am explaining my role to a hiring manager or senior engineer. Sound like a real practitioner — not a textbook, not marketing copy, not AI fluff.

### Output I need

Produce a structured narrative for **this one experience only**. Cover every section below. Use concrete details from the inputs I provide. If something is missing, say `[NEEDS DETAIL: …]` instead of inventing facts.

---

### 1. Company & Business Context
- What does the company do? Who are its customers or users?
- What industry is it in? (e.g., healthcare, fintech, lab/research, SaaS)
- What business problem does the product or platform solve?
- Why does infrastructure / engineering work matter to the business?

### 2. My Role & Scope
- My title, dates, location, and employment type (full-time, contract, hybrid, etc.)
- What I was **directly responsible for** vs what I **contributed to** or **supported**
- What systems, environments, or services fell in my scope (Dev/Test/UAT/Prod, regions, clouds, clusters, pipelines, etc.)

### 3. Team Shape & How We Work
- Team size and structure (platform, DevOps, app teams, QA, compliance, security, etc.)
- Who I reported to or paired with (staff engineers, leads, managers)
- How the team is organized (squads, on-call rotation, shared services, etc.)
- Daily/weekly rhythm (standups, sprint planning, incident reviews, change advisory boards, etc.)

### 4. How Work Gets to Me (Tickets & Prioritization)
- Where work comes from (Jira, ServiceNow, Azure DevOps, Slack, on-call pages, etc.)
- Types of work I handle (features, bugs, infra changes, incidents, compliance tasks, etc.)
- How tickets are prioritized (severity, SLA, P0–P3, compliance deadlines, etc.)
- How I pick up, triage, and close work

### 5. What I Build, Fix, and Improve
- Main projects or initiatives I owned or contributed to
- Problems I solved (with before/after where possible)
- Tools, platforms, or patterns I introduced or maintained
- Measurable outcomes (uptime, MTTD, deploy time, cost, incident reduction, compliance, etc.)

### 6. My Day-to-Day & Technical Workflow
- What a typical week looks like
- How I design, implement, review, and deploy changes
- Environments I touch and how changes flow through them
- IaC, CI/CD, GitOps, monitoring, secrets, networking — whatever applies to this role

### 7. Testing & Quality (Including My Own Pipelines)
- How the team tests changes before production (unit, integration, staging, UAT, QA sign-off)
- How **I** test my own work — especially **my own pipelines and infrastructure changes**
- Rollback, canary, blue-green, or validation gates I use
- How I verify a change is safe before and after deploy

### 8. Collaboration & Stakeholders
- Which teams I work with (app dev, QA, security, compliance, data, SRE, product, etc.)
- **How** we collaborate (design reviews, PR reviews, runbooks, incident bridges, CAB, etc.)
- Examples of cross-team problems I helped unblock

### 9. How My Work Fits the Bigger Picture
- Connect my tasks to business or user outcomes (reliability, compliance, speed, cost, safety)
- One paragraph: "If I weren't doing this, what would break or slow down?"
- Why this experience makes me credible for similar roles

### 10. Interview-Ready Summaries
At the end, give me:
- **30-second elevator pitch** for this role
- **2-minute "walk me through your experience at [Company]"** answer
- **3 STAR bullets** (Situation, Task, Action, Result) I can reuse in behavioral questions
- **5 likely follow-up questions** an interviewer might ask — with short answer hints

---

### Writing rules
- First person only ("I built…", "On my team…")
- Prefer specifics over buzzwords
- Include real tool names only if I provided them
- Show trade-offs and judgment, not just tool lists
- Keep each section readable — short paragraphs, bullets where helpful
- Do not repeat my resume bullet-for-bullet; tell the **story behind** the bullets
- Flag gaps with `[NEEDS DETAIL: …]` instead of guessing

---

### Inputs (fill these in before running the prompt)

**Company name:** [e.g., Labs196]

**Role title:** [e.g., Sr. DevOps Engineer]

**Dates:** [e.g., Feb 2025 – Present]

**Location / work model:** [e.g., Hybrid, Texas]

**Company description (what they do):**
[2–4 sentences]

**My main responsibilities:**
[Bullets or rough notes]

**Team structure & who I work with:**
[Names/roles optional; structure is enough]

**How I get work / tickets:**
[Jira, on-call, Slack, etc.]

**Key projects, systems, or pipelines I worked on:**
[List tools, clouds, services, repos]

**Testing & release process:**
[How QA, staging, and prod promotion work]

**How I test my own pipeline / infra changes:**
[Your actual process]

**Problems I solved & impact:**
[Metrics, incidents, improvements]

**Compliance, security, or regulatory context (if any):**
[e.g., GxP, HIPAA, SOC 2 — or "none"]

**Resume bullets for this role (paste for reference):**
[Paste from resume]

**Anything else I want included:**
[Optional — big incidents, promotions, tools you want emphasized]

---

## Example: Your Original Question (Corrected)

> Can we write a full story for my experience at Labs196 — what the company is about, what the team looks like, how and what I work on, how I get tickets, how we handle testing and updates, how I test my own pipeline, what I built and solved, which teams I collaborate with, and how my work connects to the bigger picture? I want this for **one experience only**, but I also want a **reusable prompt** I can use for any job on my resume.

That corrected version maps directly to the template above.

# LABS196 Innovations — Sr. Python Blockchain Developer

**Feb 2025 – Present · Hybrid, TX**

---

## Company

LABS196 Innovations is the **product / R&D** side of the Labs196 ecosystem (real estate, capital, and tokenization-adjacent work).

Two workstreams sat on the same team:

1. **Internal multi-agent automation** — find events, clean the records, draft outreach, keep a human in the loop before anything sends
2. **Tokenization / Web3 POCs** — Ethereum token standards, wallet/transaction paths, and Python datasets from on-chain activity for monitoring

Users are **internal**: product, ops, outreach, backend, engineering, and compliance reviewers. Reliability and **guardrails** matter more than a clever prompt. A bad scrape can poison CRM-shaped data; a Gmail send without review is irreversible; a token transfer rule that is wrong is a compliance problem.

---

## My Role

I am a **Sr. Python Blockchain Developer**. I am a senior IC, not a people manager. I owned the **Manager agent** and the **shared tool layer** for the multi-agent system, built the **Data Refinement** path, and did the **wallet / on-chain Python** work. Token POCs were written with engineering and compliance review — I did not invent transfer policy.

**I owned:**

- **Manager agent (GPT-4o)** — plan the task, pick tools, route work to specialist agents
- **Shared tool layer** — search, scrape, DB, cleaner, Gmail as callable functions with schemas, retries, and logs
- **Data Refinement agent** — DB + data-cleaner tools; structured records before they hit MongoDB / SQL
- **Hugging Face field extractor** — names, dates, venues, status from messy scrape/CRM text, used as a refinement tool
- **Web3 path** — Fireblocks + MetaMask (create, sign, transfer) and Python parsing of on-chain activity into monitoring datasets

**I built with the team:**

- **Event Finder (GPT-4o-mini)** — I wired **Google Search API** and **Selenium** so it returned structured event lists to the manager
- **Email Formation (GPT-4o)** — with outreach; I added **manager approval gates** so Gmail drafts could not send without review
- **Solidity POCs** — ERC-20, ERC-1404, ERC-3643 with review on mint/burn, transfer rules, and event schemas

**I did not own alone:** product definition of “what counts as an event,” outreach copy standards, MongoDB/SQL schema sign-off (backend), or compliance rules for token transfers.

---

## The Story — Multi-Agent Platform

Product and ops wanted to **automate a messy loop**: discover relevant events, get clean structured data, and draft outreach. The first request sounded like one agent. It was actually four jobs with different failure modes.

We designed specialist agents and a **Manager** that holds the plan:

```
User / ops request
        │
        ▼
Manager agent (GPT-4o)     ← I owned this
  plan, pick tools, route, wait for results
        │
        ├── Event Finder (GPT-4o-mini)
        │     Google Search API + Selenium scrape
        │     structured event list back to manager
        │
        ├── Data Refinement
        │     cleaner tools + HF field extraction
        │     write clean records via DB tools (MongoDB / SQL)
        │
        └── Email Formation (GPT-4o)
              Gmail API drafts
              ── X ── no send until Manager approval gate
```

**Why a manager instead of a single mega-prompt:** Event discovery is cheap and noisy (mini model + search/scrape). Refinement must be **schema-strict**. Email is **language-heavy** but must not send itself. The manager’s job is routing and contracts, not doing every tool call inside one prompt.

**The reliability problem:** if Event Finder passed loosely structured text, refinement guessed, and email hallucinated a date, one bad field could hit the database or a draft. I pushed **structured tool I/O**, retries, and logs, and kept **deterministic work in Python tools** (DB writes, cleaning, scrape fetch) instead of inside prompts.

---

## Workstream A — Agents, in the order we actually built them

### 1. Manager agent (GPT-4o) — I owned this

The manager interprets the request, decides which specialist runs, which tools are legal for that step, and how results flow. I treated it as an **orchestrator**, not a chatbot.

What I cared about:

- A **plan** the rest of the system can follow (find → refine → optional email)
- **Tool choice** from the shared layer, not ad-hoc API calls inside the prompt
- **Routing** — do not ask Email Formation to scrape; do not ask Event Finder to write MongoDB
- **Approval** — Gmail send is a manager-gated action, not an agent side effect

### 2. Event Finder (GPT-4o-mini) — I wired the tools

The team owned the agent behavior; I connected **Google Search API** and **Selenium** as tools. Mini model because this step is “search, open pages, extract a list,” not long reasoning.

Ambiguity we had to kill with product/ops:

- What **is** an event (name, date, venue, source, status — at minimum)
- Which sources are allowed
- How scrape failures look (timeout, login wall, junk HTML) so we do not invent events

Output was a **structured event list** back to the manager — not a paragraph.

### 3. Data Refinement — I built this agent

Scrape and CRM text is messy. Downstream agents and outreach cannot consume it raw. I built refinement around **DB tools** and **data-cleaner tools**, and sat with backend on **MongoDB / SQL schemas** so cleaned rows were actually insertable and queryable.

This is where the Hugging Face model plugged in (below). Writes go through tools with schemas — not “the LLM decided a collection name.”

### 4. Email Formation (GPT-4o) — with outreach; I added the gate

Outreach cared about tone and which business facts belong in a draft. I wired **Gmail API** for **drafts**, and I added a **manager approval gate**: generate ≠ send. Nothing left the mailbox without a review step.

That gate is the story for “how do you handle irreversible actions in GenAI.”

### 5. Shared tool layer — I owned this

Search, scrape, DB, cleaner, Gmail are **callable functions** with:

- **Schemas** for inputs/outputs (so agents cannot pass free-form sludge)
- **Retries** for flaky search/scrape/Gmail
- **Logs** so we can see which tool failed, with what payload

Other people can **add a tool** without rewriting the manager’s prompts. That is the leadership story: a pattern, not a hero prompt.

### 6. Hugging Face field extraction — I fine-tuned and plugged it in

Names, dates, venues, status from scrape + CRM text. A general LLM can extract fields, but it is expensive, inconsistent, and hard to test. I fine-tuned a **Hugging Face transformer** for those fields, then exposed it as a **refinement-agent tool** so structured fields existed **before** MongoDB writes.

---

## Workstream B — Tokenization and Web3

Same company, different risk: **on-chain behavior** and **custody**.

### Solidity POCs — ERC-20, ERC-1404, ERC-3643

I wrote Ethereum token POCs with **engineering and compliance review** on:

- **Mint / burn**
- **Transfer rules** (why 1404/3643 exist: restriction / identity-aware transfer, not “just a meme token”)
- **Event schemas** — what gets emitted so Python monitoring can parse it

I did not ship a mainnet product token by myself. The POC was to make standards **concrete** for the team: what a transfer restriction looks like in code, what we log, what compliance cares about.

### Fireblocks, MetaMask, Python monitoring

I built the **wallet and transaction path**: create, sign, transfer — **Fireblocks** for the controlled custody path, **MetaMask** for the interactive wallet path the team needed to demo and test.

Then I used **Python** to parse **on-chain activity** into datasets for **monitoring** — so the team could see what happened after a tx, not only that a UI button returned 200.

---

## Team


| Group | How we interact |
| ----- | --------------- |
| **Product / ops** | What an event is, routing between agents, when a workflow is “done” |
| **Backend** | MongoDB / SQL schemas so refined records are usable downstream |
| **Outreach** | Email Formation content; they review drafts; I own the send gate |
| **Engineering** | Token POC review — mint/burn, transfer rules, events |
| **Compliance** | Transfer restrictions and what must never auto-send or auto-transfer |
| **Other engineers** | Add tools on the shared layer without rewriting manager prompts |


Hybrid **Texas**. Shared Slack + Jira with product; schema reviews with backend; approval UX with outreach.

---

## How Work Reaches Me

- **Jira** — new tools, schema changes, agent routing bugs, token POC tasks
- **Slack** — “finder returned junk,” “draft sent the wrong venue,” scrape timeouts
- **PR reviews** — tool schemas, manager routing, Solidity, Fireblocks/Python parsers
- **Outreach / ops** — sample runs against real event pages and draft language

**Priority:** anything that can **write to DB** or **send email** or **move tokens** first. Prompt wording is later.

**Triage flow:** logs for the tool call → schema validation error vs scrape garbage vs manager mis-route → fix the **tool or contract**, not only the prompt → rerun the same event URL / same request.

---

## Platform Stack


| Tool | Job |
| ---- | --- |
| **Python** | Agents, tools, refinement, on-chain parsers |
| **GPT-4o** | Manager; Email Formation |
| **GPT-4o-mini** | Event Finder (search/scrape extraction) |
| **Google Search API** | Discovery tool for Event Finder |
| **Selenium** | Page scrape tool |
| **MongoDB / SQL** | Clean records after refinement (backend schemas) |
| **Gmail API** | Drafts only until manager approval |
| **Hugging Face / Transformers** | Field extraction tool on the refinement path |
| **Solidity / Ethereum** | ERC-20, ERC-1404, ERC-3643 POCs |
| **Fireblocks / MetaMask** | Create, sign, transfer |
| **Git / Bitbucket or GitHub, Jira** | Code review and tickets |


---

## Tool Layer vs Prompts (design stance)

Interviewers will poke this. My stance, with a real disagreement we resolved with **failure cases**:

- **LLM:** language, planning, “which specialist next”
- **Python tools:** search, scrape, clean, DB write, Gmail draft/send, HF extract

If validation, formatting, and writes live only in prompts, you cannot test them, you cannot log a bad payload cleanly, and two agents will drift. We moved those jobs into **callable tools**. Logs and retries got better; outputs got more predictable.

---

## What I Built & Improved

1. **Manager agent (GPT-4o)** — plan, tool pick, route to specialists
2. **Event Finder tools** — Google Search API + Selenium, structured lists back to the manager
3. **Data Refinement agent** — cleaner + DB tools; schemas with backend
4. **Email Formation + approval gate** — Gmail drafts; no send without manager review
5. **Shared tool layer** — schemas, retries, logs; others add tools without rewriting prompts
6. **HF extractor** — names/dates/venues/status as a refinement tool before MongoDB
7. **Solidity POCs** — ERC-20 / 1404 / 3643 with mint/burn, transfer rules, events
8. **Fireblocks + MetaMask + Python monitoring datasets** from on-chain activity

---

## Testing & How I Validated Changes

**Agents**

- Fixture pages and known event URLs — same scrape twice should not invent new fields
- Schema validation on tool I/O; reject or retry instead of writing junk
- Manager routing tests: a “find events” request must not call Gmail send
- Approval gate: draft exists, send does not fire without the review step
- Logs: tool name, latency, retry count, payload shape (not secrets)

**HF extractor**

- Held-out scrape/CRM snippets with labeled names, dates, venues, status
- Compare extractor vs regex/LLM-only on the messy cases we actually saw
- Only then wire it as a tool in front of MongoDB

**Tokens / wallets**

- Test network / POC environment — not “try it on mainnet”
- Compliance/engineering review of transfer restriction behavior
- Python parser: given a known tx/event log, dataset row matches (mint, transfer, restriction hit)
- Fireblocks vs MetaMask: same intended action, two custody paths, both logged

**Rollback:** revert the tool or routing change; Gmail stays on drafts; token POCs stay off production rails.

---

## Why It Matters

This role is **GenAI as software**: orchestration, contracts, observability, and human gates — plus **tokenization** work that has to survive compliance review. If the manager routes badly, the whole chain is wrong. If tools have no schemas, MongoDB fills with garbage. If email has no gate, outreach becomes an incident. If token events are not parseable, monitoring is theater.

That is why Senior Data / GenAI interviews should hear **LABS196** as: Manager + tools + refinement + approval, then ERC/Fireblocks as the blockchain half — not as “I wrapped GPT.”

---

## Interview Shortcuts

### 30 seconds

> "Sr. Python Blockchain Developer at LABS196 Innovations. I owned the Manager agent in a Python multi-agent workflow — GPT-4o plans, picks tools, and routes to specialists. I also owned the shared tool layer: search, scrape, DB, cleaner, Gmail, with schemas, retries, and logs. I built refinement, including a Hugging Face extractor, added a manager approval gate before Gmail send, and did Ethereum token POCs plus Fireblocks/MetaMask and Python on-chain monitoring datasets."

### 2 minutes

> "LABS196 Innovations is internal product and R&D — event-to-outreach automation and tokenization POCs. Product and ops wanted to find events, clean the data, and draft email. We did not put that in one prompt.
>
> I owned the Manager agent on GPT-4o: it plans the work, chooses tools, and routes to specialists. Event Finder uses GPT-4o-mini; I wired Google Search API and Selenium so it returned a structured event list. I built the Data Refinement agent with cleaner and DB tools and aligned MongoDB/SQL schemas with backend. Outreach and I did Email Formation on GPT-4o with Gmail drafts; I added a manager approval gate so nothing sent without review.
>
> The shared tool layer is the part I care about most: callable functions, schemas, retries, logs. Other engineers can add tools without rewriting manager prompts. Deterministic work stays in Python; the model does language and routing. I also fine-tuned a Hugging Face transformer for names, dates, venues, and status and used it as a refinement tool before MongoDB.
>
> On the blockchain side I wrote Solidity POCs for ERC-20, ERC-1404, and ERC-3643 with engineering and compliance on mint, burn, transfer rules, and events. I built create/sign/transfer with Fireblocks and MetaMask and parsed on-chain activity in Python for monitoring datasets."

### STAR bullets

**Challenging project / architecture — multi-agent reliability**

- *Situation:* Specialists for find, refine, email; manager had to route without passing sludge
- *Task:* Own Manager + tool layer
- *Action:* Structured tool schemas, retries, logs; DB/clean/scrape as Python tools; Gmail behind approval
- *Result:* Workflow you can debug; one bad scrape does not silently become a send
- *Learning:* Reliable GenAI is software engineering + guardrails, not only the model

**Ambiguity — Event Finder**

- *Situation:* “Find relevant events” had no schema
- *Task:* Make finder output usable downstream
- *Action:* Event contract (name, date, venue, source, status); Search API + Selenium tools; pass through refinement before later steps
- *Result:* Structured lists the manager can route; fewer invented events
- *Learning:* Define the output contract first, then tools, then prompts

**Leadership — shared tool layer**

- *Situation:* Each agent was going to integrate search/Gmail/DB differently
- *Task:* One reusable tool surface
- *Action:* Callable functions + schemas + retries + logs; manager prompts stay stable
- *Result:* Others add tools without rewriting orchestration
- *Learning:* Technical leadership is patterns that de-risk the team

**Learning — tokenization / Web3**

- *Situation:* Needed Solidity, ERC-20/1404/3643, Fireblocks, MetaMask quickly
- *Task:* Become useful on token + wallet flows
- *Action:* Learn lifecycle first; small POCs (mint/burn/restrictions/events); then wallet path; Python monitoring datasets
- *Result:* Team had concrete POCs and on-chain datasets, not only slides
- *Learning:* Understand the system, build a small path, then add compliance and failure handling

**Collaboration — cross-team contracts**

- *Situation:* Product, backend, outreach, compliance all touch the same workflow
- *Task:* Keep interfaces explicit
- *Action:* Schema with backend; routing with product/ops; approval with outreach; token review with engineering/compliance
- *Result:* Fewer “whose bug is this” loops
- *Learning:* Clear in/out contracts make cross-team work possible

### Likely follow-ups


| Question | Hint |
| -------- | ---- |
| What is LABS196 Innovations? | Product/R&D in the Labs196 ecosystem — **multi-agent automation** and **tokenization / Web3 POCs** |
| Your title? | **Sr. Python Blockchain Developer**, hybrid TX, Feb 2025 – Present |
| What did you own? | Manager agent, shared tools, Data Refinement, HF extractor, Fireblocks/MetaMask + Python on-chain datasets |
| GPT-4o vs mini? | 4o = manager + email (planning/language). Mini = finder (search/scrape extraction) |
| Why tools not prompts? | Testable, logged, retries; DB writes and cleaning stay deterministic |
| Why approval gates? | Gmail send is irreversible; drafts are cheap; manager (human) reviews |
| Event schema? | Name, date, venue, source, status — agreed with product/ops |
| HF vs GPT for fields? | Extractor is cheaper/testable for names/dates/venues/status; GPT still routes and writes email |
| ERC-1404 vs 3643? | Both are about **restricted / compliant transfer**, not vanilla ERC-20; talk mint/burn, transfer rules, events you implemented in the POC — do not lecture the spec if they want your code path |
| Fireblocks vs MetaMask? | Fireblocks = controlled custody path; MetaMask = user/wallet path; I built create/sign/transfer on both as the team needed |
| Did you send tokens to production? | **POCs + monitoring datasets**, with engineering/compliance review — do not oversell mainnet |
| LABS196 vs Finix196? | LABS196 = **multi-agent + tokens**. Finix196 = **RAG on finance/tokenization docs** |

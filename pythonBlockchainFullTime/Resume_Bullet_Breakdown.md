# Resume Bullet Breakdown — Who Said What / What I Did

Line-by-line breakdown of every resume bullet for **Finix196 Capital** and **LABS196 Innovations**.

Aligned with:

- `Utsav Chaudhary Resume.pdf` / `.tex` in this folder
- `Senior_Data_GenAI_Behavioral_Interview_Guide.pdf`
- `Finix196_Capital_Experience.md`
- `LABS196_Innovations_Experience.md`

Format per bullet:

- **Resume point** — exact bullet text
- **Who decided / directed** — who was above you, who set the rules
- **What I did** — your hands-on work in short

When asked “what did **you** do vs the team?”, use the tables.

---

# Finix196 Capital — Data Science Specialist (Jan 2024 – Feb 2025)

**Your level:** Mid-level IC on data / GenAI (retrieval)  
**Above you:** Support leads and document owners (what is in-scope and on-policy); engineering for where services run  
**Peers:** Frontend engineer on the chat UI; support as evaluators

---

## Bullet 1 — RAG QnA / owned retrieval

**Resume:**

> Worked with internal support and document owners on a RAG QnA tool for finance and tokenization docs. I owned the retrieval pipeline so the team could ask questions instead of digging through folders.

| | |
|---|---|
| **Support / document owners said** | We need answers from finance and tokenization PDFs — stop hunting folders. These files are source of truth. |
| **I did** | Owned retrieval end to end so questions hit the corpus and came back with grounded answers, not a folder path. |

**Story hook:** business problem first (search), then “I owned retrieval,” not “I built ChatGPT.”

---

## Bullet 2 — Python ingestion

**Resume:**

> Wrote Python ingestion jobs (chunking, metadata, embeddings, vector DB upserts) and aligned doc types and tags with the people who owned the source PDFs.

| | |
|---|---|
| **Document owners said** | These are the PDF types and tags (policy vs offering vs process, etc.). This file superseded that one. |
| **I did** | Wrote the Python jobs: split, attach their metadata, embed, upsert. Ingestion matched **their** taxonomy. |

**Story hook:** metadata is a contract with owners, not a field you invented in a notebook.

---

## Bullet 3 — Query flow + sample review

**Resume:**

> Implemented query flow (embed question, cosine similarity / ANN, top-k, LLM answer with citations) as the core DS piece, then reviewed sample answers with support before we widened access.

| | |
|---|---|
| **Support said** | Show citations. We will not roll this out until sample answers look right. |
| **I did** | Implemented embed → ANN/cosine → top-k → LLM + citations. Sat on sample answers **before** wider access. |

**Story hook:** evaluation gate before rollout; citations make retrieval inspectable.

---

## Bullet 4 — Document refresh

**Resume:**

> Automated document refresh in Python (new files, re-chunk, re-embed, upsert) so ops did not have to rebuild the index by hand when policies changed.

| | |
|---|---|
| **Ops said** | Policies change. We cannot page engineering every time a PDF is replaced. |
| **I did** | Python refresh: detect new/changed files → re-chunk → re-embed → upsert. Ops keeps the index current. |

**Story hook:** stale index is a silent production bug in RAG.

---

## Bullet 5 — Chat UI / FastAPI split

**Resume:**

> Built the chat UI in Node.js with a Python/FastAPI backend, pairing with another engineer on the frontend while I owned retrieval, ranking, and answer generation.

| | |
|---|---|
| **Frontend engineer + I agreed** | Node.js for chat chrome; FastAPI for retrieve / rank / generate. |
| **I did** | FastAPI path (retrieval, ranking, generation). Paired on Node.js UI — I did **not** solo the whole frontend. |

**Story hook:** credit the pair; keep ownership on the DS service.

---

## Bullet 6 — Retrieval tuning / “wrong doc”

**Resume:**

> Tuned chunk size, overlap, metadata filters, and top-k with support feedback so answers stayed on-policy and fewer tickets came back as "wrong doc."

| | |
|---|---|
| **Support said** | This answer is from the wrong document / old policy. |
| **I did** | Grouped failures (chunk vs filter vs top-k vs stale). Tuned those knobs on the **same** examples. Fewer wrong-doc tickets. |

**Story hook:** the “more context made it worse” mistake lives here. Precision over dumping neighbors into the window.

---

# LABS196 Innovations — Sr. Python Blockchain Developer (Feb 2025 – Present)

**Your level:** Senior IC (startup / R&D) — orchestration, tools, refinement, token POCs  
**Above you:** Product/ops (what the workflow is), backend (schema sign-off), outreach (copy + draft review), engineering + compliance (token rules)  
**Peers:** Other engineers adding tools; specialist-agent owners

---

## Bullet 1 — Multi-agent design / Manager agent

**Resume:**

> Partnered with product and ops to design a multi-agent Python workflow. I owned the Manager agent (GPT-4o) that plans tasks, picks tools, and routes work to specialist agents.

| | |
|---|---|
| **Product / ops said** | Automate find → clean → outreach. Here is what “done” means for a run. |
| **I did** | Helped design the specialist split. **Owned** the GPT-4o Manager: plan, pick tools, route. |

**Story hook:** you own orchestration, not every specialist’s prompt.

---

## Bullet 2 — Event Finder tools

**Resume:**

> Worked with the team on an Event Finder agent (GPT-4o-mini). I wired Google Search API and Selenium tools so it could scrape pages and hand structured event lists back to the manager.

| | |
|---|---|
| **Team / product said** | Finder uses mini; it should return events, not essays. Here is what qualifies as an event. |
| **I did** | Wired **Google Search API** and **Selenium** as tools. Structured lists back to the manager — I did not claim I solo-invented the finder agent. |

**Story hook:** ambiguity → event schema (name, date, venue, source, status) → tools → structured output.

---

## Bullet 3 — Data Refinement / schemas

**Resume:**

> Built the Data Refinement agent (DB and data cleaner tools) while coordinating with backend on MongoDB/SQL schemas so cleaned records were usable by later agents.

| | |
|---|---|
| **Backend said** | These collections/tables and fields are what downstream can read. Do not invent a parallel schema. |
| **I did** | Built refinement: **cleaner + DB tools**. Coordinated so writes matched MongoDB/SQL contracts. |

**Story hook:** refinement is a data-quality agent, not “another GPT.”

---

## Bullet 4 — Email Formation / approval gate

**Resume:**

> Collaborated with outreach on an Email Formation agent (GPT-4o) and Gmail API drafts. I added manager approval gates so nothing sent without a review step.

| | |
|---|---|
| **Outreach said** | Drafts must sound like us and include the right business facts. We review before anything sends. |
| **I did** | Gmail **drafts** via API. **Manager approval gate** — generate is not send. |

**Story hook:** irreversible actions get a human/manager gate. This is the guardrails answer.

---

## Bullet 5 — Shared tool layer

**Resume:**

> Owned the shared tool layer (search, scrape, DB, cleaner, Gmail) as callable functions with schemas, retries, and logs so the rest of the team could add tools without rewriting agent prompts.

| | |
|---|---|
| **Team needed** | One way to call search/scrape/DB/Gmail — not a copy-paste integration per agent. |
| **I did** | **Owned** the tool layer: functions, schemas, retries, logs. Others add tools; manager prompts stay stable. |

**Story hook:** technical leadership without a manager title. Also the “logic in tools vs prompts” disagreement.

---

## Bullet 6 — Hugging Face extractor

**Resume:**

> Fine-tuned a Hugging Face transformer for field extraction (names, dates, venues, status) from messy scrape and CRM text, then plugged it in as a refinement-agent tool before data hit MongoDB.

| | |
|---|---|
| **Refinement needed** | Stable fields from messy text before DB write — not a one-off prompt per row. |
| **I did** | Fine-tuned HF for those four field groups. Exposed it as a **tool** on the refinement agent, **before** MongoDB. |

**Story hook:** ML where extraction must be testable and cheap; LLM still used for routing and email.

---

## Bullet 7 — Solidity token POCs

**Resume:**

> Wrote Solidity token POCs on Ethereum for ERC-20, ERC-1404, and ERC-3643 with engineering and compliance review on mint/burn, transfer rules, and event schemas.

| | |
|---|---|
| **Engineering / compliance said** | POC these standards. Mint/burn, transfer restrictions, and events must be reviewable. You do not set legal policy. |
| **I did** | Wrote the Solidity POCs. Walked mint/burn, transfer rules, and event schemas through their review. |

**Story hook:** 1404/3643 exist for **restricted transfer**, not for flexing standard names. POC + review, not “I launched a security token.”

---

## Bullet 8 — Fireblocks / MetaMask / on-chain datasets

**Resume:**

> Built the Web3 wallet and transaction path with Fireblocks and MetaMask (create, sign, transfer) and used Python to parse on-chain activity into datasets the team used for monitoring.

| | |
|---|---|
| **Team needed** | A path to create, sign, transfer — custody (Fireblocks) and wallet (MetaMask) — and to **see** what landed on-chain. |
| **I did** | Built that path. Python parsers → monitoring **datasets** from activity, not only a UI success toast. |

**Story hook:** learn the tx lifecycle, then POCs, then monitoring data. Two wallet paths, one parsing job.

---

# Quick comparison

| | **Finix196 Capital** | **LABS196 Innovations** |
|---|----------------------|-------------------------|
| **Title** | Data Science Specialist | Sr. Python Blockchain Developer |
| **Dates** | Jan 2024 – Feb 2025 · On-site TX | Feb 2025 – Present · Hybrid TX |
| **Focus** | RAG on finance / tokenization **docs** | Multi-agent **tools** + Ethereum **token/wallet** POCs |
| **You owned** | Retrieval: ingest, index, query, citations, refresh, FastAPI rank/generate | Manager agent, tool layer, refinement, HF extractor, Fireblocks/MetaMask + on-chain Python datasets |
| **Team owned / directed** | Source PDFs, on-policy bar, most Node.js chrome | Event definition, outreach copy, DB schema sign-off, token policy |
| **Core models** | Embeddings + LLM-with-citations | GPT-4o (manager, email), GPT-4o-mini (finder), HF extractor |
| **Irreversible action** | Stale/wrong policy answer | Gmail send; token transfer |
| **Eval / quality** | Support gold questions; wrong-doc tickets | Tool schemas, logs, approval gate, labeled extraction fields |

---

# Interview tip

When asked "what did **you** do vs the team?":

> "At Finix196, document owners and support decided which PDFs were source of truth and whether an answer was on-policy. I owned the retrieval pipeline — chunking, embeddings, vector search, top-k, citations, refresh, and the FastAPI generate path — and I paired on the Node.js chat UI. At LABS196, product and ops defined the workflow, backend signed schemas, and outreach reviewed drafts. I owned the GPT-4o Manager, the shared tool layer, Data Refinement, the Hugging Face extractor, the Gmail approval gate, and the Fireblocks/MetaMask plus Python on-chain monitoring path."

**Best story order (from the behavioral guide):** LABS196 multi-agent → Finix196 RAG → then older roles if needed.

**GenAI answers:** talk data quality, evaluation, logs, schemas, and human gates — not only prompts and model names.

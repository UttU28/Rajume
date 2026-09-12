# Finix196 Capital — Data Science Specialist

**Jan 2024 – Feb 2025 · On-Site, TX**

---

## Company

Finix196 Capital is a **financial services** firm focused on **real-world asset (RWA) tokenization** — real estate and capital-markets products. Advisors, support, ops, and document owners live in a pile of **finance and tokenization PDFs**: offering docs, policy memos, onboarding rules, token-transfer restrictions, and internal process notes.

The business problem was not “build a chatbot.” People were **searching folders** to answer the same questions: *which policy applies, what does this clause say, which version is current?* Wrong or stale answers create support tickets and compliance risk. The job was to turn that document set into a **retrievable, citable Q&A path**.

This role is **data / GenAI work on documents**: Python ingestion, retrieval, and a cited Q&A path for internal support and ops.

---

## My Role

I was the **Data Science Specialist** on an internal **RAG QnA** tool. I owned the **retrieval pipeline** end to end: how documents got into the index, how a question found the right chunks, and how the LLM answered **with citations**.

**I owned:**

- **Python ingestion** — chunking, metadata tagging, embeddings, vector-store upserts
- **Query path** — embed the question, cosine similarity / ANN, top-k, LLM answer with citations
- **Document refresh** — new or changed files → re-chunk, re-embed, upsert (no manual index rebuild)
- **Retrieval quality** — chunk size, overlap, metadata filters, top-k, reviewed with support
- **FastAPI retrieval/answer service** — ranking and generation behind the chat UI

**I paired on:**

- **Chat UI** — Node.js frontend with another engineer; I owned the Python/FastAPI backend
- **Doc taxonomy** — types and tags with the people who owned the source PDFs
- **Access rollout** — sample-answer review with support before we widened who could use it

**I did not own alone:** which documents were in-scope, policy sign-off, or product UX for the chat shell. Support and document owners decided what “on-policy” meant; I made retrieval match that.

---

## The Story — How This Work Happened

Internal support and ops were the first users. They knew the documents but could not keep every clause in their head, and folder search failed when a question spanned two PDFs or an old version sat next to a new one.

We started from the **output contract**, not the model: a useful answer had to (1) come from the right document type, (2) cite the chunk it used, and (3) stay current when a policy PDF changed. That is why I treated this as a **data/retrieval system** with an LLM on top, not as a prompt demo.

First I sat with document owners and tagged source PDFs by type (policy, offering, process, tokenization rules). Those tags became **metadata filters** later. Then I wrote the Python ingestion jobs: split text, attach metadata, embed, upsert. Only after a small index existed did we wire the query flow and a thin chat UI.

When support started asking real questions, the first failure mode was **wrong document**, not a “dumb model.” That is the loop I ran for the rest of the engagement: collect the ticket, find whether chunking, filters, or top-k caused it, change one thing, retest the same examples.

---

## Team


| Group | How we interact |
| ----- | --------------- |
| **Internal support** | Real questions, “wrong doc” tickets, sample-answer review before wider access |
| **Document owners** | Which PDFs are source-of-truth, doc types, tags, when a file is superseded |
| **Ops** | Refresh when policies change; they should not rebuild the index by hand |
| **Frontend engineer** | Node.js chat UI; I owned FastAPI retrieval, ranking, and generation |
| **Engineering / infra** | Where the vector store and FastAPI service ran; access to source files |


On-site in **Texas** — short loop with support: sit with a bad answer, open the cited chunk, decide if retrieval or the source PDF was the problem.

---

## How Work Reaches Me

- **Jira** — ingestion bugs, new doc types, retrieval quality tickets
- **Support tickets / Slack** — “this answer cited the wrong policy”
- **Document owners** — new or replaced PDFs that need a refresh run
- **PR reviews** — Python ingest/query changes before they hit the shared index

**Priority:** wrong or stale answers on live questions first, then new document types, then UI polish.

**Triage flow:** ticket → look at the question, retrieved chunks, and citations → decide chunking vs metadata filter vs top-k vs stale index → change one retrieval knob → rerun the same examples with support.

---

## Platform Stack


| Tool | Job |
| ---- | --- |
| **Python** | Ingestion, chunking, metadata, embeddings, refresh jobs |
| **Vector store** | Embedded chunks + metadata; cosine / ANN search |
| **Embeddings** | Document chunks and user questions in the same space |
| **LLM** | Answer generation grounded in retrieved chunks, with citations |
| **FastAPI** | Query API: retrieve → rank → generate |
| **Node.js** | Chat UI (paired with another engineer) |
| **Source PDFs** | Finance and tokenization docs owned by support / document owners |


---

## Where Data Flows

```
Finance / tokenization PDFs (owners + support)
        │
        ▼
Python ingestion
  split into chunks
  attach metadata (doc type, tags, source, version)
  embed chunks
  upsert into vector store
        │
        ├── scheduled / on-change refresh
        │     new file → re-chunk → re-embed → upsert
        │
        ▼
User question (Node.js chat)
        │
        ▼
FastAPI query path
  embed question
  cosine similarity / ANN
  metadata filters
  top-k chunks
  LLM answer + citations
        │
        ▼
Support review of sample answers
  tune chunk size, overlap, filters, top-k
```


| Layer | Where | Who owns |
| ----- | ----- | -------- |
| Source PDFs | Shared doc stores | Document owners + support |
| Ingestion + refresh | Python jobs | Me (DS) |
| Vector index | Vector store | Me (retrieval) + infra for hosting |
| Query + generation | FastAPI | Me |
| Chat UI | Node.js | Pair: frontend engineer + me on API contract |
| “On-policy” sign-off | Sample reviews | Support + document owners |


---

## Core Deliverable — RAG QnA

**Problem:** teams spent too long digging through finance and tokenization folders; answers were slow and sometimes from the wrong file.

**What I built:**

1. **Ingestion** — Python jobs that chunk, tag, embed, and upsert
2. **Retrieval** — embed question → ANN / cosine → filtered top-k
3. **Generation** — LLM answer with citations back to source chunks
4. **Refresh** — new/changed files re-indexed without a hand rebuild
5. **Chat path** — Node.js UI talking to FastAPI
6. **Tuning loop** — support examples → chunk/overlap/filter/top-k changes

**Result:** people could **ask questions against the document set** instead of searching folders. When a policy PDF changed, ops ran refresh instead of paging engineering to rebuild the index. Fewer tickets came back as “wrong doc” after we tightened retrieval with support.

---

## Retrieval Quality (the real DS work)

Early assumption: **more chunks in context = better answers.** In practice, semantically similar but **wrong** documents entered the window and the LLM sounded confident on the wrong policy.

I sat with support on those cases and grouped them:

- **Chunking** — clause split across chunks, or chunk too big and mixed topics
- **Metadata** — question was about tokenization rules but a generic finance FAQ ranked in
- **Top-k** — extra neighbors added noise
- **Stale index** — new PDF landed, old embedding still ranked

I changed **one** of those at a time and retested the **same** questions. Precision beat “more context.” That is the lesson I use in interviews: in RAG, a lot of “model quality” is retrieval quality.

**What I tuned with support:**

- Chunk size and overlap
- Metadata filters (doc type / tags)
- Top-k
- Whether a citation pointed at a chunk a human would actually open

---

## Document Refresh

Without automation, a new or edited policy meant someone had to rebuild parts of the index by hand — or users kept getting yesterday’s clause.

I wrote a Python workflow:

- Detect new or changed files
- Re-chunk and re-embed those files
- Upsert into the vector store (replace stale vectors for that source)

Ops could keep knowledge current without an engineering rebuild. That mattered because tokenization and finance policies **do** change; a frozen index is a silent failure.

---

## Chat UI and Service Split

```
Node.js chat UI  ──REST──►  Python FastAPI
                              │
                              ├── embed query
                              ├── retrieve + filter + top-k
                              └── LLM generate + citations
```

I paired on the frontend so the UI showed **citations** and enough source context for support to distrust a bad answer. I owned retrieval, ranking, and generation — that is the DS piece. The other engineer owned most of the chat chrome.

We did **not** widen access until support had reviewed a set of sample questions and we had fixed the obvious wrong-doc cases.

---

## What I Built & Improved

1. **Retrieval pipeline** — ingestion through cited answers, owned by me
2. **Python ingest jobs** — chunking, metadata, embeddings, upserts aligned with PDF owners
3. **Query flow** — cosine / ANN, top-k, LLM + citations
4. **Refresh automation** — re-chunk / re-embed / upsert on file change
5. **FastAPI + Node.js chat** — I owned the backend; paired on UI
6. **Evaluation loop** — support “wrong doc” tickets → targeted retrieval tuning

---

## Testing & How I Validated Changes

**Not enough:** “the API returned 200.”

**What I actually did:**

- Keep a **gold set** of support questions (right doc, wrong-doc traps, multi-doc questions)
- After a retrieval change, rerun that set — do not only try new questions
- Read citations: if the answer is right but the cited chunk is wrong, it still fails
- For ingest changes: spot-check chunk boundaries on a known PDF (tables, headers, footers)
- For refresh: change a fixture file, confirm old vectors drop and new chunks rank

**How I validated my own PRs:**

- Run ingest on a small doc subset first
- Query the same questions before/after
- Review two or three answers with support before promoting a retrieval default (chunk size, top-k)

---

## Why It Matters

Tokenization and capital ops live on **written policy**. If the Q&A tool cites the wrong PDF, people will stop trusting it and go back to folders — or worse, act on a stale clause. This role is **data engineering + retrieval + evaluation**, with an LLM as the last step. That is the Finix196 story for Senior Data / GenAI interviews.

---

## Interview Shortcuts

### 30 seconds

> "Data Science Specialist at Finix196 Capital — RWA tokenization and finance docs. I owned the retrieval pipeline for an internal RAG Q&A tool: Python ingestion, chunking, metadata, embeddings, vector upserts, cosine/ANN retrieval, top-k, and LLM answers with citations. I automated document refresh and tuned chunking and filters with support so we got fewer wrong-document answers."

### 2 minutes

> "Finix196 Capital does real-world asset tokenization — real estate and capital products. Internal support and ops were spending too much time searching finance and tokenization PDFs.
>
> I owned the retrieval side of an internal RAG Q&A tool. Python jobs chunked the PDFs, attached metadata with the document owners, embedded the chunks, and upserted them into a vector store. On query, I embedded the question, ran cosine similarity / ANN, applied metadata filters, took top-k, and generated an LLM answer with citations. The chat UI was Node.js; I owned the FastAPI backend for retrieve, rank, and generate, and paired with another engineer on the frontend.
>
> Two things made it usable. First, document refresh: when a policy file changed, we re-chunked, re-embedded, and upserted so ops did not rebuild the index by hand. Second, evaluation: support showed us wrong-document answers. I had assumed more context would help; it often hurt. We tuned chunk size, overlap, filters, and top-k on the same examples until answers stayed on-policy."

### STAR bullets

**Ownership — retrieval pipeline**

- *Situation:* Teams searched finance/tokenization folders by hand
- *Task:* Own retrieval for an internal RAG QnA tool
- *Action:* Ingest (chunk, metadata, embed, upsert); query (ANN/cosine, top-k, cited LLM answers); refresh automation; support review
- *Result:* Questions against the corpus instead of folder search; index stayed current when PDFs changed

**Mistake — more context is not better**

- *Situation:* I increased top-k / chunk volume to “give the model more”
- *Task:* Fix vague or wrong-policy answers
- *Action:* Reviewed cases with support; tuned top-k, metadata filters, chunk size/overlap; retested the same questions
- *Result:* Higher precision; fewer “wrong doc” tickets
- *Learning:* RAG quality is retrieval + evaluation, not a larger context window

**Process — document refresh**

- *Situation:* Policy PDFs changed; stale embeddings kept ranking
- *Task:* Stop manual index rebuilds
- *Action:* Python job for new/changed files → re-chunk, re-embed, upsert
- *Result:* Ops could refresh without engineering; answers tracked current policy

**Collaboration — support as evaluators**

- *Situation:* We could not widen access on a prototype that failed silently
- *Task:* Make quality measurable
- *Action:* Sample-answer review; grouped failures (chunk vs filter vs rank vs stale); one change at a time
- *Result:* Feedback became a test set, not a generic “the model is wrong” complaint

### Likely follow-ups


| Question | Hint |
| -------- | ---- |
| What is Finix196? | Capital / RWA tokenization — finance and tokenization **documents**, not a public chatbot |
| Your title? | **Data Science Specialist**, on-site TX, Jan 2024 – Feb 2025 |
| What did you own? | Retrieval: ingest, index, query, citations, refresh, FastAPI ranking/generation |
| What did you not own? | Source-of-truth PDFs, policy sign-off, most of the Node.js chrome |
| Vector DB name? | Speak to **vector store + embeddings + ANN/cosine** — do not invent a vendor if they ask for a brand you did not use |
| Why citations? | Support must verify the chunk; citations make wrong retrieval visible |
| Why metadata filters? | Semantic neighbors can be the wrong **doc type** (FAQ vs transfer policy) |
| Chunk size? | Tuned with overlap using support examples — no single magic number |
| How did you eval? | Gold questions + “wrong doc” tickets; change one knob; retest the same set |
| FastAPI vs Node? | FastAPI = retrieve/rank/generate. Node = chat UI. Pair on the frontend. |
| Finix196 vs LABS196? | Finix196 = **RAG on finance and tokenization docs**. LABS196 = **multi-agent tools** plus **ERC token / Fireblocks POCs** |

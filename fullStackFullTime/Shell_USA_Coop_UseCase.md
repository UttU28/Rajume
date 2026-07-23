# Shell USA — Regulated Token Payment POC (Co-Op)

**Role:** Python Developer Co-Op  
**Company:** Shell USA, Inc., TX  
**Period:** June 2023 – Dec 2023  
**Project type:** Innovation POC — cross-functional squad (Solidity/Web3 + full-stack + data science)  
**Outcome:** Technical POC completed; **production rollout paused** pending legal/regulatory clarity  
**Stack:** Python, FastAPI, React.js, Next.js, D3.js, Azure (AKS, App Service, API Management, Functions, Databricks), PostgreSQL, MongoDB, Snowflake, Fireblocks SDK, Metamask SDK, Solidity (ERC-3643 / ERC-20), Llama 3.2, Azure DevOps CI/CD

---

## What Was the POC? (Plain English)

Shell's innovation team wanted to see if the company could settle B2B partner payments and track tokenized energy attributes using a permissioned company token on Ethereum — not a public cryptocurrency, but a controlled testnet prototype. Over six months, the co-op squad built the full path: issue a compliance-aware token, create user wallets through Fireblocks, let users connect via Metamask in a React dashboard, and pipe transaction data into analytics for stakeholder demos. The POC was needed because Shell was already exploring blockchain for supply chain, commodity trading, and environmental credits — this project tested whether the same approach could work for partner payments with compliance built in from the start.

---

## Company Context

| | |
|---|---|
| **What we built** | Token payment + transaction monitoring POC on Ethereum testnet |
| **What we did not build** | Production payment rail, public token sale, or retail crypto product |
| **Team** | Solidity devs (contracts), me (platform + APIs + data), data science (Llama 3.2), product owner |
| **My role** | Connect wallets, Fireblocks, contracts, site, APIs, databases, and analytics into one demo stakeholders could use |

---

## Team Makeup

| Role | Focus |
|------|--------|
| **Solidity / Web3 developers** | ERC-3643 permissioned token + ERC-20 interface on testnet; ONCHAINID / compliance hooks; contract ABIs |
| **Me (Python Co-Op)** | Metamask SDK integration, Fireblocks SDK wallet + transfer flows, FastAPI, React/Next.js, PostgreSQL/MongoDB, Databricks ETL, Azure deploy |
| **Data science** | Llama 3.2 fine-tuning to classify transaction memos / flag anomalies on curated data |
| **Product owner + Legal liaison** | Demo scope, stakeholder cadence, escalating regulatory questions that eventually paused rollout |

---

## Wallet & Transaction Model (Metamask + Fireblocks)

This is the split stakeholders asked for in demos:

### Fireblocks SDK — custodial backbone
- **Generated wallets (vault accounts)** for each POC user on onboarding.
- **All programmatic transfers and transactions** were **created, signed, and tracked through Fireblocks SDK** — not raw private keys in our app.
- Fireblocks webhook/audit log fed our API → PostgreSQL `transactions` + MongoDB `fireblocks_events`.
- Institutional policy controls (approval queues, gas management) stayed in Fireblocks sandbox.

### Metamask — Web3 wallet connect layer
- I integrated the **Metamask SDK** in the React dashboard as the **user-facing Web3 wallet** experience.
- Users **connected Metamask** to link an external address **or** interact with flows that routed signing back through the Fireblocks-managed vault tied to their account.
- Session state (`wallet_address`, `chain_id`, `connected_at`) stored in **MongoDB**; linked to **PostgreSQL** `users` row.

```
User signs up (Next.js site)
        ↓
Azure AD / app login → JWT (FastAPI) → RBAC role assigned
        ↓
Fireblocks SDK: create vault account + deposit address for user
        ↓
User connects Metamask (SDK) → address linked in PostgreSQL
        ↓
User initiates token transfer in React UI
        ↓
Transfer built and submitted via Fireblocks SDK (custody + signing)
        ↓
ERC-3643 contract runs canTransfer / compliance check on-chain
        ↓
Tx confirmed → Azure Functions index event → FastAPI persists → dashboard updates
```

**Interview line:** *"Metamask was the Web3 wallet UX; Fireblocks was where wallets were generated and every transfer was actually managed."*

---

## Auth & Data Storage (Explicit)

Yes — we had full **auth** and **database** layers. The POC was not chain-only.

### Authentication & authorization

| Layer | Technology |
|-------|------------|
| **Identity (humans)** | Azure AD (Entra ID) SSO for internal stakeholders; email/password + JWT for external POC partners |
| **API auth** | FastAPI JWT middleware behind **Azure API Management** |
| **RBAC** | Roles in **PostgreSQL** (`analyst`, `executive`, `admin`, `poc_partner`) |
| **Chain identity** | Fireblocks vault ID + Metamask `wallet_address` linked to `users.id` |

### Databases — what lived where

| Database | Purpose |
|----------|---------|
| **PostgreSQL** | Relational source of truth — users, wallets, transactions, balances, audit log |
| **MongoDB** | Semi-structured / high-write payloads — raw chain logs, webhooks, sessions, ML outputs |
| **Snowflake** | Analyst SQL prototype for reporting views |
| **Databricks Delta** | Bronze / Silver / Gold pipeline storage before load back to PG/Mongo |

**Rule we followed:** PostgreSQL owned **who** and **what happened** (users, tx facts, balances); MongoDB owned **raw event blobs** and ML outputs; dashboards read **curated** tables after ETL, not RPC calls.

---

## End-to-End POC Flow

```
Stakeholder / partner opens Next.js POC site (Azure App Service)
        ↓
Login → Azure AD or partner credentials → JWT issued
        ↓
React dashboard (D3.js): balance, transfer history, compliance status
        ↓
Onboarding: Fireblocks SDK creates vault wallet → Metamask SDK connect/link
        ↓
User requests transfer of Shell POC token (ERC-3643) or demo energy-attribute asset
        ↓
FastAPI validates RBAC + balance → Fireblocks SDK submits transaction
        ↓
Smart contract compliance check (ERC-3643 Identity Registry + canTransfer)
        ↓
Azure Functions capture Transfer event → FastAPI write
        ↓
PostgreSQL transactions row + MongoDB chain_events document
        ↓
Optional: Llama 3.2 classifies tx memo (GPU AKS, API Management)
        ↓
Nightly Databricks: Bronze → Silver → Gold → reporting tables
        ↓
Dashboard + Snowflake analyst views + CSV export for leadership demo
        ↓
[Post co-op] Legal review → rollout held — regulatory uncertainty
```

---

## My Scope as Co-Op

### Owned end to end
- **Metamask SDK** integration (connect, account, chain events in React)
- **Fireblocks SDK** integration (vault create, transfer APIs, webhook ingestion)
- FastAPI services: auth, wallet linking, transaction orchestration, read APIs
- PostgreSQL schema for users / wallets / transactions; MongoDB for events
- React dashboard + Next.js site; D3.js analytics
- Databricks PySpark ETL + Snowflake view prototypes
- Azure DevOps pipelines; PostgreSQL/MongoDB index tuning

### Partnered with Web3 team
- They deployed ERC-3643 contracts and compliance registries on testnet
- I wired ABIs, event listeners, and Fireblocks contract-call payloads
- Coordinated testnet redeploys when compliance rules changed

---

## Databricks ETL — Data Processing & Analysis

Every night, a Databricks job pulled data from PostgreSQL (users and transactions), MongoDB (raw chain events and Fireblocks webhooks), and a few ops CSVs into a simple Bronze → Silver → Gold pipeline. Bronze was the raw dump; Silver cleaned it up — deduped transaction hashes, linked Fireblocks IDs to on-chain hashes, and fixed messy fields. Gold turned that into the numbers stakeholders actually cared about: daily transfer volume, how many users finished onboarding, compliance failures, and timing between Fireblocks and the chain. Those curated results landed back in PostgreSQL/Mongo for the React dashboards and in Snowflake for analysts to query in SQL.

### Pipeline flow

```
PostgreSQL snapshots (users, transactions)   MongoDB exports (chain_events, fireblocks)
Batch ops CSVs (volume, region, partner)              │
        └────────────────────┬────────────────────────┘
                             ▼
                   Databricks Bronze (raw)
                             ▼
                   Databricks Silver (cleansed)
         — dedupe tx_hash, link fireblocks_id ↔ on-chain hash, normalize enums
                             ▼
                   Databricks Gold (metrics)
                             ▼
              PostgreSQL reporting_* + MongoDB aggregates + Snowflake views
                             ▼
                    React/D3 dashboards + analyst SQL
```

### What went in

| Source | What it held |
|--------|--------------|
| PostgreSQL | Users, transactions, wallet links |
| MongoDB | Chain events, Fireblocks webhooks, Metamask sessions |
| Ops CSVs | Partner settlement volumes for comparison |

### What came out (Gold → dashboards)

| Metric | Used for |
|--------|----------|
| Daily transfer volume | D3 time-series on the React dashboard |
| Onboarding funnel | Vault created → Metamask linked → first transfer |
| Compliance revert rate | Failed `canTransfer` checks by reason |
| Fireblocks vs chain latency | Custody submit → on-chain confirm timing |

---

## POC Challenges & How We Handled Them

### Challenge 1: Testnet contract redeploy broke Fireblocks + dashboard sync

**Symptom:** Fireblocks showed `COMPLETED` but dashboard balance unchanged after ERC-3643 redeploy.

**Root cause:** New contract address not updated in Fireblocks asset config or Azure Functions indexer.

**Fix:** Contract addresses in Azure DevOps env vars; versioned ABIs; `GET /chain/sync-status` health check; Fireblocks asset catalog updated in same release train.

---

### Challenge 2: Metamask-connected address vs Fireblocks vault mismatch

**Symptom:** User connected Metamask but transfers failed compliance — Identity Registry had vault address, not Metamask EOA.

**Root cause:** ERC-3643 verifies **holder identity**, not just any connected wallet.

**Fix:** Onboarding flow: Fireblocks vault = **primary holder**; Metamask link stored as `linked_external` for UX only until compliance team whitelisted via ONCHAINID demo claims. Documented in POC runbook for Legal demos.

---

## Why the POC Was Held (Legal / Regulatory)

| Concern (2023–2024) | Impact on Shell |
|---------------------|-----------------|
| **SEC Howey uncertainty** | Company-issued token could be deemed an investment contract depending on marketing and utility — no safe harbor for energy majors |
| **Money transmission / state licensing** | B2B payment token might trigger state MTB analysis if used as settlement rail |
| **Security vs commodity vs utility** | Unclear bucket for permissioned energy-sector tokens; ERC-3643 helps technically, not legally |
| **Enterprise risk appetite** | Shell blockchain programs (VAKT, digital passport, Avelia) stayed in **permissioned / attribute-tracking** lanes — public-style token payments were a bigger leap |

**Decision:** Complete co-op POC in Dec 2023; archive testnet contracts; preserve architecture docs and ETL patterns for future regulatory window. **My work still valid** — wallet infra, Fireblocks integration, Metamask UX, data pipeline — the pause was **go-to-market**, not a failed sprint.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│  Next.js POC Site          React Dashboard (Metamask SDK, D3.js)  │
└──────────────┬──────────────────────────────┬───────────────────────┘
               │  Azure AD / JWT               │
               ▼                              ▼
┌──────────────────────────────────────────────────────────────────────┐
│           Azure API Management (auth, throttling)                    │
└──────────────────────────────┬───────────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│  FastAPI (AKS)  │  Fireblocks SDK (wallets, transfers)  │  Functions │
│  JWT + RBAC     │  Llama 3.2 inference (GPU)           │  chain idx │
└───────┬─────────┴──────────────────┬───────────────────┴──────┬─────┘
        │                            │                          │
        ▼                            ▼                          ▼
  PostgreSQL                   MongoDB              ERC-3643 testnet
  users·roles·tx               events·sessions      (Solidity team)
        │                            │
        └────────────┬───────────────┘
                     ▼
        Databricks Bronze → Silver → Gold → Snowflake views
```

---

## Interview Talking Points (STAR-ready)

### POC purpose in one story
**Situation:** Shell innovation explored company-issued token payments for partners; unclear if US law allowed it.  
**Task:** Prove technical feasibility in 6 months as co-op without production commitment.  
**Action:** ERC-3643 testnet token; Fireblocks for wallet gen + all transfers; Metamask SDK for Web3 UX; PG/Mongo auth + data; Databricks analytics.  
**Result:** End-to-end demo worked; Legal held rollout for regulatory reasons — engineering delivered a complete POC.

### Metamask + Fireblocks split
**Situation:** Stakeholders wanted familiar wallet UX and institutional custody.  
**Task:** Integrate both without exposing private keys.  
**Action:** Metamask SDK for connect/display; Fireblocks SDK for vault creation and every transaction; PostgreSQL linked `user_id` → `vault_id` → `metamask_address`.  
**Result:** Demo showed consumer-grade wallet flow with enterprise custody underneath.

### Auth + databases
**Situation:** POC needed real login, roles, and auditable tx history — not just chain explorer links.  
**Task:** Design storage and RBAC.  
**Action:** Azure AD + JWT; PostgreSQL for users/transactions; MongoDB for raw events; RBAC on API and UI.  
**Result:** Analysts and execs saw role-appropriate dashboards with full audit trail.

---

## Key Metrics

- **< 250ms** average FastAPI / inference latency (API Management + AKS)
- **~35%** faster delivery after Azure DevOps automation
- Databricks curated multi-source data → dashboard + Snowflake analyst views
- POC **completed** on schedule; **production held** for legal/regulatory review

---

## 60-Second Elevator Pitch

> "At Shell USA I co-oped on an innovation POC: could the company settle partner payments using its own permissioned token? Solidity devs built an ERC-3643 testnet contract — compliance on-chain, ERC-20 compatible. I integrated Fireblocks SDK to generate user wallets and manage every transfer, and Metamask SDK as the Web3 wallet connect layer in React. Behind that: FastAPI on AKS with JWT and RBAC, PostgreSQL for users and transactions, MongoDB for chain events, and Databricks ETL into dashboards and Snowflake. We proved the full path — login, wallet, transfer, analytics — but leadership held production because US token law in 2023–2024 was too unsettled for an energy company to launch. The tech shipped; the pause was legal, not engineering."

---

*Aligns with resume: Shell USA, Inc., Python Developer Co-Op, June 2023 – Dec 2023.*

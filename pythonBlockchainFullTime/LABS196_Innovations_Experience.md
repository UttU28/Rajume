# LABS196 Innovations — Sr. Python Blockchain Developer

**Feb 2025 – Present · Hybrid, TX**

---

## Company

LABS196 Innovations runs a **regulated lab and research platform**. The work is not one customer-facing app — it is the **multicloud backbone** (AWS + Azure) that lab and research services run on. Environments are **GxP-validated** and subject to **FDA-aligned** internal reviews, so uptime, traceability, and controlled change matter as much as speed.

---

## My Role

I am on the **platform team**. I keep Kubernetes workloads, infrastructure, and release pipelines **stable, compliant, and repeatable** across **Dev, Test, UAT, QA, and Production**.

**I build / maintain:**
- **Terraform** — VPC/VNet, IAM, EKS, AKS, RDS, Key Vault, S3/Blob, networking
- **Ansible** — post-provision config Terraform modules don't cover cleanly
- **Rancher** — centralized multicloud cluster ops (EKS + AKS)
- **Argo CD** — GitOps release automation into all envs
- **GitOps repo** — env + cloud value overlays, Application/ApplicationSet config
- **CI** — Bitbucket Pipelines (lint, test, Docker build, Terraform plan/apply)
- **Platform Helm** — Prometheus, log agents, ingress controllers (not app charts)
- **Secrets infra** — Key Vault / Secrets Manager + External Secrets → K8s
- **Observability** — Prometheus, CloudWatch, ELK; on-call, runbooks
- **Backup & retention** — S3, Azure Blob, DBs per GxP rules

**App teams build:** application Helm charts, Dockerfiles, app code.

**I review:** app charts before prod — probes, resources, security context, no secrets in Git, correct EKS vs AKS ingress annotations.

**I do not own alone:** compliance policy, application code, or final production access approvals.

---

## Team

| Group | How we interact |
|-------|-----------------|
| **Platform / staff engineers** | Design reviews, GitOps standards, Argo CD and Rancher patterns |
| **Application teams** | Helm charts, env promotion, deploy troubleshooting |
| **Compliance** | GxP validation, audit logging, retention requirements |
| **Security** | RBAC, least-privilege access, Key Vault / secrets |
| **Data / pipeline owners** | Platform SLAs for data pipeline services |

Shared **on-call rotation** for platform and data pipeline services.

---

## How Work Reaches Me

- **Jira** — infra changes, compliance tasks, platform improvements
- **On-call pages** — alerts from Prometheus, CloudWatch, ELK
- **Slack** — incident coordination with app teams
- **PR reviews** — Terraform, Ansible, GitOps, platform Helm

**Triage:** alert/ticket → dashboards/logs → runbook → coordinate → fix/rollback → document.

---

## Platform Stack — Who Does What

| Tool | Job | Analogy |
|------|-----|---------|
| **Terraform** | Provisions cloud foundation | Builds the building |
| **Ansible** | Bootstrap / config after TF | HVAC wiring after build |
| **Rancher** | Manages EKS + AKS clusters | Building management / access control |
| **Argo CD** | GitOps app delivery into clusters | Tenant move-in process from approved plans |
| **Helm** | Packages K8s manifests | Standardized deployment template |
| **Prometheus** | Metrics + alerts | Cameras / sensors |
| **ELK + CloudWatch** | Central + AWS-native logs | Security / audit logs |

**Rancher + Argo CD together is normal** — they solve different problems:
- **Rancher** = cluster management (multicloud ops, RBAC, cluster health)
- **Argo CD** = application GitOps (sync apps from Git into clusters)

---

## Where Services Are Deployed

Platform infra is **separate from app projects** — it connects to K8s clusters Terraform creates first.

```
CI/CD pipeline
  └── Terraform apply → Ansible (if needed)
          │
          ├── Platform / mgmt cluster
          │     ├── Rancher server
          │     ├── Argo CD
          │     └── (optional) central dashboards
          │
          ├── Workload clusters (Dev / Test / UAT / QA / Prod × EKS + AKS)
          │     ├── App workloads        ← Argo CD + Helm (app team chart)
          │     ├── Prometheus           ← in-cluster metrics
          │     └── Log agents           ← ship to CloudWatch (AWS) + ELK (central)
          │
          └── Central ELK                ← logs from all clusters
```

| Service | Where | Who deploys |
|---------|-------|-------------|
| EKS / AKS / VPC / IAM / RDS | Cloud (Terraform) | Platform |
| Rancher, Argo CD | Platform cluster | Platform |
| Prometheus, Fluent Bit | Inside each workload cluster | Platform (Helm) |
| ELK | Central observability cluster/VMs | Platform |
| CloudWatch | AWS managed (EKS integration) | Platform config |
| App services | Workload clusters | App team chart via Argo CD |
| ETL / data pipelines | K8s CronJobs or data platform | Platform / data team |

---

## Terraform vs Ansible

**Terraform creates:** VPC, subnets, security groups, IAM, **EKS/AKS clusters**, RDS, Key Vault, Azure SQL, S3/Blob.

**Ansible handles:** agents, OS hardening, bootstrap steps that don't fit TF modules.

**Order:**
```
Terraform → Ansible → Rancher imports clusters → Argo CD deploys apps
```

**How I verify Terraform:**
1. `terraform plan` in PR + peer review
2. Apply to **Dev first**, walk env ladder to Prod
3. Re-run plan — no drift
4. Spot-check: cluster ACTIVE, `kubectl get nodes`, RDS/Key Vault reachable
5. Rancher shows cluster healthy; Prometheus targets up

**How I verify Ansible:**
1. `ansible-playbook --check` (dry run)
2. Run playbook; confirm `failed=0`
3. Re-run — idempotent (no changes on second run)
4. Verification tasks in playbook assert expected state

---

## CI/CD

| Layer | Tool |
|-------|------|
| **Git** | **Bitbucket** |
| **CI** | **Bitbucket Pipelines** |
| **CD** | **Argo CD** (GitOps) |

**CI builds and validates. Argo CD deploys.** No SSH or manual `kubectl apply` to prod.

```
Bitbucket Pipelines (CI)                    Argo CD (CD)
────────────────────────                    ────────────
PR opened                                   Git merge / tag
  → lint, test                                → detects GitOps change
  → docker build                              → syncs Helm to cluster
  → push image to ECR/ACR                     → Dev → Test → UAT → QA → Prod
  → terraform plan (infra PRs)
  → terraform apply (after approval)
```

### What each pipeline runs

**App repo (Bitbucket Pipelines):**
```
lint → unit tests → Docker build → push to ECR/ACR → update GitOps repo image tag
```

**Platform / infra repo:**
```
terraform validate → terraform plan (PR) → terraform apply (Dev first, then promoted)
ansible-playbook --check → ansible-playbook run
```

**Platform Helm / GitOps repo:**
```
helm lint → helm template dry-run → merge → Argo CD picks up change
```

### Runners

| Runner | Used for |
|--------|----------|
| **Bitbucket cloud-hosted** | Lint, test, `terraform plan`, lightweight PR checks |
| **Self-hosted** (EKS or EC2 in AWS) | Docker builds, image push to ECR, Terraform apply into private VPC |

Platform team maintains self-hosted runners for jobs that need VPC access or faster Docker builds.

### Who owns what

| Task | Tool |
|------|------|
| Source control | Bitbucket |
| Build & test on PR | Bitbucket Pipelines |
| Docker image → registry | Bitbucket Pipeline (self-hosted runner) |
| Infra (EKS, VPC, IAM) | Terraform via pipeline |
| Bootstrap config | Ansible via pipeline |
| Deploy apps to K8s | Argo CD |
| Env promotion | Argo CD + GitOps overlays |
| Frontend previews (if applicable) | AWS Amplify |

---

## Monitoring

| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | **Prometheus** (in each cluster) | Pod/node/K8s metrics, alerting |
| Logs (AWS) | **CloudWatch Logs** | EKS-side logs and alarms |
| Logs (central) | **ELK** (Elasticsearch, Logstash, Kibana) | Cross-cloud log search |
| Cluster ops | **Rancher** | Cluster health view (not full observability) |
| Deploy health | **Argo CD** | Sync status, drift, failed deploys |

**Incident flow:** alert → Prometheus metrics → CloudWatch/ELK logs → Rancher (if cluster-level) → Argo CD (if deploy-related) → runbook → fix.

---

## Helm — Multicloud Layout

**Industry standard at Labs196:** one Helm chart, env + cloud overlays in a GitOps repo.

```
App repo (app team)                    GitOps repo (platform + app)
──────────────────                     ─────────────────────────────
helm/lab-service/                      apps/lab-service/
  Chart.yaml                             dev/eks/values.yaml
  values.yaml  (cloud-neutral defaults)  dev/aks/values.yaml
  templates/                             test/eks/values.yaml
                                         ...
                                         prod/eks/values.yaml
                                         prod/aks/values.yaml
                                       argocd/applications/
                                         lab-service-prod-eks.yaml
                                         lab-service-prod-aks.yaml
```

**Same chart for EKS and AKS.** Only values change per cloud:
- EKS: ALB ingress annotations, `gp3` storage, IAM role ARN on ServiceAccount
- AKS: App Gateway ingress, `managed-csi` storage, workload identity client ID

**GxP promotion:**
```
Dev (EKS+AKS) → Test → UAT → QA → Prod
  auto-sync       CI pass   QA sign-off   validation   tagged release, restricted sync
```

**Deploy commands (Argo CD does this automatically):**
```bash
# EKS prod example
helm upgrade --install lab-service ./helm/lab-service \
  -f values.yaml -f apps/lab-service/prod/eks/values.yaml -n production
```

At scale: **ApplicationSet** generates one Argo CD app per env × cloud combo.

---

## Values & Secrets

### Non-secret values (safe in Git)

Stored in **GitOps overlays** per env + cloud.

| Value | Source |
|-------|--------|
| Replicas, resources | Platform standards + app team |
| Image tag | CI build / release tag (pinned in prod) |
| Ingress host | Platform DNS / networking |
| DB hostname | Terraform outputs |
| IAM role ARN / workload identity ID | Terraform outputs → values file |
| `ENV`, `LOG_LEVEL` | GitOps overlay |

Flow: `Terraform outputs → GitOps values → Argo CD → cluster`

### Secrets (never in Git)

| Cloud | Store | How pods get them |
|-------|-------|-------------------|
| AWS | **Secrets Manager** | External Secrets Operator / CSI → K8s Secret |
| Azure | **Key Vault** | External Secrets Operator / CSI → K8s Secret |

Helm references the **secret name only**, never the password:

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: lab-service-db
        key: password
```

Platform sets up External Secrets + IAM / workload identity. App chart consumes the K8s secret.

---

## What I Built & Improved

1. **GitOps with Argo CD** — traceable deploys across GxP envs; fewer manual kubectl steps
2. **Rancher + Entra ID** — single multicloud view; audit-ready RBAC
3. **Terraform / Ansible IaC** — version-controlled AWS + Azure footprint
4. **Observability** — Prometheus + CloudWatch + ELK for cross-cloud incident response
5. **Backup & retention automation** — GxP-aligned S3, Blob, DB workflows

---

## Testing & My Own Pipelines

**App releases:** Dev → Test → UAT/QA → Prod; QA sign-off on GxP paths; Argo CD drift checks.

**My infra changes:**
- `terraform plan` + PR review before apply
- Apply Dev first, walk env ladder
- Ansible `--check` then idempotency re-run
- Verify: Rancher health, Prometheus targets, logs clean
- Rollback: revert Git or Argo CD sync rollback — no SSH to prod

---

## Why It Matters

Research and lab services depend on this platform being **available, auditable, and correctly configured**. Without platform infra, app teams can't deploy safely, audits fail on traceability, and incidents go undetected.

---

## Interview Shortcuts

### 30 seconds
> "Sr. Python Blockchain Developer on the platform team for a regulated lab/research environment. Multicloud AWS + Azure — EKS, AKS, Terraform, Bitbucket Pipelines for CI, Argo CD for GitOps CD, Rancher, Prometheus/ELK. GxP-validated envs from Dev through Prod. App teams own charts; I own clusters, pipelines, GitOps, secrets infra, and observability."

### 2 minutes
> "Labs196 is a regulated lab platform — my team owns the cloud and Kubernetes backbone. Terraform builds EKS, AKS, networking, IAM, and databases. **Bitbucket Pipelines** handles CI — lint, test, Docker builds, Terraform plan/apply. **Argo CD** handles CD — GitOps syncs Helm to the right cluster. Rancher manages clusters centrally. App teams build Helm charts; platform owns GitOps overlays per env and cloud — `prod/eks`, `prod/aks`, etc. Self-hosted runners handle Docker builds inside our AWS network. Secrets live in Key Vault and Secrets Manager — never in Git. On-call uses Prometheus, CloudWatch, and ELK. Everything ties back to GxP traceability and controlled prod promotion."

### STAR bullets

**GitOps standardization**
- *Situation:* Manual release steps across GxP multicloud envs
- *Action:* Argo CD GitOps with approved-branch prod syncs, secrets outside Git
- *Result:* Fewer manual steps; audit-ready deploy history

**Centralized cluster ops**
- *Situation:* EKS and AKS managed separately; access hard to audit
- *Action:* Rancher + Entra ID RBAC across both clouds
- *Result:* Single ops view; least-privilege prod access

**GxP backup & retention**
- *Situation:* Manual/ad-hoc backup jobs for regulated data
- *Action:* Automated S3, Blob, and DB retention per compliance policy
- *Result:* Reliable retention without manual ops

### Likely follow-ups

| Question | Hint |
|----------|------|
| Rancher **and** Argo CD? | Rancher = cluster ops; Argo CD = app GitOps. Complementary. |
| Who builds Helm? | App team = app chart. Platform = clusters, GitOps, secrets, platform Helm, review. |
| Where do env values come from? | GitOps overlays per env/cloud; TF outputs for hostnames, IAM ARNs. |
| Where are secrets? | Key Vault (Azure) + Secrets Manager (AWS) → External Secrets → K8s. Never Git. |
| Terraform vs Ansible? | TF = cloud resources + clusters. Ansible = post-provision config. |
| Same Helm for EKS and AKS? | Yes — one chart, different values files per cloud. |
| How verify TF/Ansible? | plan/check → apply Dev first → idempotency → Rancher/Prometheus checks. |
| What is GxP? | Validated envs, controlled GitOps, audit logging, compliant retention. |
| On-call flow? | Alert → Prometheus/ELK → runbook → coordinate → restore → document. |
| CI vs CD tools? | **Bitbucket Pipelines** = CI (build, test, TF plan). **Argo CD** = CD (GitOps deploy). |
| What runners? | Cloud-hosted for PR checks/plans; self-hosted on EKS/EC2 for Docker builds + VPC access. |

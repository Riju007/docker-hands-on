# Docker + Kubernetes Mastery Roadmap
**Background:** Django, Python, MySQL, Docker basics, Azure  
**Goal:** Production-grade Docker + Kubernetes skills through real systems  
**Mentor Style:** Hands-on, milestone-driven, production constraints

**Status:** Docker intermediate | Kubernetes beginner

---

## Phase 0: Docker Production Baseline (1-2 weeks)
**Objective:** Make Docker builds fast, secure, and reliable before touching Kubernetes.

### Milestones & Projects

**Project 0.1 - Optimized Django Image**
- Use `uv` for dependency installation.
- Advanced multi-stage build (builder + runtime).
- Enable BuildKit caching (layers, uv cache mount).
- Non-root user, minimal image size (<300MB target).
- Proper `.dockerignore`.

**Project 0.2 - Production Debugging Lab**
- Intentionally introduce issues (OOM, slow start, high CPU, secret exposure).
- Master debugging flow: `docker logs`, `docker stats`, `docker exec`, healthchecks, resource limits.
- Add Prometheus client for metrics.

**Project 0.3 - Stateful Multi-Container Stack**
- Django + Celery + Redis + Postgres using Docker Compose.
- Custom bridge networks.
- Volumes, backups, and data persistence testing.
- Simulate volume failures and recovery.

**Key Concepts to Master:**
- BuildKit caching, layer ordering, multi-stage, security scanning (Aqua/JFrog), HEALTHCHECK, ulimits, networking, volumes vs bind mounts.

**Success Metric:** Rebuild time < 60s on code change. Debug any container issue in < 5 minutes.

---

## Phase 1: Local Kubernetes Fundamentals (2-3 weeks)
**Objective:** Run your full Django stack on Kubernetes locally with confidence.

**Recommended Tools:** kind (preferred) or minikube, kubectl, K9s, Helm (basics).

### Projects

**Project 1.1 - First Django Deployment**
- Deploy optimized image to kind cluster.
- Deployment, Service, ConfigMap, Secret.
- Proper liveness + readiness probes.
- Rolling updates.

**Project 1.2 - Full Production-like Stack**
- Django + Postgres (StatefulSet + PVC) + Redis + Celery workers.
- Ingress controller (nginx or Traefik).
- External access testing.

**Project 1.3 - Observability & Chaos**
- Logging (Loki or EFK light), Metrics (Prometheus + Grafana).
- Intentionally break pods, test self-healing, scaling.
- HPA (Horizontal Pod Autoscaler) basics.

**Stretch Challenges:**
- Use Helm chart for the application.
- Simulate node drain and pod eviction.

**Key Concepts:**
- Pods, Deployments, StatefulSets, Services, Ingress, ConfigMap/Secret, Probes, PVC, HPA.

**Success Metric:** Full stack running locally. Can survive pod kills and scaling without downtime.

---

## Phase 2: Production Kubernetes on Azure (4-6 weeks)
**Objective:** Production-grade AKS deployment with real constraints.

**Tools:** AKS, Azure Container Registry (ACR), GitHub Actions, ArgoCD/Flux (GitOps), Helm.

### Projects

**Project 2.1 - GitOps Django on AKS**
- Create small AKS cluster.
- CI/CD pipeline: Build → ACR → Deploy via GitOps.
- Multi-environment config (dev/staging/prod) using Helm values.

**Project 2.2 - Resilient & Observable System**
- HPA + Cluster Autoscaler.
- cert-manager + Ingress.
- Full monitoring stack (Prometheus, Grafana, Loki).
- Alerting rules.

**Project 2.3 - Advanced Failure & Release Scenarios**
- Blue/Green or Canary deployments.
- Node failure simulation, DB connection pool exhaustion.
- Secret rotation, config changes without downtime.
- Cost monitoring.

**Stretch Challenges:**
- Implement or use an Operator.
- Policy enforcement (Gatekeeper).
- Multi-region DR strategy.

**Key Concepts:**
- GitOps workflow, resource requests/limits, autoscaling, ingress, service mesh basics, chaos engineering.

**Success Metric:** Production-like Django system on AKS that survives common failures and supports zero-downtime releases.

---

## Phase 3: Advanced & Specialization (Ongoing)
- Service Mesh (Istio/Linkerd) – when and why
- Storage deep dive (Azure Disk vs Rook)
- Security & Policy as Code
- eBPF tools (Falco)
- Custom controllers / Operators
- Cost optimization & FinOps practices

---

## Execution Rules
1. Finish one project completely before moving to the next.
2. Break things on purpose and document fixes.
3. Keep everything in Git.
4. After each project, do a mini code-review with me.
---
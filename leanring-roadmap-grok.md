# Docker + Kubernetes Mastery Roadmap
**Owner:** Riju007 (Avisek)  
**Main Learning Repo:** [Riju007/docker-hands-on](https://github.com/Riju007/docker-hands-on)

**Goal:** Turn this repository into a strong production-grade Docker + Kubernetes learning showcase.

**Current Status:** Docker intermediate | Kubernetes beginner

---

## Phase 0: Docker Production Baseline (1-2 weeks)
**Focus:** Improve existing folders (`django-docker-demo` + `docker-debug-lab`)

### Projects

**Project 0.1 - Optimized Django Image** (Start Here)
- Enhance `django-docker-demo/Dockerfile`
- Introduce `uv` for faster dependency installation
- Enable BuildKit caching
- Add non-root user, security hardening, better `.dockerignore`

**Project 0.2 - Production Debugging & Hardening**
- Extend `docker-debug-lab`
- Add resource limits, healthchecks, proper logging
- Build systematic debugging workflow

**Project 0.3 - Stateful & Network Improvements**
- Improve volumes, custom networks, backup strategy in Django setup
- Test real persistence and failure cases

---

## Phase 1: Local Kubernetes (2-3 weeks)
- Deploy optimized Django app to kind/minikube
- Full stack with StatefulSet for Postgres
- Observability + chaos testing

## Phase 2: AKS Production (4-6 weeks)
- GitOps to Azure Kubernetes Service
- Scaling, monitoring, zero-downtime releases

## Phase 3: Advanced (Ongoing)
- Service Mesh, Operators, Policy, Cost optimization

---
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0db7ed,100:384d54&height=200&section=header&text=🐳%20Docker%20Hands-On&fontSize=50&fontColor=ffffff&fontAlignY=38&desc=Learn%20Docker%20by%20Doing%20%7C%20Real%20Projects%2C%20Real%20Containers&descAlignY=58&descSize=18" width="100%"/>

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](https://rust-lang.org)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

<br/>

> **🚀 A hands-on Docker learning lab — from your very first container to multi-language, production-style architectures with CI/CD.**

</div>

---

## 📦 Repository Structure

```
docker-hands-on/
│
├── 🐍 docker-basics/              # Start here! Your first Dockerfile & Python app
├── 🦄 fastapi-demo-01/            # FastAPI + PostgreSQL with Docker Compose
├── 🎸 django-docker-demo/         # Django 6 + PostgreSQL + multi-stage builds + CI/CD
├── 🌐 polyglot-docker/            # Python + Node.js + Rust + Nginx + Grafana/Loki
└── 🔬 docker-debug-lab/           # Simulate real production incidents & debug them
```

---

## 🗺️ Learning Path

Follow these projects in order for the smoothest learning journey:

```
① docker-basics       →    ② fastapi-demo-01    →    ③ django-docker-demo
   First container            Compose + DB               Multi-stage + CI/CD

                                    ↓

④ docker-debug-lab    →    ⑤ polyglot-docker
   Debug like a pro             Multi-language microservices + Observability
```

---

## 🐍 1. docker-basics — Your First Container

**What you'll learn:** Writing a Dockerfile, building an image, running a container, reading live logs.

```
docker-basics/
├── app.py         # Simple Python counter app
└── Dockerfile     # Your first Dockerfile
```

**The App:** A Python script that prints a running counter every 2 seconds — perfect for watching logs live.

```python
# app.py
while True:
    print(f"Running...{counter}!!", flush=True)
    counter += 1
    time.sleep(2)
```

**The Dockerfile:**
```dockerfile
FROM python:3.12
WORKDIR /app
COPY . /app/
CMD ["python", "-u", "app.py"]
```

**▶️ Try it:**
```bash
cd docker-basics
docker build -t my-first-app .
docker run my-first-app
# Watch the counter tick... 🎉
```

---

## 🦄 2. fastapi-demo-01 — FastAPI + PostgreSQL

**What you'll learn:** Docker Compose, multi-container apps, volume persistence, service dependencies.

```
fastapi-demo-01/
├── main.py              # FastAPI app with health-check endpoint
├── requirements.txt     # fastapi, uvicorn, watchfiles
├── Dockerfile
└── docker-compose.yml   # Web + PostgreSQL services
```

**Architecture:**
```
┌─────────────────┐         ┌──────────────────┐
│  FastAPI  :8000 │ ──────► │  PostgreSQL :5432 │
│  (fast-api-     │         │  (fast-api-db)    │
│   demo-01)      │         │                   │
└─────────────────┘         └──────────────────┘
```

**Endpoints:**
| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Hello from Docker! |
| `GET` | `/health-check` | Returns `{"status": "Healthy"}` |

**▶️ Try it:**
```bash
cd fastapi-demo-01
docker compose up --build

# Test it
curl http://localhost:8000/health-check
```

---

## 🎸 3. django-docker-demo — Production-Ready Django

**What you'll learn:** Multi-stage Docker builds, Django + PostgreSQL, GitHub Actions CI/CD, GHCR image publishing.

```
django-docker-demo/
├── config/                  # Django project settings, URLs, WSGI/ASGI
├── core/                    # Core app with health-check view
│   └── views.py             # Returns {"status": "Healthy"}
├── requirements.txt         # Django 6, psycopg, etc.
├── Dockerfile               # ✨ Multi-stage build (builder + runtime)
├── docker-compose.yml       # Web + PostgreSQL
└── .github/workflows/
    └── django_docker_demo.yml  # 🚀 Build & push to GHCR on every push
```

### ✨ Multi-Stage Dockerfile Explained

This is where things get serious! The Dockerfile uses two stages to keep the final image lean:

```dockerfile
# ── Stage 1: Builder ──────────────────────────────
FROM python:3.12-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential  # compile deps
COPY requirements.txt .
RUN pip install -r requirements.txt                       # install into /usr/local

# ── Stage 2: Runtime ──────────────────────────────
FROM python:3.12-slim                                     # fresh, clean image
WORKDIR /app
COPY --from=builder /usr/local /usr/local                 # copy ONLY installed packages
COPY . /app/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

> 💡 **Why two stages?** The builder stage needs `build-essential` (heavy!) to compile Python packages. The runtime stage copies only the installed packages — no build tools, no bloat. Smaller image = faster deploys!

### 🔄 CI/CD Pipeline (GitHub Actions)

Every push to any branch automatically:
1. ✅ Checks out the code
2. 🏷️ Sets a lowercase image name from your GitHub username
3. 🔐 Logs into GitHub Container Registry (GHCR)
4. 🏗️ Builds the Docker image (tagged with the commit SHA)
5. 📤 Pushes the image to `ghcr.io/<your-username>/docker-hands-on`

**▶️ Try it:**
```bash
cd django-docker-demo
docker compose up --build

# Health check
curl http://localhost:8000/health-check/
# → {"status": "Healthy"}
```

---

## 🌐 4. polyglot-docker — Multi-Language Microservices

**What you'll learn:** Multi-container orchestration across different languages, Nginx reverse proxy, centralized logging with Grafana + Loki + Promtail.

```
polyglot-docker/
├── python-api/          # FastAPI service (Python 3.12)
├── node-api/            # Express service (Node.js 22)
├── rust-api/            # Axum service (Rust) — multi-stage build
├── nginx/
│   └── nginx.conf       # Reverse proxy routing all 3 APIs
├── promtail-config.yaml # Scrapes Docker container logs
└── compose.yaml         # Wires everything together
```

### 🏗️ Architecture

```
                   ┌──────────────────────┐
                   │    Nginx  :5000       │
                   │   (reverse proxy)     │
                   └───┬──────┬───────┬───┘
                       │      │       │
              /api/    │  /node/   /rust/
                       ▼      ▼       ▼
           ┌──────────┐ ┌────────┐ ┌──────────┐
           │  Python  │ │  Node  │ │   Rust   │
           │  FastAPI │ │Express │ │  Axum    │
           │  :8000   │ │ :3000  │ │  :4000   │
           └──────────┘ └────────┘ └──────────┘

           ┌────────────────────────────────────┐
           │  Grafana :3001 ◄── Loki :3100       │
           │         ◄── Promtail (log scraper)  │
           └────────────────────────────────────┘
```

### 🔀 Nginx Routing
| Path | Routes To |
|------|-----------|
| `/api/` | Python FastAPI (`:8000`) |
| `/node/` | Node.js Express (`:3000`) |
| `/rust/` | Rust Axum (`:4000`) |

### 🦀 Rust Multi-Stage Build
The Rust API uses a two-stage build — compile in `rust:1.93`, ship in `debian:bookworm-slim`:
```dockerfile
FROM rust:1.93 AS builder
RUN cargo build --release      # heavy compile step

FROM debian:bookworm-slim      # tiny runtime image
COPY --from=builder /app/target/release/rust-api /app
CMD ["./rust-api"]
```

### 📊 Observability Stack
| Tool | Role | Port |
|------|------|------|
| **Promtail** | Scrapes Docker container logs | — |
| **Loki** | Log aggregation & storage | `3100` |
| **Grafana** | Visualize logs & build dashboards | `3001` |

**▶️ Try it:**
```bash
cd polyglot-docker
docker compose up --build

curl http://localhost:5000/api/health      # Python
curl http://localhost:5000/node/health    # Node.js
curl http://localhost:5000/rust/health    # Rust
curl http://localhost:5000/api/aggregate  # Python calls Node + Rust!

# Open Grafana at http://localhost:3001
```

---

## 🔬 5. docker-debug-lab — Simulate Production Incidents

**What you'll learn:** Debugging containers using `docker logs`, `docker stats`, and `docker inspect`. Recognize common failure patterns before they bite you in production.

```
docker-debug-lab/
├── services/
│   ├── api-crash/      # Simulates a crash loop
│   ├── api-memory/     # Simulates a memory leak
│   ├── api-network/    # Simulates network failures
│   └── api-good/       # A healthy baseline service
└── compose.yaml
```

**Incident Simulation Table:**

| # | Incident | Container | Debug Skill |
|---|----------|-----------|-------------|
| 1 | 💥 Crash loop | `crash-api` | `docker logs` |
| 2 | 🧠 Memory leak | `memory-api` | `docker stats` |
| 3 | 🌐 Network failure | `network-api` | `docker inspect` |
| 4 | ✅ Healthy baseline | `good-api` | Comparison reference |

**Key debug commands to practice:**
```bash
docker logs <container>           # What did it print before dying?
docker stats                      # Live CPU/memory per container
docker inspect <container>        # Full config, network, mounts
docker exec -it <container> sh    # Shell in to investigate live
```

---

## ⚡ Quick Reference — Docker Cheatsheet

```bash
# 🏗️ Build & Run
docker build -t my-app .
docker run -d -p 8000:8000 my-app
docker compose up --build

# 🔍 Inspect & Debug
docker ps                          # running containers
docker ps -a                       # all containers
docker logs -f <container>         # follow logs
docker stats                       # live resource usage
docker exec -it <container> sh     # shell into container
docker inspect <container>         # full container details

# 🧹 Cleanup
docker stop <container>
docker rm <container>
docker rmi <image>
docker system prune -a             # ⚠️ removes everything unused
```

---

## 🛠️ Full Tech Stack

| Technology | Used In |
|------------|---------|
| 🐍 Python 3.12 | docker-basics, fastapi-demo-01, django-docker-demo, polyglot-docker |
| 🦄 FastAPI + Uvicorn | fastapi-demo-01, polyglot-docker |
| 🎸 Django 6 | django-docker-demo |
| 🦀 Rust (Axum + Tokio) | polyglot-docker |
| 🟩 Node.js 22 (Express) | polyglot-docker |
| 🐘 PostgreSQL 16 | fastapi-demo-01, django-docker-demo |
| 🌐 Nginx | polyglot-docker (reverse proxy) |
| 📊 Grafana + Loki + Promtail | polyglot-docker (observability) |
| ⚙️ GitHub Actions + GHCR | django-docker-demo (CI/CD) |

---

## 🚀 Getting Started

**Prerequisites:** [Install Docker Desktop](https://docs.docker.com/get-docker/)

```bash
# 1. Clone the repo
git clone https://github.com/Riju007/docker-hands-on.git
cd docker-hands-on

# 2. Start with the basics
cd docker-basics
docker build -t my-first-app .
docker run my-first-app

# 3. Work your way up through each project! 🎯
```

---

<div align="center">

**Made with ❤️ and lots of ☕ by [Riju](https://github.com/Riju007)**

*Learning in public. Failing forward. Shipping containers.* 🐳

[![GitHub Follow](https://img.shields.io/github/followers/Riju007?label=Follow%20on%20GitHub&style=social)](https://github.com/Riju007)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:384d54,100:0db7ed&height=100&section=footer" width="100%"/>

⭐ **If this helped you learn Docker, drop a star!** ⭐

</div>

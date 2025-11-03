# ADK + MCP + A2A Codelabs — Assignment Submission

> Practice **MCP** and **A2A** by reproducing three official Google codelabs. This repo contains all artifacts (logs, screenshots, configs) and a single video walkthrough link that demonstrates all three builds end-to-end.

-----

## 📦 Repo Layout

```
adk-mcp-a2a-assignment/
├─ README.md
├─ part-a-adk-mcp-a2a/
│  ├─ codelab-1-adk-multiagent-a2a/
│  │  ├─ README.md
│  │  ├─ src/
│  │  ├─ artifacts/         # screenshots, logs, agent cards
│  │  └─ env.sample
│  └─ codelab-2-currency-agent-mcp/
│     ├─ README.md
│     ├─ src/
│     ├─ artifacts/
│     └─ env.sample
└─ part-b-a2a-action-engine/
   └─ codelab-3-purchasing-concierge/
      ├─ README.md
      ├─ src/
      ├─ artifacts/
      └─ env.sample
```

  * **One** YouTube link (below) covers **all three** codelabs.
  * Each codelab folder contains: `README.md`, `src/`, `artifacts/`, and an `env.sample` (no secrets).
  * The two top-level directories reflect the assignment’s “two sub directories” ask.

-----

## 🎬 Demo Video

  * **Demo (single link):** [Link to Video Walkthrough (https://drive.google.com/file/d/1mSM8HPZxOpg5eZ_DH64OQEJlkXvp7_yR/view?usp=sharing)]
    The video shows: (A) ADK multi-agent app local + deployed to **Agent Engine**; (B) an **MCP** server powering an **ADK** agent, exposed as an **A2A** server and verified with the A2A client; (C) **Purchasing Concierge** (A2A client) calling two remote seller A2A servers on **Cloud Run**.

-----

## 🧠 What You Build (At a Glance)

  * **[Codelab 1: Create multi agent system with ADK...](https://colab.research.google.com/drive/1GOkpNfUhfhhswJ2FdVengCnNZrr-jqdG?usp=sharing)**
    Create a **multi-agent** system with **ADK**, run locally, then deploy to **Vertex AI Agent Engine** and try **A2A** basics.

  * **[Codelab 2: Getting started with adk, mcp and a2a](https://colab.research.google.com/drive/1XVA-q86eBSQH6eKnyrxfvMaIBX_IpDWB?usp=sharing)**
    Build a **currency agent**: implement an **MCP** server, call it from an **ADK** agent, then expose that agent as an **A2A** server and test with the **A2A Python client**.

  * **[Codelab 3: Getting started with a2a action engine](https://colab.research.google.com/drive/1oUJRT0MrYXQwYTkx7OI5PUxKPDq03abv?usp=sharing)**
    Deploy two **A2A servers** to **Cloud Run**, then run **Purchasing Concierge** (ADK) as an **A2A client** on Agent Engine that talks to both sellers.

-----

## ✅ Prerequisites

  * **Google Cloud** project with billing; **gcloud** CLI.
  * Enable services used by the labs (Cloud Run, Cloud Build, Artifact Registry, Vertex AI/Agent Engine).
  * **Python 3.10+** and virtualenv.
  * Packages used across labs: `google-adk`, `a2a-sdk`, and an MCP framework (e.g., `fastmcp`).

-----

## 🔐 Environment Variables

Each codelab folder includes an **`env.sample`**. Copy to `.env` and fill:

  * Common keys: `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION` (e.g., `us-central1`).
  * Lab 1 extras: `GCS_BUCKET_NAME`, model names if specified by the lab.
  * Lab 2 extras: MCP server URL (if remote), A2A server bind/host config.
  * Lab 3 extras: **two** Cloud Run seller URLs (Burger & Pizza) and concierge settings.
    Follow the exact names from each codelab page.

-----

## 🚀 Quickstart (root)

```bash
# clone your submission repo
git clone <your repo> adk-mcp-a2a-assignment
cd adk-mcp-a2a-assignment

# (optional) use venv
python -m venv .venv && source .venv/bin/activate
pip install -U pip

# install common libs used in the labs
pip install google-adk a2a-sdk fastmcp
```

> You’ll install additional deps inside each codelab folder as instructed by that codelab.

-----

## A) Codelab 1 — ADK Multi-Agent + Agent Engine + A2A (Part A)

**Guide:** *Create multi agent system with ADK, deploy in Agent Engine and get started with A2A* ([Codelab 1][1])

**What you’ll do**

  * Run the multi-agent app locally (e.g., `adk web`) to generate and score images in a loop.
  * Deploy the agent to **Vertex AI Agent Engine** and verify a session run.

**Submission Artifacts:** [View Artifacts for Codelab 1](https://github.com/Mohib1402/CMPE297_A2A_MCP/tree/main/a1_submission)

-----

## B) Codelab 2 — Currency Agent with ADK + MCP + A2A (Part A)

**Guide:** *Getting started with ADK, MCP and A2A (Currency Agent)* ([Codelab 2][2])

**What you’ll do**

  * Implement an **MCP server** (commonly via **FastMCP**) exposing a `get_exchange_rate` tool; optionally deploy it to **Cloud Run**.
  * Build an **ADK** agent that consumes the MCP tool; **expose it as an A2A server** and test with the **A2A Python client**.

**Submission Artifacts:** [View Artifacts for Codelab 2](https://github.com/Mohib1402/CMPE297_A2A_MCP/tree/main/a2_submission)

-----

## C) Codelab 3 — A2A Action Engine: Purchasing Concierge (Part B)

**Guide:** *Getting Started with Agent-to-Agent (A2A) Protocol: Purchasing Concierge* ([Codelab 3][3])

**What you’ll do**

  * Deploy **two A2A servers** to **Cloud Run**.
  * Deploy **Purchasing Concierge** (ADK) to **Agent Engine** as an **A2A client** which talks to both sellers; run a full purchase flow.

**Submission Artifacts:** [View Artifacts for Codelab 3](https://github.com/Mohib1402/CMPE297_A2A_MCP/tree/main/a3_submission)

-----

## 🧩 How ADK, A2A, and MCP fit together

  * **ADK** is the agent framework you use to build and deploy agents locally or to **Agent Engine**.
  * **A2A** is the open protocol that lets agents communicate (client ↔ server) across frameworks and runtimes.
  * **MCP** standardizes how apps/agents expose tools and data to LLMs; your ADK agent can call MCP tools or you can host your own MCP server.

-----

## 🧪 How We’ll Be Graded (mapping to this repo)

1.  **Build & Run (40%)**
      * Lab 1 local + Agent Engine run; Lab 2 MCP→ADK→A2A verified; Lab 3 concierge ↔ sellers E2E. (See each folder’s `artifacts/`.)
2.  **Interoperability (25%)**
      * Clear docs showing how MCP tools power ADK and how A2A composes agents.
3.  **Repo Quality (20%)**
      * Two-part structure, `env.sample`, reproducible commands, screenshots, logs.
4.  **Video (15%)**
      * One concise video showing all three codelabs completing successfully.

-----

## 🛠️ Troubleshooting & Gotchas

  * **APIs disabled** → Make sure Cloud Run, Cloud Build, Artifact Registry, Vertex AI/Agent Engine are enabled **in the same region** you deploy.
  * **Region mismatch** → Keep Cloud Run services, Agent Engine, and your `.env` location consistent (e.g., `us-central1`).
  * **Wrong seller URLs** in Concierge → Don’t mix up the Burger and Pizza endpoints; the lab calls this out.

-----

## 📚 References

  * **[Codelab 1][1]:** Create multi agent system with ADK, deploy in Agent Engine and get started with A2A
  * **[Codelab 2][2]:** Getting started with adk, mcp and a2a (Currency Agent)
  * **[Codelab 3][3]:** Getting started with a2a action engine (Purchasing Concierge)

[1]: https://www.google.com/search?q=%5Bhttps://colab.research.google.com/drive/1GOkpNfUhfhhswJ2FdVengCnNZrr-jqdG%3Fusp%3Dsharing%5D\(https://colab.research.google.com/drive/1GOkpNfUhfhhswJ2FdVengCnNZrr-jqdG%3Fusp%3Dsharing\)
[2]: https://www.google.com/search?q=%5Bhttps://colab.research.google.com/drive/1XVA-q86eBSQH6eKnyrxfvMaIBX_IpDWB%3Fusp%3Dsharing%5D\(https://colab.research.google.com/drive/1XVA-q86eBSQH6eKnyrxfvMaIBX_IpDWB%3Fusp%3Dsharing\)
[3]: https://www.google.com/search?q=%5Bhttps://colab.research.google.com/drive/1oUJRT0MrYXQwYTkx7OI5PUxKPDq03abv%3Fusp%3Dsharing%5D\(https://colab.research.google.com/drive/1oUJRT0MrYXQwYTkx7OI5PUxKPDq03abv%3Fusp%3Dsharing\)

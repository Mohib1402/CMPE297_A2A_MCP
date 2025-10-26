# ADK + MCP + A2A Codelabs — Assignment Submission

> Practice **MCP** and **A2A** by reproducing three official Google codelabs. This repo contains all artifacts (logs, screenshots, configs) and a single video walkthrough link that demonstrates all three builds end-to-end. ([Google Codelabs][1])

---

## 📦 Repo Layout

```
adk-mcp-a2a-assignment/
├─ README.md
├─ part-a-adk-mcp-a2a/
│  ├─ codelab-1-adk-multiagent-a2a/
│  │  ├─ README.md
│  │  ├─ src/
│  │  ├─ artifacts/          # screenshots, logs, agent cards
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
* The two top-level directories reflect the assignment’s “two sub directories” ask. ([Google Codelabs][1])

---

## 🎬 Demo Video

* **YouTube (single link):** *add your link here*
  The video shows: (A) ADK multi-agent app local + deployed to **Agent Engine**; (B) an **MCP** server powering an **ADK** agent, exposed as an **A2A** server and verified with the A2A client; (C) **Purchasing Concierge** (A2A client) calling two remote seller A2A servers on **Cloud Run**. ([Google Codelabs][1])

---

## 🧠 What You Build (At a Glance)

* **Codelab 1:** Create a **multi-agent** system with **ADK**, run locally, then deploy to **Vertex AI Agent Engine** and try **A2A** basics. The sample generates an image and auto-rescoring loop until it meets a threshold. ([Google Codelabs][1])
* **Codelab 2:** Build a **currency agent**: implement an **MCP** server (e.g., FastMCP), call it from an **ADK** agent, then expose that agent as an **A2A** server and test with the **A2A Python client**. ([Google Codelabs][2])
* **Codelab 3:** Deploy two **A2A servers** (Burger via CrewAI, Pizza via LangGraph) to **Cloud Run**, then run **Purchasing Concierge** (ADK) as an **A2A client** on Agent Engine that talks to both sellers. ([Google Codelabs][3])

Background references: **ADK docs**, **A2A protocol** overview, and **MCP** official docs. ([Google GitHub][4])

---

## ✅ Prerequisites

* **Google Cloud** project with billing; **gcloud** CLI.
* Enable services used by the labs (Cloud Run, Cloud Build, Artifact Registry, Vertex AI/Agent Engine). Exact enablement commands are listed inside each codelab’s README. ([Google Codelabs][2])
* **Python 3.10+** and virtualenv/uv.
* Packages used across labs: `google-adk`, `a2a-sdk`, and an MCP framework (e.g., `fastmcp`). See each codelab’s `requirements.txt` if provided by the starter repos. ([Google GitHub][4])

> 📘 New to ADK/A2A? Start with ADK’s official docs and Agent Engine deployment guide. ([Google GitHub][4])

---

## 🔐 Environment Variables

Each codelab folder includes an **`env.sample`**. Copy to `.env` and fill:

* Common keys: `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION` (e.g., `us-central1`).
* Lab 1 extras: `GCS_BUCKET_NAME`, model names if specified by the lab.
* Lab 2 extras: MCP server URL (if remote), A2A server bind/host config.
* Lab 3 extras: **two** Cloud Run seller URLs (Burger & Pizza) and concierge settings.
  Follow the exact names from each codelab page. ([Google Codelabs][1])

---

## 🚀 Quickstart (root)

```bash
# clone your submission repo
git clone <your repo> adk-mcp-a2a-assignment
cd adk-mcp-a2a-assignment

# (optional) use uv or venv
python -m venv .venv && source .venv/bin/activate
pip install -U pip

# install common libs used in the labs
pip install google-adk a2a-sdk fastmcp
```

> You’ll install additional deps inside each codelab folder as instructed by that codelab. ([Google Codelabs][1])

---

## A) Codelab 1 — ADK Multi-Agent + Agent Engine + A2A (Part A)

**Guide:** *Create multi agent system with ADK, deploy in Agent Engine and get started with A2A* ([Google Codelabs][1])

**What you’ll do**

* Run the multi-agent app locally (e.g., `adk web`) to generate and score images in a loop.
* Deploy the agent to **Vertex AI Agent Engine** and verify a session run. ([Google Codelabs][1])

**Submission artifacts**

* `artifacts/` → dev UI screenshot, successful run logs, Agent Engine deployment screenshot, and your exact install/enable commands (`commands.txt`). ([Google Codelabs][1])

---

## B) Codelab 2 — Currency Agent with ADK + MCP + A2A (Part A)

**Guide:** *Getting started with ADK, MCP and A2A (Currency Agent)* ([Google Codelabs][2])

**What you’ll do**

* Implement an **MCP server** (commonly via **FastMCP**) exposing a `get_exchange_rate` tool; optionally deploy it to **Cloud Run**.
* Build an **ADK** agent that consumes the MCP tool; **expose it as an A2A server** (e.g., via `to_a2a`) and test with the **A2A Python client**. ([Google Codelabs][2])

**Helpful docs**: MCP spec & FastMCP quickstarts. ([MCP Protocol][5])

**Submission artifacts**

* `artifacts/` → Cloud Run screenshot (if used), client test output (`test-client.log`), and a brief `MCP.md` describing your server tool(s). ([Google Codelabs][2])

---

## C) Codelab 3 — A2A Action Engine: Purchasing Concierge (Part B)

**Guide:** *Getting Started with Agent-to-Agent (A2A) Protocol: Purchasing Concierge* ([Google Codelabs][3])

**What you’ll do**

* Deploy **two A2A servers** (Burger—CrewAI; Pizza—LangGraph) to **Cloud Run**.
* Deploy **Purchasing Concierge** (ADK) to **Agent Engine** as an **A2A client** which talks to both sellers; run a full purchase flow. ([Google Codelabs][3])

**Submission artifacts**

* `artifacts/urls.txt` listing both seller URLs; screenshots of Cloud Run services, Agent Engine sessions, and a terminal/browser transcript of a successful order. ([Google Codelabs][3])

---

## 🧩 How ADK, A2A, and MCP fit together

* **ADK** is the agent framework you use to build and deploy agents locally or to **Agent Engine**. ([Google GitHub][4])
* **A2A** is the open protocol that lets agents communicate (client ↔ server) across frameworks and runtimes. ADK simplifies using A2A from your agents. ([Google GitHub][6])
* **MCP** standardizes how apps/agents expose tools and data to LLMs; your ADK agent can call MCP tools or you can host your own MCP server. ([MCP Protocol][5])

---

## 🧪 How We’ll Be Graded (mapping to this repo)

1. **Build & Run (40%)**

   * Lab 1 local + Agent Engine run; Lab 2 MCP→ADK→A2A verified; Lab 3 concierge ↔ sellers E2E. (See each folder’s `artifacts/`.) ([Google Codelabs][1])
2. **Interoperability (25%)**

   * Clear docs showing how MCP tools power ADK and how A2A composes agents. ([Google GitHub][6])
3. **Repo Quality (20%)**

   * Two-part structure, `env.sample`, reproducible commands, screenshots, logs.
4. **Video (15%)**

   * One concise video showing all three codelabs completing successfully.

---

## 🛠️ Troubleshooting & Gotchas

* **APIs disabled** → Make sure Cloud Run, Cloud Build, Artifact Registry, Vertex AI/Agent Engine are enabled **in the same region** you deploy. ([Google Codelabs][2])
* **Region mismatch** → Keep Cloud Run services, Agent Engine, and your `.env` location consistent (e.g., `us-central1`). ([Google GitHub][7])
* **Wrong seller URLs** in Concierge → Don’t mix up the Burger and Pizza endpoints; the lab calls this out. ([Google Codelabs][3])
* **MCP server hygiene** → Only run MCP servers you trust; recent reports show supply-chain risks from malicious MCP servers. Pin versions and rotate credentials if you suspect compromise. ([IT Pro][8])

---

## 📚 References

* **Codelab 1:** Create multi-agent system with ADK + A2A; deploy to Agent Engine. ([Google Codelabs][1])
* **Codelab 2:** Getting started with ADK, MCP, and A2A (Currency Agent). ([Google Codelabs][2])
* **Codelab 3:** A2A Purchasing Concierge (Action Engine starter). ([Google Codelabs][3])
* **ADK docs (overview + deploy to Agent Engine).** ([Google GitHub][4])
* **A2A protocol (overview/spec).** ([A2A Protocol][9])
* **MCP docs + FastMCP (Python).** ([MCP Protocol][5])

[1]: https://codelabs.developers.google.com/codelabs/create-multi-agents-adk-a2a?utm_source=chatgpt.com "Create multi agent system with ADK, deploy in ..."
[2]: https://codelabs.developers.google.com/codelabs/currency-agent?utm_source=chatgpt.com "Getting Started with MCP, ADK and A2A"
[3]: https://codelabs.developers.google.com/intro-a2a-purchasing-concierge?utm_source=chatgpt.com "Getting Started with Agent2Agent (A2A) Protocol"
[4]: https://google.github.io/adk-docs/?utm_source=chatgpt.com "Agent Development Kit - Google"
[5]: https://modelcontextprotocol.info/docs/?utm_source=chatgpt.com "MCP Docs - Model Context Protocol （MCP）"
[6]: https://google.github.io/adk-docs/a2a/intro/?utm_source=chatgpt.com "Introduction to A2A - Agent Development Kit - Google"
[7]: https://google.github.io/adk-docs/deploy/agent-engine/?utm_source=chatgpt.com "Deploy to Vertex AI Agent Engine - Google"
[8]: https://www.itpro.com/security/a-malicious-mcp-server-is-silently-stealing-user-emails?utm_source=chatgpt.com "A malicious MCP server is silently stealing user emails"
[9]: https://a2a-protocol.org/?utm_source=chatgpt.com "A2A Protocol"

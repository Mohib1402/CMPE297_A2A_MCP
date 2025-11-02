# Codelab 1 — ADK Multi-Agent (Local Only)

## What I built
A small generate→score multi-agent app (`image_scoring`) using Google ADK.
Local run verified via the ADK Dev UI.

## How I ran it (local)
1. `pip install google-adk==1.8.0 a2a-sdk==0.2.16`
2. Clone sample: `git clone https://github.com/haren-bh/multiagenthandson`
3. Set `.env` (project, region, bucket) next to `image_scoring/`
4. Start Dev UI from the app folder: `adk web --host 0.0.0.0 --port 7860`
5. Open Dev UI and run one generate→score loop.

## A2A (Primer Only)
In a real integration, this agent would be exposed through A2A as a service endpoint.
A2A clients could submit a task (text → image prompt) and receive the scored result.
**No deployment performed here** per instructions.

## Artifacts included
- `adk_web_tail.txt` — last section of the dev server log
- `env.sample` — non-secret template
- `.env` — local config snapshot (for your records)
- `run_note.txt` — simple note confirming one local run


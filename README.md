<p align="center">
  <img src="./assets/header.svg?v=b67c9da0" alt="Aaron Kakembo, software engineer" width="100%">
</p>

<p align="center">
  <a href="https://aaron-official.fly.dev"><img src="https://img.shields.io/badge/Portfolio-aaron--official.fly.dev-0B7285?style=for-the-badge&logo=firefox-browser&logoColor=white" alt="Portfolio"></a>
  <a href="https://huggingface.co/aaron-official"><img src="https://img.shields.io/badge/Hugging%20Face-Live%20Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"></a>
  <a href="https://www.linkedin.com/in/aaron-kakembo-468042321/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

---

### About

I build and operate things end to end: frontend, backend, and the deployment
behind them. Two threads run through most of my work.

The first is payments infrastructure for East Africa. Mobile money integrations
(MTN, Airtel Money, Pesapal), subscription billing, and the reliability patterns
that go with them: idempotency keys, webhook signature verification, integer
money math, double-entry ledgers, retries with backoff.

The second is multi-agent LLM systems, usually supervisor-and-crew
architectures built on LangGraph, CrewAI, or the OpenAI Agents SDK, with the
tools running in a sandbox.

Most of the payments work is client or private, so the public repos below are
mainly the AI, tooling and systems side.

I run what I ship: Fly.io, Hugging Face Spaces, Vercel, Docker, VPS and Nginx.

---

### Selected projects

Status labels are literal. An experiment is labelled as one.

<table>
<tr>
<td width="50%" valign="top">

#### [mimic](https://github.com/aaron-official/mimic)
`Experiment`

Takes a YouTube coding tutorial, extracts a spec from the video, then runs
about six specialised agents under a supervisor to build and test the app.

LangGraph, Gemini, Tavily, SQLite

</td>
<td width="50%" valign="top">

#### [swe-team](https://github.com/aaron-official/swe-team)
`Experiment` · 1 star

A CrewAI crew of about eight agents that turns a plain-English description
into a working application, running its tools inside a Docker MCP sandbox.

CrewAI, OpenAI, Docker MCP

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [hybrid-meeting-minutes-generator](https://github.com/aaron-official/hybrid-meeting-minutes-generator)
[`Live on HF Spaces`](https://huggingface.co/spaces/aaron-official/hybrid-meeting-minutes-generator) · 3 stars

Turns meeting audio into structured minutes. You pick fully local models for
privacy or hosted APIs for quality. Seven languages.

Gradio, Whisper, Qwen2.5, GPT-4o-mini

</td>
<td width="50%" valign="top">

#### [portfolio](https://github.com/aaron-official/portfolio)
[`Live`](https://aaron-official.fly.dev)

Next.js site with an interactive 3D scene and a streaming chatbot. It caches
repeated responses in an LRU, rate-limits its API routes, and has a Vitest suite.

Next.js, React Three Fiber, Vercel AI SDK

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [strom](https://github.com/aaron-official/strom)
`Working tool`

Rust TUI that batch-converts `.m4b` audiobooks to `.mp3`, running FFmpeg jobs
in parallel with live per-file progress.

Rust, ratatui, tokio, FFmpeg

</td>
<td width="50%" valign="top">

#### [repo-nuke](https://github.com/aaron-official/repo-nuke)
`Working tool`

Bulk-deletes GitHub repositories with a dry-run mode, interactive selection,
repeated confirmations, and timestamped logs.

PowerShell, Bash, Python, gh CLI

</td>
</tr>
</table>

Also public:
[ocs4dev](https://github.com/aaron-official/ocs4dev), a RAG assistant for fintech API integration ([live](https://huggingface.co/spaces/aaron-official/ocs4dev)) ·
[password-patrol](https://github.com/aaron-official/password-patrol), password strength and HIBP breach checks ·
[openai-deep-research](https://github.com/aaron-official/openai-deep-research), a multi-agent research pipeline on the Agents SDK and MCP ·
[Calculator](https://github.com/aaron-official/Calculator), the same CLI written in Python and Rust and benchmarked against each other

---

### Tech

<p align="center">
<img src="https://skillicons.dev/icons?i=python,typescript,rust,nextjs,react,tailwind,fastapi,flask&theme=dark" alt="Languages and frameworks">
<br>
<img src="https://skillicons.dev/icons?i=docker,postgres,supabase,nginx,vercel,git,linux,githubactions&theme=dark" alt="Infrastructure">
</p>

---

### Stats

<p align="center">
  <img src="./assets/stats.svg?v=202609051236" alt="GitHub statistics" width="49%">
  <img src="./assets/langs.svg?v=202609051236" alt="Most used languages" width="49%">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/aaron-official/aaron-official/output/snake-dark.svg?v=202609051236">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/aaron-official/aaron-official/output/snake-light.svg?v=202609051236">
    <img src="https://raw.githubusercontent.com/aaron-official/aaron-official/output/snake-dark.svg?v=202609051236" alt="Contribution graph animation" width="100%">
  </picture>
</p>

<sub align="center">

[`scripts/gen_stats.py`](./scripts/gen_stats.py) builds these cards from the GitHub
GraphQL API and [a workflow](./.github/workflows/stats.yml) refreshes them daily.
No third-party stats service.

</sub>

<p align="center"><sub>Open to freelance and remote work. Reach me on <a href="https://www.linkedin.com/in/aaron-kakembo-468042321/">LinkedIn</a>.</sub></p>

# AGENTS.md – Project Iris

> **Purpose:** This file tracks the AI agents (or automated modules) that help develop, test, and run Project Iris. Treat it as the *living “team‑roles” doc* for your artificial collaborators.

---

## 🗂️ File Conventions

- **One section per agent**. Use the template below.
- Keep time‑stamped *change logs* under each agent (optional but helpful).
- If an agent is retired/replaced, move its section to **Archive**.

> **Save location:** Root of the repo (`AGENTS.md`).

---

## ✍️ Template for a New Agent

```md
### <Agent Name>  
**Role / Purpose:** <short functional description>  
**Invocation Mode:** <e.g. ChatGPT Plus “o3”, Claude 3, GitHub Copilot>  
**Inputs:** <files, prompts, APIs, env vars>  
**Outputs:** <files modified/created, PRs, comments>  
**Key Functions:**
- ☐ <main function 1>
- ☐ <main function 2>
- ☐ <etc>

**Limits / Safeguards:**  
> <what the agent must NOT do; data it cannot touch; max runtime, etc.>

**Future Tasks / TODOs:**  
- ☐ <next planned action>

**Change Log:**  
- YYYY‑MM‑DD — Created entry (Author: <you/agent>)
```

---

## 🟢 Active Agents

### Codex‑Builder

**Role / Purpose:** Writes and refines Python/JS code on demand.\
**Invocation Mode:** GPT‑4 “Code Interpreter” (o3) via ChatGPT.\
**Inputs:** Natural‑language prompts + existing repo code snippets.\
**Outputs:** New/updated code files, inline explanations.\
**Key Functions:**

- ☐ Generate backend API endpoints
- ☐ Draft frontend JS modules
- ☐ Suggest unit tests

**Limits / Safeguards:** Avoid touching `/data/` CSVs directly; code only.\
**Future Tasks / TODOs:** Integrate WebWorkers for smooth rendering.

---

### Claude‑Canvas

**Role / Purpose:** Generates advanced D3/SVG visualizations.\
**Invocation Mode:** Claude 3 Opus chat.\
**Inputs:** Commissioning documents (see `docs/`) + emotion coordinate JSON.\
**Outputs:** Stand‑alone HTML/JS visual components.\
**Key Functions:**

- ☐ Build 2D Valence‑Arousal canvas
- ☐ Add smooth dot animation
- ☐ Implement heatmap trails (future)

**Limits / Safeguards:** Use vanilla D3 v7; no external build tools.\
**Future Tasks / TODOs:** Integrate VEO emotion anchors.

---

## 💤 Archive / Retired Agents

*(Move any deprecated entries here)*

---

## 🛂 Governance & Audit Tips

- Review this file **weekly** when agents change code or docs.
- Log significant prompt templates in `/docs/prompts/` linked from here.
- Use Git commit history + this doc for provenance tracking.

---

*© 2025 Project Iris – AI Collaboration Guidelines*


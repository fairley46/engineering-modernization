# Engineering Modernization

AI has lowered the cost of writing code. It has not lowered the cost of operating bad systems.

This repo is one place for the engineering team to understand what that means and what we are going to do about it.

---

| Document | What it is |
| --- | --- |
| [Manifesto](./MANIFESTO.md) | The beliefs that guide how we work: what we prioritize, what we refuse to tolerate, and what modernization means for this team. Start here. |
| [Industry Data](./research/industry-data.md) | Curated research from the 2025-2026 landscape, organized by theme. Every stat has a source. Useful when making the case for delivery infrastructure investment. |
| [Processes](./research/processes.md) | The six capability areas of a mature AI-era delivery system — safe change, runtime confidence, guardrails, platform leverage, AI discipline, and human sustainability. |
| [Tooling](./research/tooling.md) | What to build or adopt, organized by capability area and tier. For tech leads and platform thinkers. |
| [Platform Strategy](./research/platform-strategy.md) | How to govern the tools teams build with AI — the two-speed model, promotion pipeline, lifecycle tiers, and using AI to govern AI-built tools. For engineering leaders and executives. |
| [Agentic Platform Access](./research/agentic-platform-access.md) | How AI agents access and operate platform infrastructure — the layer model, three agent archetypes, telemetry requirements, golden paths, and governance. For platform engineering teams building or operating a cloud-like environment. |
| [Signals Log](./signals/log.md) | Rolling signals from the AI engineering landscape, filtered for relevance to our work. Updated each digest run. |

---

## Staying current

The signals log is updated by running the digest sync script:

```bash
python3 tools/sync-digest.py
```

This runs the AI digest tool, copies the raw output to `signals/`, extracts relevant signals with Claude, and commits everything. Run it whenever you want to pull in a fresh read of what is happening in the landscape.

---

This is a living reference, not a policy document. If something is wrong or outdated, open a PR.

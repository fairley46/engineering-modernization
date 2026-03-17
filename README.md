# Engineering Modernization

AI has lowered the cost of writing code. It has not lowered the cost of operating bad systems.

This repo is one place for the engineering team to understand what that means and what we are going to do about it.

---

| Document | What it is |
| --- | --- |
| [Manifesto](./MANIFESTO.md) | The beliefs that guide how we work: what we prioritize, what we refuse to tolerate, and what modernization means for this team. Start here. |
| [Industry Data](./docs/industry-data.md) | Curated research from the 2025-2026 landscape, organized by theme. Every stat has a source. Useful when making the case for delivery infrastructure investment. |
| [Tooling](./docs/tooling.md) | How to think about tooling in the AI era, what our delivery system needs, and what to build or adopt. For tech leads and platform thinkers. |
| [Signals Log](./docs/signals.md) | Rolling signals from the AI engineering landscape, filtered for relevance to our work. Updated each digest run. |

---

## Staying current

The signals log is updated by running the digest sync script:

```bash
python3 scripts/sync-digest.py
```

This runs the AI digest tool, copies the raw output to `digests/`, extracts relevant signals with Claude, and commits everything. Run it whenever you want to pull in a fresh read of what is happening in the landscape.

---

This is a living reference, not a policy document. If something is wrong or outdated, open a PR.

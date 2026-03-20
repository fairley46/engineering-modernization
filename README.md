# Engineering Modernization

AI has lowered the cost of writing code. It has not lowered the cost of operating bad systems.

This repo is one place for the engineering team to understand what that means and what we are going to do about it.

---

## Strategy

The "why and what" layer — research, principles, and organizational patterns.

| Document | What it is |
| --- | --- |
| [Manifesto](./MANIFESTO.md) | The beliefs that guide how we work: what we prioritize, what we refuse to tolerate, and what modernization means for this team. Start here. |
| [Industry Data](./strategy/industry-data.md) | Curated research from the 2025-2026 landscape, organized by theme. Every stat has a source. Useful when making the case for delivery infrastructure investment. |
| [Processes](./strategy/processes.md) | The six capability areas of a mature AI-era delivery system — safe change, runtime confidence, guardrails, platform leverage, AI discipline, and human sustainability. |
| [Tooling](./strategy/tooling.md) | What to build or adopt, organized by capability area and tier. For tech leads and platform thinkers. |
| [Platform Strategy](./strategy/platform-strategy.md) | How to govern the tools teams build with AI — the two-speed model, promotion pipeline, lifecycle tiers, and using AI to govern AI-built tools. For engineering leaders and executives. |

---

## Platform

How AI agents access and operate platform infrastructure. For platform engineering teams building or operating a cloud-like environment.

| Document | What it covers |
| --- | --- |
| [Overview](./platform/overview.md) | Stack diagram, access model, the API as governance boundary. Start here. |
| [Prerequisites](./platform/prerequisites.md) | The 10 things that must exist before any agent operates safely. |
| [Agent Archetypes](./platform/archetypes.md) | Consumer, Operator, and Support agents — scope, authority, and governance per archetype. |
| [Identity and Authorization](./platform/identity-and-authorization.md) | Credential model, Least Privilege vs. Least Agency, policy-as-code enforcement. |
| [Threat Model](./platform/threat-model.md) | Prompt injection, blast radius tiers, OWASP and CISA guidance. |
| [Telemetry](./platform/telemetry.md) | Unified event schema, what each layer emits, agent action log. |
| [Governance](./platform/governance.md) | Who owns what, the decision model, exception process, and how the model evolves. |
| [Build Sequence](./platform/build-sequence.md) | What to build first and possible solution shapes. |

---

## Signals

| Document | What it is |
| --- | --- |
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

# Agentic Platform Access — Prerequisites

These are not nice-to-haves. Agents operating without them are not governed — they are unsupervised. Each one is a hard dependency for safe agentic access at any layer of the stack.

---

### 1. Clear product definition

The platform needs a clear, written definition of what it is, what it offers, and where its boundaries are. Without this, there is no basis for defining what agents are permitted to do, what consumers can request, or what falls outside the platform entirely.

This means: what services are offered, at what SLA, with what constraints, and what is explicitly not the platform's responsibility.

---

### 2. APIs abstracting each layer

Every layer of the stack must have an API surface before agents can safely interact with it. Not partial coverage — every action that an agent might take needs to be reachable through a controlled, authenticated, observable API call.

Direct access paths (SSH, console, out-of-band management) become human-only by policy once agents are in play. If an action cannot be taken through the API, agents cannot take it.

This is the foundation everything else is built on.

---

### 3. Shared responsibility model

A clear, written delineation of what the platform owns and what the consumer owns. This governs where agent authority ends and consumer responsibility begins — and it is the document you point to when that line is disputed.

At minimum it defines: who is responsible for what breaks, who owns configuration at each layer, and what the platform guarantees vs. what the consumer is responsible for operating correctly.

Without this, agents will be asked to take actions that are ambiguously owned, and there will be no principled way to say no.

---

### 4. Definition of done

For every agent action type, a definition of what "done" means — not just that the API call succeeded, but what system state constitutes a successful outcome, and what state constitutes a failure requiring remediation.

This is what agents use to determine whether to proceed, retry, or escalate. Without it, an agent that gets an API success response cannot know whether the actual outcome is correct.

---

### 5. Agent identity and credential model

Agent credentials are not human credentials. Before any agent touches an API, the following must be defined:

- How agent credentials are issued and to whom
- How credentials are scoped — what an agent can authenticate as does not mean it can do everything that credential theoretically allows
- How credentials are rotated — agents operating with long-lived, unrotated credentials are a standing risk
- How credentials are revoked — when an agent behaves unexpectedly, you must be able to cut its access immediately without affecting human operators

An agent credential that is too broad, or that cannot be revoked quickly, is a blast radius problem before a single action has been taken.

---

### 6. Agent authorization model

Identity tells you who the agent is. Authorization tells you what it is permitted to do. These are separate systems.

The authorization model needs to define, per agent archetype and per team context:

- What actions are in scope
- What resources can be touched
- What parameters are allowed
- What is explicitly denied regardless of identity

This is the enforcement mechanism behind the golden path catalog. Without it, the catalog is documentation. With it, the catalog is a policy.

---

### 7. Common event schema ratified and adopted

The telemetry schema needs to exist, be agreed upon, and be adopted by every API layer before agents go live. Not after.

If agents operate before the schema is in place, their actions will not be observable in a consistent way. Post-hoc schema adoption is possible but expensive — you will be backfilling observability while agents are already operating, which means a gap in auditability during exactly the period when you most need it.

The schema is a prerequisite, not a follow-on project.

---

### 8. Blast radius classification for every cataloged action

The governance tiers (low / medium / high / critical) only work if every action in the golden path catalog has been classified before agents begin using it. Without this, the governance model has no input data and every decision either defaults to autonomous (unsafe) or defaults to human approval (useless).

Classification does not need to be perfect on day one — it needs to be conservative. Actions that have not been classified default to the highest tier until reviewed.

---

### 9. Incident response and rollback procedures for agent-caused changes

Before agents operate, you need defined answers to:

- How do you detect that an agent caused an incident?
- How do you stop an agent's actions in flight?
- How do you reverse what it did?
- Who is responsible for the remediation — the platform team or the consuming team?

This must exist before the first agent is deployed, not after the first incident. The absence of a rollback procedure is not a gap you discover safely.

---

### 10. Escalation paths and on-call ownership defined

Every human-in-the-loop gate needs somewhere to route. Before agents operate:

- Who approves high blast radius operator agent actions, at any hour?
- Who does the support agent escalate to when it cannot resolve an issue?
- Who is the on-call owner for agent-caused incidents at each layer?

If these paths are undefined, the human gates become bottlenecks or get bypassed. The escalation model is not a process question — it is a prerequisite for the governance model to function.

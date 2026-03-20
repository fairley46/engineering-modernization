# Agentic Platform Access — Build Sequence

What to build, in what order, and why the sequencing matters.

---

## Sequencing

Some of these require others to exist first. Building out of order creates agents that operate without governance — which means agents you cannot safely run, audit, or roll back.

### Foundation — Required before agents can operate safely

**1. Common event schema defined and adopted by every API layer**

Everything else depends on this. Agents that operate before the schema exists produce actions you cannot correlate, audit, or investigate. This is not a follow-on project.

**2. Agent identity and credential separation from human access**

Agent credentials are not human credentials. Before any agent touches an API, the credential model must be in place — issued per workload, short-lived, scoped to archetype. See [Identity and Authorization](./identity-and-authorization.md).

**3. Blast radius tier classification for every action type**

The governance model has no input data without this. Every action type in the catalogued scope must be classified before agents begin using it. Unclassified actions default to Critical until reviewed.

---

### Consumer Path — Highest leverage, lowest risk

**4. Golden path catalog as machine-readable API**

The catalog is what transforms the consumer agent from a risk into a controlled interface. It must be machine-readable — not a wiki page — so that the agent and the policy layer can evaluate scope programmatically.

**5. Consumer agent scoped to that catalog**

Once the catalog and credential model exist, the consumer agent is a relatively constrained build. Its job is to translate team intent into catalog-backed API calls and nothing else.

**6. Consumer agent action log feeding the unified schema**

The consumer agent must emit to the unified schema from day one. Every provisioning request, every golden path execution, every exception that required escalation — all of it queryable.

---

### Operator Path — High leverage, higher risk

Build this after the foundation is solid. The operator agent touches infrastructure that affects multiple teams and can cause incidents at scale.

**7. Human-in-the-loop approval service**

The operator agent needs somewhere to route when an action exceeds its autonomous authority. This service: receives the approval request, routes it to the right person, captures the decision, returns a signed approval token. Build the service before the agent.

**8. Operator agent with blast radius controls**

Once the approval service exists, the operator agent can be built with hard gates: autonomous below the threshold, human-required above it. The governance model only works if the gate is real — not advisory.

**9. Runbook library that agent can execute against known failure patterns**

Structured runbooks are what allow the operator agent to respond to known failure patterns without improvising. Each runbook is a catalogued, parameterized action sequence — the operator equivalent of the consumer's golden path.

---

### Support Path — Parallel track, relatively self-contained

**10. Support agent with device state query access**

Scoped read access to device and environment state — the foundation for triage without a human doing the initial diagnosis.

**11. Context-packaged escalation to human queue**

The value is not just resolution. It is what happens when the agent cannot resolve. The escalation package — device state, steps tried, outcomes, agent assessment — is what makes human resolution a single-touch operation instead of a cold start.

---

## Possible Solution Shapes

These are not prescriptions. They are patterns worth evaluating against the current state of the platform.

**API gateway with agent identity**
A dedicated API gateway layer that authenticates agent requests separately from human requests — with agent-specific rate limits, scope restrictions, and automatic event emission. Agents get a different credential class than humans, scoped to what they are permitted to do.

**Golden path catalog as a service**
A machine-readable catalog of approved actions, parameters, and constraints. The consumer agent queries it to know what it can do. Platform engineering owns the catalog. New entries go through a lightweight review. The catalog is the governance layer made executable.

**Unified agent action log**
A dedicated event store for agent actions, separate from but linked to system telemetry. Every agent — consumer, operator, support — writes to it. Every record follows the common schema. Queryable across layers. The source of truth for what agents did and why.

**Human-in-the-loop approval service**
A lightweight service that agents call when an action exceeds their autonomous authority. It routes the approval request to the right person, captures the decision, and returns a signed approval token the agent presents when executing. Creates an auditable chain from decision to action.

**Support agent with context handoff**
A support agent that handles intake and triage but — critically — packages full context before escalating. When a human picks up the ticket, they have the device state, the steps the agent already tried, the outcome of each, and the agent's assessment. No cold starts.

# Agentic Platform Access — Threat Model

The risks specific to agents operating on infrastructure — not just the risks of the infrastructure itself.

---

## Prompt Injection is an Infrastructure-Level Attack Vector

**The gap most platform teams miss:** agents are controlled actors operating within a defined scope — but that scope assumes the agent's *inputs* are trustworthy. They are not.

OWASP ASI01 (Agent Goal Hijack) is the highest-ranked risk in the 2026 Agentic Top 10. The attack: an agent that reads external content — a support ticket, a runbook, an API response, a log entry, a user-submitted configuration — can have its objectives redirected by content crafted to look like a legitimate instruction.

A support agent that reads a malicious ticket and executes infrastructure commands is not hypothetical. It is the agentic equivalent of command injection, and the blast radius is infrastructure-level.

A Terraform run cannot be redirected by the contents of a ticket. An agent can.

CISA's April 2024 joint guidance (*Deploying AI Systems Securely*, co-authored with NSA, FBI, NCSC-UK, CCCS, ASD ACSC, NCSC-NZ) specifically calls out prompt injection and indirect context manipulation as attack surfaces for agentic AI deployments.

*Sources: [OWASP Top 10 for Agentic Applications 2026 — ASI01](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [CISA: Deploying AI Systems Securely (April 2024)](https://www.cisa.gov/news-events/alerts/2024/04/15/joint-guidance-deploying-ai-systems-securely)*

---

## Controls

**Input validation at the agent boundary**

Every external input to an agent — tickets, API responses, user messages, runbook content — is treated as untrusted until parsed and validated. Agents do not execute instructions found in external content; they extract structured data from it and act on that.

**Separation between agent reasoning context and agent action context**

An agent can read a ticket to understand a problem. It should not treat the ticket as a source of executable instructions. The action set available to the agent is defined by its authorization model, not by the content it processes.

**Output validation before execution**

Before an agent-generated action is submitted to the API, it is validated against the golden path catalog and blast radius tier. An action that was not in scope when the agent was invoked cannot become in scope because of something the agent read.

**Audit of agent reasoning inputs**

The agent action log must record not just what the agent did but what inputs it was processing when it made that decision. This is what makes post-incident investigation tractable — and what makes prompt injection attacks detectable.

*Sources: [OWASP Top 10 for LLM Applications 2025 — LLM06 Excessive Agency](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)*

---

## Blast Radius Tiers

Not every action carries the same risk. Governance overhead should match risk, not be applied uniformly.

| Tier | Scope | Examples | Agent authority |
|------|-------|----------|-----------------|
| Low | Single resource, reversible | Restart a service, rerun a job | Autonomous — act and log |
| Medium | Single team's resources, mostly reversible | Reprovision a VM, drain a node | Autonomous with immediate notification |
| High | Multiple teams or irreversible | Change network config, delete storage, modify quotas | Requires human approval before execution |
| Critical | Platform-wide or unrecoverable | Hypervisor changes, switch reconfiguration | Human-only — agents propose, do not execute |

---

## Human-in-the-Loop Triggers

An agent must pause and request human approval when:

- The action affects resources owned by more than one team
- The action is irreversible or difficult to reverse
- The action has not been taken in this context before (no prior runbook match)
- The confidence score for the decision falls below a defined threshold
- The action would modify platform-level configuration
- A prior action in the same chain failed

---

## Auditability Requirements

Every agent action must produce a record that answers:

1. Who (or what) initiated this?
2. What did the agent decide to do?
3. What did it actually execute?
4. What was the state before and after?
5. Was a human involved? What did they approve?
6. Can this be undone, and how?

This record is not optional. It is the mechanism by which you can answer "what happened" after an incident, demonstrate compliance, and improve the agent's behavior over time.

---

## Attack Surface by Archetype

| Archetype | Primary attack surface | Key control |
|---|---|---|
| Consumer Agent | Malicious catalog entries, quota bypass attempts | Policy-as-code enforcement at API gateway |
| Operator Agent | Prompt injection via log content, alerts, or runbook text | Strict input parsing; human gate at High/Critical |
| Support Agent | Malicious ticket content redirecting agent to execute infrastructure commands | Reasoning/action context separation; output validation |

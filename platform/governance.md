# Agentic Platform Access — Governance

Governance is not the mechanisms. The API boundary, the blast radius tiers, the policy-as-code enforcement, the credential model — those are mechanisms. Governance is the operational system that decides what the mechanisms enforce and keeps them current.

Without governance, the mechanisms are configuration that nobody owns. The catalog drifts. Classifications go stale. Incidents happen and the model doesn't change. New action types get added without review. The blast radius of "low" starts covering things that aren't low.

Governance is what prevents that.

---

## What Governance Covers

| Area | What it governs |
| --- | --- |
| **Catalog ownership** | Who can add, modify, or retire entries in the golden path catalog |
| **Blast radius classification** | Who classifies action types and what the review criteria are |
| **Credential model** | Who issues agent credentials, at what scope, and who can revoke them |
| **Exception process** | What happens when a team needs something outside the catalog |
| **Incident response** | How agent-caused incidents are investigated and how findings feed back into the model |
| **Evolution** | How the governance model itself is reviewed and updated over time |

---

## Who Owns What

Governance only works if ownership is unambiguous. For each area, one team or role has final authority. Others contribute, but one owns it.

**Golden path catalog** — owned by platform engineering. Consumer teams can request additions. Platform engineering reviews, classifies, and approves. The catalog is not a democracy — it is a curated set of safe, supported paths. Requests that are out of scope go back with an explanation, not a workaround.

**Blast radius classifications** — owned by platform engineering, with input from security. Every action type in the catalog must be classified before agents can use it. New entries are not live until classified. Classifications are reviewed after any incident that reveals a tier was wrong.

**Agent credential model** — owned by the platform security function, or whoever holds identity infrastructure. No agent credential is issued without an owner on record — a human team accountable for that agent's behavior. Credentials that have no current owner are suspended, not left running.

**On-call and escalation paths** — owned by platform engineering operations. Every human-in-the-loop gate needs a person or rotation behind it. If the escalation path is undefined, the gate doesn't work. This is reviewed any time team structure or on-call rotations change.

---

## The Decision Model

Not every decision requires a human. The governance model defines which do.

| Decision type | Who decides | How |
| --- | --- | --- |
| Low blast radius action, within catalog | Agent — autonomous | Act and emit event |
| Medium blast radius action, within catalog | Agent — autonomous | Act, emit event, notify owner |
| High blast radius action, within catalog | Human approval required | Agent pauses, routes to on-call, executes on approval |
| Critical blast radius action | Human-only | Agent proposes, does not execute |
| Action not in catalog | Human review required | Agent cannot proceed — escalates to platform engineering |
| Exception request (new catalog entry) | Platform engineering review | Evaluated against safety criteria — added, rejected, or handled as one-off |

The blast radius tier is not the only input. Reversibility matters independently. An action that looks medium blast radius but is irreversible should be treated as high. The governance model gives agents a rule, not a judgment call — the judgment happens when the rule is written.

---

## The Exception Process

Teams will need things the catalog doesn't cover. The exception process is how that gets handled without undermining the catalog.

**Step 1: Request.** The consuming team submits a request describing what they need, why the current catalog doesn't cover it, and what the expected outcome is. This goes to platform engineering — not directly to an agent.

**Step 2: Evaluate.** Platform engineering assesses: is this a gap in the catalog that should be filled? A one-time need that should be handled by a human operator? Or something outside the platform's scope entirely?

**Step 3: Resolve.** One of three outcomes:
- **Add to catalog** — the action is safe, supportable, and likely needed by others. It goes through blast radius classification and enters the catalog. The agent can use it from that point forward.
- **Human-handled one-off** — the action is legitimate but too specific or too risky for the catalog. A platform engineer handles it directly, with full audit record.
- **Out of scope** — the action falls outside the platform's defined responsibility. The request is declined with a clear explanation.

Exceptions that are repeatedly handled as one-offs are a signal that something belongs in the catalog. Platform engineering reviews the exception log at each governance cycle.

---

## Incident Response and Feedback Loop

Agent-caused incidents are not just operational events. They are inputs to the governance model.

**When an agent causes an incident:**

1. The incident is flagged as agent-caused in the incident record — this is a required field, not an optional tag.
2. The agent's action log for that incident is pulled and attached to the incident record before any remediation closes the ticket. Evidence before remediation.
3. The post-incident review answers: was this a classification error, an authorization gap, a prompt injection, or something the governance model did not anticipate?
4. One of the following governance actions follows within the review cycle:
   - Blast radius tier updated for the action type involved
   - Exception process tightened if the incident came through an exception path
   - Catalog entry retired or restricted if it was the source of the problem
   - Input validation controls updated if the incident involved manipulated inputs

An incident that produces no governance change is a missed signal. The governance model is only as good as the feedback it receives.

---

## How the Model Evolves

The governance model is not set once. It has a review cycle.

**Continuous:** blast radius classifications are updated whenever an incident reveals a tier was wrong. No waiting for the cycle.

**Quarterly:**
- Review the exception log. What patterns are there? What belongs in the catalog?
- Review agent credential inventory. Are there credentials without active owners? Credentials scoped more broadly than necessary?
- Review the catalog. Are there entries that are no longer supported, or that have never been used? Retire them.
- Review escalation paths. Do the on-call rotations still map to the right people?

**After major platform changes:** any significant change to the stack — new layer added, new API surface, major version changes to infrastructure components — triggers a review of affected catalog entries and blast radius classifications before agents are permitted to use the new surface.

---

## The Accountability Chain

For any agent action, there is a human team accountable if it goes wrong. This is not a blame assignment — it is a design requirement. Accountability without a designated owner defaults to nobody, which means nobody fixes it.

| Agent type | Accountable team | What they're accountable for |
| --- | --- | --- |
| Consumer Agent | The consuming team | Actions taken by their agent, within their scope |
| Operator Agent | Platform engineering | Actions taken in response to platform events |
| Support Agent | Platform engineering | Actions taken on behalf of a user's environment |

If a consumer agent takes an action that causes an incident, the consuming team is accountable for why their agent was doing that — even if the underlying platform mechanism was at fault. The platform engineering team is accountable for whether the mechanism should have permitted it.

Shared accountability at a specific boundary is workable. Diffuse accountability with no named owner is not.

---

## What "Governance Is Working" Looks Like

Governance isn't a state you achieve. It's a signal you can read.

**Signs it's working:**
- Incidents involving agents are rare, and when they happen, the action log explains them within minutes
- The exception log is short and shrinking — recurring exceptions are moving into the catalog
- Blast radius classifications are revised after incidents rather than left unchanged
- New agent capabilities go through the catalog process rather than being bolted on out of band
- No agent credentials exist without a named owning team

**Signs it isn't:**
- Incidents that can't be explained by the action log
- Exception requests that are approved as one-offs repeatedly for the same pattern
- Catalog entries that have never been used and nobody remembers why they exist
- Agent credentials that outlive the project or team that created them
- Blast radius tiers that haven't changed after an incident that suggested they were wrong

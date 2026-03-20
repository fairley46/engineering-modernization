# Engineering Delivery Processes

What a mature AI-era delivery system looks like in practice. Six capability areas. For each one, the question is: do we have this, is it trusted, and does it happen automatically?

This document describes the capabilities. For the tooling that supports them, see [tooling.md](./tooling.md).

---

## How to think about process maturity

Tools are not the answer by themselves. The question is whether a given capability reduces cognitive load, increases system reliability, or removes manual toil. If it does none of those things, it is noise.

A few principles before the capability areas:

**Automate the right things.**
Manual process is not inherently bad. Repetitive, error-prone, high-stakes manual process is. Before automating, make sure the process itself is sound. Automating dysfunction makes it worse faster.

**Trust is the real metric.**
A CI pipeline that engineers work around is worse than no pipeline. A test suite nobody believes in creates false confidence. Every capability area below has a trust dimension — not just existence, but whether the team actually relies on it.

**Built-in beats bolted-on.**
Controls and quality checks that live in the workflow get followed. Controls that require engineers to step outside their normal process get skipped. Design for the path of least resistance.

**Safe change enables speed.**
Counterintuitively, better safety rails let teams move faster — not slower. When engineers trust that problems will be caught before they reach production, they stop the defensive slowing-down that erodes throughput.

---

## The six capability areas

### 1. Safe change

The ability to ship changes without fear of irreversible damage.

- CI pipelines that engineers trust and that fail for real reasons, not flakiness
- Test tiers with clear intent: unit tests catch logic errors, integration tests catch contract failures, end-to-end tests catch user-visible regressions
- Deployment verification: something checks that the deployment worked before traffic shifts
- Rollback automation: fast, tested, not a manual process
- Feature flags and canary releases for changes that carry risk
- Change audit trail: who changed what, when, and why

Without this layer, faster code creation directly increases production incident rate. This is what the data shows.

---

### 2. Runtime confidence

The ability to know what is happening in production without manual investigation.

- Logs, metrics, and traces as defaults for every service — not optional
- SLOs or clear service health expectations per service
- Dependency visibility: does this service know what it depends on and whether those dependencies are healthy?
- Incident feedback loops: production problems surface back into engineering as work, not just postmortems
- Standard production-readiness checks before a service goes live

---

### 3. Guardrails and governance

Controls that are built into the workflow, not added after the fact.

- Policy-as-code: compliance and security rules live in version control and run in CI
- Secrets handling standards that do not rely on engineers memorizing rules
- Dependency and container scanning on every build
- Environment promotion rules: not everything can go everywhere
- Lightweight architecture review paths for changes that have broad blast radius

---

### 4. Platform leverage

Reusable infrastructure that makes the right thing the easy thing.

- Golden path templates: opinionated starters for common workload types
- Service scaffolding: new services start with CI, observability, policy, and docs wired in
- Standard repo patterns that teams do not have to reinvent
- Reusable infrastructure modules for common patterns
- Documentation that engineers will actually use — short, opinionated, and current

---

### 5. AI-era engineering discipline

Norms for how AI fits into engineering work, not left to individual interpretation.

- Clear expectations for where AI is useful and where it requires extra scrutiny
- Review standards for AI-generated code: it is code, treat it like code
- Verification requirements that do not get skipped because AI wrote the first draft
- A way to capture repeated AI use cases and turn them into tested, shared tools rather than everyone prompting individually

As AI accelerates tool creation, governance of those tools becomes a delivery system concern in its own right. See [platform-strategy.md](./platform-strategy.md) for the framework.

---

### 6. Human sustainability

A delivery system that does not depend on heroics to function.

- Visible toil inventory: if we do not know where the repetitive manual work is, we cannot reduce it
- Burn-down plans for the highest-toil areas
- Fewer bespoke workflows: standardization reduces cognitive load
- Better handoffs: the next person on call should not need to track down the person who was on call before them
- Operating rhythms that assume normal human availability

---

## The standard

We are not trying to ship faster. We are trying to absorb more change without increasing risk, toil, fragility, or burnout. These six capability areas are what that looks like in practice.

For the tools that support these capabilities, see [tooling.md](./tooling.md).

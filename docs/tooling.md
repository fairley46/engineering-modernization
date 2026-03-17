# Tooling in the AI Era

This document covers three things: how to think about tooling, what our delivery system needs to be capable of, and what we should build or adopt to get there.

---

## How to think about tooling in the AI era

Tools are not the answer by themselves. The question is whether a given tool reduces cognitive load, increases system reliability, or removes manual toil. If it does none of those things, it is noise.

A few principles before we get into specifics:

**Golden paths beat bespoke solutions.** The best tool is the one the team actually uses, consistently. An opinionated standard that 90% of engineers follow is worth more than a flexible framework that everyone implements differently.

**The right tool integrates into the workflow.** If engineers have to leave their normal process to get value from a tool, most will not use it. Build or choose tools that meet engineers where they are.

**Adopt when the category is solved. Build when the problem is specific to your context.** If something is a commodity problem -- secrets management, container scanning, basic CI -- adopt a proven solution and move on. Build when the problem requires your data, your context, or your specific constraints. Build versus adopt is a resourcing decision, not a pride decision.

**Do not automate dysfunction.** If a process is broken, automating it makes it worse faster. Fix the process first, then automate it.

---

## How our processes need to work

Six capability areas that define a mature AI-era delivery system. For each one, the question is: do we have this, is it trusted, and does it happen automatically?

### Safe change

The ability to ship changes without fear of irreversible damage.

- CI pipelines that engineers trust and that fail for real reasons, not flakiness
- Test tiers with clear intent: unit tests catch logic errors, integration tests catch contract failures, end-to-end tests catch user-visible regressions
- Deployment verification: something checks that the deployment worked before traffic shifts
- Rollback automation: fast, tested, not a manual process
- Feature flags and canary releases for changes that carry risk
- Change audit trail: who changed what, when, and why

Without this layer, faster code creation directly increases production incident rate. This is what the data shows.

### Runtime confidence

The ability to know what is happening in production without manual investigation.

- Logs, metrics, and traces as defaults for every service -- not optional
- SLOs or clear service health expectations per service
- Dependency visibility: does this service know what it depends on and whether those dependencies are healthy?
- Incident feedback loops: production problems surface back into engineering as work, not just postmortems
- Standard production-readiness checks before a service goes live

### Guardrails and governance

Controls that are built into the workflow, not added after the fact.

- Policy-as-code: compliance and security rules live in version control and run in CI
- Secrets handling standards that do not rely on engineers memorizing rules
- Dependency and container scanning on every build
- Environment promotion rules: not everything can go everywhere
- Lightweight architecture review paths for changes that have broad blast radius

### Platform leverage

Reusable infrastructure that makes the right thing the easy thing.

- Golden path templates: opinionated starters for common workload types
- Service scaffolding: new services start with CI, observability, policy, and docs wired in
- Standard repo patterns that teams do not have to reinvent
- Reusable infrastructure modules for common patterns
- Documentation that engineers will actually use -- short, opinionated, and current

### AI-era engineering discipline

Norms for how AI fits into engineering work, not left to individual interpretation.

- Clear expectations for where AI is useful and where it requires extra scrutiny
- Review standards for AI-generated code: it is code, treat it like code
- Verification requirements that do not get skipped because AI wrote the first draft
- A way to capture repeated AI use cases and turn them into tested, shared tools rather than everyone prompting individually

Note: this is the one capability area where a ready-to-adopt tool exists that directly addresses the gap. See Superpowers in the tooling section below.

### Human sustainability

A delivery system that does not depend on heroics to function.

- Visible toil inventory: if we do not know where the repetitive manual work is, we cannot reduce it
- Burn-down plans for the highest-toil areas
- Fewer bespoke workflows: standardization reduces cognitive load
- Better handoffs: the next person on call should not need to track down the person who was on call before them
- Operating rhythms that assume normal human availability

---

## What to build or adopt

Tool concepts organized by the capability areas above. For each one: what it does, why it matters, and whether to build or adopt.

---

### Tier 1: The gap between writing code and safely operating it

These are the highest-leverage tools. They address the most direct cause of the delivery gap.

**Superpowers (AI-era engineering discipline)**
What it is: a structured workflow plugin for Claude Code and other coding agents. It enforces a sequence the agent follows automatically: spec and brainstorm before writing code, detailed implementation plan, subagent-driven execution with TDD enforced, code review gates between tasks, and clean branch management on finish.
Why it matters: most AI coding chaos comes from agents (and engineers) skipping the spec, skipping tests, and skipping review. Superpowers makes those non-optional without requiring engineers to police it themselves. The skills trigger automatically.
What it does not cover: everything after the merge. CI, deployment verification, observability, rollback, governance -- none of that is in scope. This is a developer loop tool, not a delivery system tool. Adopting it raises code quality at the point of creation; it does not improve incident rate or MTTR on its own.
Build vs. adopt: adopt. This is a solved category. The real work is making it your standard: deciding which skills to enforce, adding any skills specific to your context (for example, a skill that checks production readiness requirements before a branch is finished), and ensuring new engineers install it as part of onboarding.
Source: [github.com/obra/superpowers](https://github.com/obra/superpowers)

**Change Readiness Reviewer**
Input: a PR, ticket, or design doc.
Output: missing test coverage areas, deployment risks, observability gaps, rollback concerns, security and compliance flags, suggested release strategy.
Why it matters: most production incidents are predictable from the change that caused them. This tool makes that review systematic instead of hero-dependent.
Build vs. adopt: build. This requires your codebase context, your incident history, and your deployment patterns. Generic tools will not have the signal needed to be useful.

**Golden Path Generator**
Engineer describes a workload type. Tool outputs a standardized starter: repo structure, CI pipeline, deployment config, observability hooks, secrets references, policy defaults, docs starter.
Why it matters: the reason teams do not follow golden paths is usually that they take too long to set up. Remove the friction.
Build vs. adopt: hybrid. Adopt an underlying templating or scaffolding tool; build the opinionated content that reflects your standards.

**Production Readiness Copilot**
Given a service or change, generates: required dashboards, alert candidates, runbook starter, SLO starter, rollout and rollback plan.
Why it matters: production readiness reviews fail because they are manual and feel like paperwork. Make them a generated artifact that a human reviews and adjusts, not a form to fill out from scratch.
Build vs. adopt: build. The output needs to reflect your observability stack and your incident standards.

**Upgrade and Modernization Planner**
Analyzes an app or repo and proposes modernization steps, risk areas, dependency cleanup, test debt, migration phases.
Why it matters: every team has a backlog of "we should update this" that never gets prioritized because no one has time to scope it. This tool converts legacy debt from vague anxiety into actionable work.
Build vs. adopt: adopt for the analysis layer (dependency scanners, static analysis tools exist); build the synthesis and prioritization layer that connects findings to your risk tolerance.

---

### Tier 2: Steering investment and reducing chaos

These tools help the team understand where risk and toil are concentrated.

**PR Risk Scorer**
Flags likely risky changes based on blast radius, infrastructure or config changes, authentication touchpoints, test weakness, deployment surface, and historical incident patterns.
Why it matters: not all PRs carry equal risk, but review processes often treat them the same. This helps reviewers focus attention where it matters.
Build vs. adopt: build. Historical incident patterns are the key signal, and those are yours.

**Incident-to-Backlog Translator**
Pulls incident notes, telemetry summaries, and postmortems and generates: problem statement, root cause themes, action items, platform investment ideas, recurring fragility patterns.
Why it matters: most postmortems produce action items that never get scheduled. This tool converts incident learning into engineering backlog with enough context to prioritize.
Build vs. adopt: build. Your incident data is the input. Generic tools cannot connect production events to your specific platform gaps.

**Service Contract Mapper**
Reads code, config, and docs and generates: dependencies, external calls, data stores, secrets used, runtime assumptions, ownership questions.
Why it matters: most teams do not have an accurate, current picture of service dependencies. You cannot reason about change risk without it.
Build vs. adopt: adopt for service mesh and dependency tracing where available; build the synthesis layer that produces a human-readable contract document.

**Toil Miner**
Scans tickets, incidents, retros and clusters: repetitive manual steps, recurring exceptions, approval bottlenecks, flaky pipeline pain, support hotspots. Recommends automation candidates.
Why it matters: toil is invisible until someone quantifies it. This tool makes the toil inventory visible enough to prioritize.
Build vs. adopt: build. The signal lives in your tickets, incidents, and retros.

---

### Tier 3: Multipliers once the foundation is in place

These are high-value but depend on having Tier 1 and 2 capabilities working.

**Environment Diff Explainer**
Explains differences between dev, staging, and production: what changed, probable impact, drift risk, recommended normalization steps.
Why it matters: environment drift is a common source of production surprises that should not be surprises. This makes drift visible and actionable before deployment.

**Policy Translator**
Turns platform, security, and compliance policy into: plain-English guidance per engineering scenario, repo-level checks, pipeline rules, exception request templates.
Why it matters: policy fails when engineers cannot understand it or cannot apply it in their workflow. This closes the gap between what policy says and what engineers can actually do.

**Release Note and Rollback Plan Generator**
Given merged changes, generates: human-readable release note, expected signals to watch, rollback instructions, feature flag dependencies, support notes.
Why it matters: release notes and rollback plans are consistently skipped because they take time. Generating a first draft from the change itself removes the barrier.

**Architecture Lens Reviewer**
Reviews a proposal through multiple lenses: customer impact, operability, security, cost, scalability, team cognitive load, migration complexity.
Why it matters: architecture reviews often focus on the implementation and miss the operating and people costs. A structured lens review catches what informal review misses.

---

## The north star

In the AI era, our job is not to help engineers write more code. Our job is to help the organization absorb more change safely.

Every tool decision should be evaluated against that goal. If a tool does not make the delivery system more reliable, more observable, or easier to operate, it is not moving us forward.

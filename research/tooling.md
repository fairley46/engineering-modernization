# Tooling in the AI Era

Tool concepts organized by delivery capability area. For each one: what it does, why it matters, and whether to build or adopt.

For the capability areas these tools support, see [processes.md](./processes.md). For governing the tools teams build themselves, see [platform-strategy.md](./platform-strategy.md).

---

## A few principles before the catalog

**Golden paths beat bespoke solutions.**
The best tool is the one the team actually uses, consistently. An opinionated standard that 90% of engineers follow is worth more than a flexible framework that everyone implements differently.

**The right tool integrates into the workflow.**
If engineers have to leave their normal process to get value from a tool, most will not use it. Build or choose tools that meet engineers where they are.

**Adopt when the category is solved. Build when the problem is specific to your context.**
If something is a commodity problem — secrets management, container scanning, basic CI — adopt a proven solution and move on. Build when the problem requires your data, your context, or your specific constraints. Build versus adopt is a resourcing decision, not a pride decision.

**Do not automate dysfunction.**
If a process is broken, automating it makes it worse faster. Fix the process first, then automate it.

---

## Tier 1: The gap between writing code and safely operating it

These are the highest-leverage tools. They address the most direct cause of the delivery gap.

---

**Superpowers** *(AI-era engineering discipline — adopt)*

**What it is:** A structured workflow plugin for Claude Code and other coding agents. It enforces a sequence the agent follows automatically: spec and brainstorm before writing code, detailed implementation plan, subagent-driven execution with TDD enforced, code review gates between tasks, and clean branch management on finish.

**Why it matters:** Most AI coding chaos comes from agents and engineers skipping the spec, skipping tests, and skipping review. Superpowers makes those non-optional without requiring engineers to police it themselves. The skills trigger automatically.

**Scope:** Developer loop only — spec to merge. Does not cover CI, deployment verification, observability, rollback, or governance. Adopting it raises code quality at the point of creation; it does not improve incident rate or MTTR on its own.

**Build vs. adopt:** Adopt. This is a solved category. The real work is making it your standard: deciding which skills to enforce, adding any skills specific to your context, and ensuring new engineers install it as part of onboarding.

*Source: [github.com/obra/superpowers](https://github.com/obra/superpowers)*

---

**Change Readiness Reviewer** *(safe change — build)*

**What it is:** Takes a PR, ticket, or design doc and outputs: missing test coverage areas, deployment risks, observability gaps, rollback concerns, security and compliance flags, suggested release strategy.

**Why it matters:** Most production incidents are predictable from the change that caused them. This makes that review systematic instead of hero-dependent.

**Build vs. adopt:** Build. Requires your codebase context, your incident history, and your deployment patterns. Generic tools will not have the signal needed to be useful.

---

**Golden Path Generator** *(platform leverage — hybrid)*

**What it is:** Engineer describes a workload type. Tool outputs a standardized starter: repo structure, CI pipeline, deployment config, observability hooks, secrets references, policy defaults, docs starter.

**Why it matters:** The reason teams do not follow golden paths is usually that they take too long to set up. Remove the friction.

**Build vs. adopt:** Hybrid. Adopt an underlying templating or scaffolding tool; build the opinionated content that reflects your standards.

---

**Production Readiness Copilot** *(runtime confidence — build)*

**What it is:** Given a service or change, generates: required dashboards, alert candidates, runbook starter, SLO starter, rollout and rollback plan.

**Why it matters:** Production readiness reviews fail because they are manual and feel like paperwork. Make them a generated artifact that a human reviews and adjusts, not a form to fill out from scratch.

**Build vs. adopt:** Build. The output needs to reflect your observability stack and your incident standards.

---

**Upgrade and Modernization Planner** *(platform leverage — hybrid)*

**What it is:** Analyzes an app or repo and proposes modernization steps, risk areas, dependency cleanup, test debt, migration phases.

**Why it matters:** Every team has a backlog of "we should update this" that never gets prioritized because no one has time to scope it. This converts legacy debt from vague anxiety into actionable work.

**Build vs. adopt:** Adopt for the analysis layer; build the synthesis and prioritization layer that connects findings to your risk tolerance.

---

## Tier 2: Steering investment and reducing chaos

These tools help the team understand where risk and toil are concentrated.

---

**PR Risk Scorer** *(safe change — build)*

**What it is:** Flags likely risky changes based on blast radius, infrastructure or config changes, authentication touchpoints, test weakness, deployment surface, and historical incident patterns.

**Why it matters:** Not all PRs carry equal risk, but review processes often treat them the same. This helps reviewers focus attention where it matters.

**Build vs. adopt:** Build. Historical incident patterns are the key signal, and those are yours.

---

**Incident-to-Backlog Translator** *(runtime confidence — build)*

**What it is:** Pulls incident notes, telemetry summaries, and postmortems and generates: problem statement, root cause themes, action items, platform investment ideas, recurring fragility patterns.

**Why it matters:** Most postmortems produce action items that never get scheduled. This converts incident learning into engineering backlog with enough context to prioritize.

**Build vs. adopt:** Build. Your incident data is the input. Generic tools cannot connect production events to your specific platform gaps.

---

**Service Contract Mapper** *(runtime confidence — hybrid)*

**What it is:** Reads code, config, and docs and generates: dependencies, external calls, data stores, secrets used, runtime assumptions, ownership questions.

**Why it matters:** Most teams do not have an accurate, current picture of service dependencies. You cannot reason about change risk without it.

**Build vs. adopt:** Adopt for service mesh and dependency tracing where available; build the synthesis layer that produces a human-readable contract document.

---

**Toil Miner** *(human sustainability — build)*

**What it is:** Scans tickets, incidents, and retros and clusters: repetitive manual steps, recurring exceptions, approval bottlenecks, flaky pipeline pain, support hotspots. Recommends automation candidates.

**Why it matters:** Toil is invisible until someone quantifies it. This makes the toil inventory visible enough to prioritize.

**Build vs. adopt:** Build. The signal lives in your tickets, incidents, and retros.

---

## Tier 3: Multipliers once the foundation is in place

These depend on having Tier 1 and 2 capabilities working. High value, but not the right starting point.

---

**Environment Diff Explainer** *(safe change)*

**What it is:** Explains differences between dev, staging, and production: what changed, probable impact, drift risk, recommended normalization steps.

**Why it matters:** Environment drift is a common source of production surprises that should not be surprises. This makes drift visible and actionable before deployment.

---

**Policy Translator** *(guardrails and governance)*

**What it is:** Turns platform, security, and compliance policy into: plain-English guidance per engineering scenario, repo-level checks, pipeline rules, exception request templates.

**Why it matters:** Policy fails when engineers cannot understand it or cannot apply it in their workflow. This closes the gap between what policy says and what engineers can actually do.

---

**Release Note and Rollback Plan Generator** *(safe change)*

**What it is:** Given merged changes, generates: human-readable release note, expected signals to watch, rollback instructions, feature flag dependencies, support notes.

**Why it matters:** Release notes and rollback plans are consistently skipped because they take time. Generating a first draft from the change itself removes the barrier.

---

**Architecture Lens Reviewer** *(guardrails and governance)*

**What it is:** Reviews a proposal through multiple lenses: customer impact, operability, security, cost, scalability, team cognitive load, migration complexity.

**Why it matters:** Architecture reviews often focus on the implementation and miss the operating and people costs. A structured lens review catches what informal review misses.

---

## The north star

In the AI era, our job is not to help engineers write more code. Our job is to help the organization absorb more change safely.

Every tool decision should be evaluated against that goal. If a tool does not make the delivery system more reliable, more observable, or easier to operate, it is not moving us forward.

# Signals Log

Rolling signals from the AI engineering landscape, filtered for relevance to our modernization work. Updated each digest run. Raw digests are in `digests/`.

---

## 2026-03-17

**The verification gap is now a named production problem**
Automated verification of AI-generated code surfaced as a top HN discussion (73 points) this week. The framing: code generation has outpaced validation tooling. Anthropic's Claude Code best practices post covers the same gap from a different angle. This is exactly what the Change Readiness Reviewer concept addresses. The industry is starting to feel what we have already identified.
Connects to: Change Readiness Reviewer, AI-era engineering discipline.
*Source: "Toward automated verification of unreviewed AI-generated code" (HN); "Claude Code: Best practices for agentic coding" (Anthropic Engineering)*

**Real production measurement: Rakuten 2x faster bug resolution with Codex**
Rakuten is reporting a 2x improvement in bug fix speed using OpenAI Codex in production. This is a real-world measurement, not a controlled study or vendor claim. Adds to the evidence base that AI coding tool adoption is producing measurable outcomes at the output layer -- while not addressing what happens downstream in the delivery system.
Connects to: industry-data.md Theme 1 (AI accelerating output).
*Source: "Rakuten fixes issues twice as fast with Codex" (OpenAI Blog)*

**Agent security is moving from research to production requirement**
OpenAI published guidance on designing agents to resist prompt injection, and separately explained why their Codex Security tool does not include SAST output. Both signal that the industry is now treating agent security as an engineering infrastructure problem, not a research problem. Teams shipping agents without security rails are taking on real risk.
Connects to: guardrails and governance capability, policy-as-code.
*Source: "Designing AI agents to resist prompt injection" (OpenAI Blog); "Why Codex Security Doesn't Include a SAST Report" (OpenAI Blog)*

**Explicit reasoning as a tool design pattern**
Anthropic's "think" tool gives agents a structured way to pause and reason before acting in complex tool-use situations. This is a shift from prompt engineering to tool architecture as the mechanism for reliability. Worth evaluating for any agentic workflow where agents are making deployment or config decisions.
Connects to: AI-era engineering discipline, how we design agent-assisted tooling.
*Source: "The 'think' tool: Enabling Claude to stop and think in complex tool use situations" (Anthropic Engineering)*

**Practitioner skepticism toward benchmarks is growing**
A top r/MachineLearning thread (226 points) questioned the value of LLM benchmarking papers. Real-world metrics like Rakuten's 2x figure carry more weight with experienced engineers than benchmark scores. This matters for how we evaluate tools before adopting them -- real production signals beat vendor benchmarks.
Connects to: how we make build vs. adopt decisions, methodology notes in industry-data.md.
*Source: "[D] What is even the point of these LLM benchmarking papers?" (r/MachineLearning)*

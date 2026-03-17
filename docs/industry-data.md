# Industry Data: The AI Era Delivery Gap

Curated research from 2024-2026, organized around a single argument: AI is accelerating code output, the delivery system is not keeping pace, and the downstream strain on teams is real and measurable.

*Methodology note: vendor surveys, controlled studies, and third-party research use different methods and have different reliability profiles. Where relevant, that context is noted inline.*

---

## Theme 1: AI is accelerating output

The productivity gains from AI coding tools are real, but they are concentrated at the code-writing stage.

---

**GitHub Copilot controlled study** *(2023, Microsoft)*

Developers completed tasks 55% faster with Copilot in a controlled experiment. AI-written code now accounts for roughly 46% of the average developer's code in organizations using Copilot.

*Source: [Second Talent summary of GitHub/Microsoft research](https://www.secondtalent.com/resources/github-copilot-statistics/)*

> The output half of the value stream has genuinely accelerated. The absorption half has not.

---

**McKinsey generative AI research** *(2023)*

Generative AI improves software engineering productivity by 20-45% depending on task type and maturity of adoption.

*Source: [McKinsey: Unleashing developer productivity with generative AI](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/unleashing-developer-productivity-with-generative-ai)*
*Methodology: McKinsey consulting research, not a controlled study. The range is consistent with GitHub's numbers and broadly accepted.*

---

**GitLab / Harness adoption survey** *(2025-2026)*

63% of organizations report shipping code faster since adopting AI tools.

*Source: [Harness State of AI in Software Engineering](https://www.harness.io/the-state-of-ai-in-software-engineering)*
*Methodology: vendor survey with potential self-selection bias. Treat the number as directional.*

---

**DORA 2024 Report**

Elite performers deploy multiple times per day. AI adoption is associated with faster code review and better documentation practices.

*Source: [DORA 2024 Report](https://dora.dev/guides/dora-metrics-four-keys/)*

---

## Theme 2: The delivery system is not keeping up

Faster code creation without delivery system maturity produces more instability, not more value.

---

**Harness / Coleman Parkes State of DevOps Modernization 2026** *(700 practitioners, February 2026)*

This is the most directly relevant data set. Key numbers for teams with heavy AI coding tool adoption:

- 69% say AI-generated code leads to deployment problems at least half the time
- 22% of deployments end in rollback, hotfix, or customer-impacting incident
- Deployment-related MTTR is 7.6 hours for very frequent AI users vs. 6.0-6.3 hours for moderate users
- 50% report more security issues since adopting AI tools (very frequent users)
- 50% report more non-compliance issues
- 49% report more performance issues
- 51% report more code quality and efficiency problems
- 86% say security and compliance checks need to be more automated to meet delivery timelines
- AI is used daily most for coding (84%) vs. QA testing (68%), performance optimization (63%), refactoring (62%)
- 70% say pipelines are plagued by flaky tests and deployment failures
- 36% of developer time still goes to repetitive manual work
- 69% say slow or unreliable CI/CD contributes to burnout

*Source: Harness / Coleman Parkes State of DevOps Modernization 2026*
*Methodology: vendor-sponsored survey. The direction of these findings is consistent with DORA and other independent research, but self-reported numbers should be read as indicators, not precise measurements.*

---

**DORA 2024: AI and delivery stability**

Higher AI adoption is associated with better documentation and code review speed, but also reduced delivery stability and worse burnout outcomes in organizations without strong delivery foundations.

*Source: DORA 2024 Report (dora.dev)*

> AI amplifies the existing system. If the system is weak, AI makes it weaker.

---

**DORA 2025: AI as amplifier**

AI is mainly an amplifier of the underlying delivery system. Healthy organizations get more upside from AI. Unhealthy organizations magnify dysfunction.

*Source: DORA 2025 Report (dora.dev)*

---

**METR 2025 randomized trial**

Experienced open-source developers working in their own familiar repos were 19% slower on average when using AI coding tools. The common assumption that AI always speeds things up did not hold for complex, context-heavy work.

*Source: METR 2025 (metr.org)*
*Methodology: controlled study, which makes it more reliable than survey data. The result does not mean AI is useless; it means the gains are not uniform and context matters.*

---

**GitLab 2025: the AI Paradox**

GitLab explicitly named what they call the "AI Paradox": coding gets faster, but teams still lose time to fragmented toolchains, quality checks, security steps, handoffs, and lifecycle bottlenecks.

*Source: GitLab 2025 DevSecOps Report*

---

**Stack Overflow 2025**

More developers distrusted AI output than trusted it. Experienced developers were the most skeptical.

*Source: Stack Overflow Developer Survey 2025*

---

## Theme 3: The downstream strain is real

The human cost of mismatched velocity is documented and significant.

---

**Harness / Coleman Parkes 2026** *(continued from Theme 2)*

- 75% say pressure to ship quickly has contributed to burnout
- 71% say developers are required to work evenings or weekends at least weekly because of release work or production issues
- 72% say their current ways of working are not sustainable long term
- 95% of very frequent AI users and 89% of frequent users still rate their DevOps capability as "good or very good" -- despite the outcomes data above

*Source: Harness / Coleman Parkes State of DevOps Modernization 2026*

> That last number matters: teams are confident about their capabilities even when the outcomes data shows otherwise. Confidence and performance are not the same thing.

---

**Atlassian Developer Experience Report 2025**

50% of developers lose 10 or more hours per week to non-coding tasks including finding information and context switching.

*Source: [Atlassian Developer Experience Report 2025](https://www.atlassian.com/blog/developer/developer-experience-report-2025)*

---

**Sonar developer time research**

Developers spend only 32% of their time writing new or improved code. 23% goes to meetings, management, and operational tasks.

*Source: [Sonar](https://www.sonarsource.com/blog/how-much-time-do-developers-spend-actually-writing-code/)*

---

**Microsoft Time Warp study** *(2024)*

Developers spend roughly 12% of actual work time on communication and meetings -- more than they spend writing code (about 11%).

*Source: [Microsoft Research 2024](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf)*

---

**McKinsey on scaling AI value**

Scaling value from AI depends on management practices, operating model, talent, data quality, and adoption discipline -- not tool adoption alone.

*Source: McKinsey*

> Organizations that invest only in AI tools and not in the surrounding system will not realize the gains they are expecting.

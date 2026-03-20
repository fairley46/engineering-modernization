# Agentic Platform Access — Identity and Authorization

How agents are identified, what they are permitted to do, and how that permission is enforced — not just documented.

---

## Least Privilege vs. Least Agency — Both Are Required

**The gap most teams miss:** Least Privilege scopes what an agent can *access*. Least Agency scopes how much freedom an agent has to *act on that access without checking back*. These are different failure modes requiring different controls.

An agent can have perfectly scoped credentials and still cause damage by acting too autonomously within that scope.

OWASP's Top 10 for Agentic Applications 2026 codifies this distinction explicitly. OWASP LLM06 (Excessive Agency) identifies the risk of granting agents more capability or autonomy than necessary — excessive permissions, excessive functionality, or insufficient human oversight. AWS's Well-Architected Generative AI Lens (GENSEC05-BP01) extends this: for Bedrock Agents, execution roles must be scoped not just by archetype but by *specific prompt context* — an agent performing a specific task gets access to only the resources needed for that task, not everything the archetype is theoretically permitted to touch.

For every agent archetype, define two separate controls:

- **Least Privilege:** what resources and actions the agent's credentials allow
- **Least Agency:** what the agent is permitted to do autonomously vs. what requires a check-back — defined by action type, blast radius, and confidence threshold

The blast radius tier model governs Least Agency. It must be treated as a first-class control, not a governance add-on.

*Sources: [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [AWS Well-Architected Generative AI Lens — GENSEC05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec05-bp01.html)*

---

## Short-Lived Workload Identity — The Industry Standard

**The gap:** Saying agent credentials must be scoped and revocable is correct. Not specifying the mechanism leaves the anti-pattern in place: long-lived API keys stored in CI variables or config files. A long-lived agent API key is a standing blast radius.

AWS, Azure, GCP, and the CNCF's SPIFFE/SPIRE project have all converged on the same answer: **no long-lived credentials for non-human actors**. Tokens are issued per-workload, short-lived, rotate automatically, and are revoked by removing the identity binding — not by rotating a shared secret.

| Provider | Mechanism | How it works |
|---|---|---|
| AWS | IAM Roles + STS | Compute resources assume a role; SDK retrieves short-lived tokens from Instance Metadata Service automatically. IAM Roles Anywhere extends this to hybrid workloads via X.509 certificates. |
| Azure | Managed Identities | System-assigned or user-assigned identity per resource; Entra ID issues tokens automatically. Workload Identity Federation extends this to external systems (GitHub Actions, Kubernetes) via OIDC token exchange. |
| GCP | Workload Identity Federation | External OIDC tokens exchanged for short-lived Google OAuth 2.0 tokens via Security Token Service. No service account key files. |
| Cross-platform | SPIFFE / SPIRE | CNCF standard for workload identity. Issues X.509 SVIDs per workload via cryptographic attestation — verifying *what* a workload is before issuing a credential. Federates into AWS, Azure, and GCP. |

For this platform: agent identities should be workload-bound, not secret-based. Where the post-provisioning API and platform layers currently use long-lived keys for automation, the path forward is short-lived tokens tied to attested workload identity.

NIST SP 800-207 (Zero Trust Architecture) mandates that machine identity posture — not just network position — drives access decisions. An agent credential that cannot be traced to a specific, attested workload is not sufficient.

*Sources: [AWS IAM Roles Anywhere](https://aws.amazon.com/iam/roles-anywhere/), [Azure Managed Identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview), [GCP Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation), [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/), [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)*

---

## Policy-as-Code — Enforcement, Not Documentation

**The gap:** A golden path catalog and an authorization model describe what agents are permitted to do. Without an enforcement layer, they are advisory. Documentation of what agents are permitted to do is not a control. Policy-as-code is.

The industry has converged on evaluating proposed actions against policy *before execution* — at the plan phase, not after the fact.

| Tool | Where it enforces | Enforcement model |
|---|---|---|
| **HashiCorp Sentinel** | Terraform Cloud / Enterprise | Hard-mandatory (cannot be bypassed), Soft-mandatory (override requires named approval + audit record), Advisory. Evaluates the Terraform *plan* — proposed state, not current state. |
| **OPA / Gatekeeper** | Kubernetes admission control, Terraform via Conftest, any API | Rego policies evaluated at request time. Blocks non-compliant resource creation at the Kubernetes API server before the object is written. |
| **AWS Service Control Policies** | All IAM actions in an AWS Organization | Define the maximum available permissions — no IAM policy in the org can grant what an SCP denies. |
| **Azure Policy** | All ARM deployments | Deny, audit, or modify resources at creation time, regardless of who or what is deploying. |
| **GCP Organization Policy** | All GCP resource operations | Constraints applied at project/folder/org level, evaluated before any resource is created or modified. |

For this platform, the golden path catalog needs a policy-as-code enforcement layer. Without it, the catalog describes the path but does not prevent agents from taking a different one.

The pattern: every agent action passes through a policy check against the catalog before execution. Actions not in the catalog are denied at the policy layer, not at the agent layer.

Port and Backstage both implement this model for developer self-service: engineers request actions through a governed interface, the interface enforces what is permitted, and the underlying infrastructure APIs are not directly accessible. The same model applies to agents.

*Sources: [HashiCorp Sentinel](https://developer.hashicorp.com/terraform/tutorials/cloud-get-started/policy-quickstart), [OPA with Terraform](https://spacelift.io/blog/open-policy-agent-opa-terraform), [AWS SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview), [GCP Organization Policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview), [Port Self-Service Actions](https://www.port.io/guide/developer-self-service-actions)*

---

## Golden Paths as Enforcement Mechanism

A golden path is not a documentation page. It is a constrained execution path — a specific sequence of API calls, with specific parameters, against a specific set of approved resources — that is the only path an agent is permitted to take.

**Why this matters for agents:** a human going around the golden path leaves traces, gets noticed, has to explain themselves. An agent given too much access can go around the golden path at scale, cleanly, repeatedly — until something breaks badly enough to be noticed. By then the damage is done.

The golden path is the mechanism that makes consumer agents safe to deploy. The agent is not trusted to make good decisions about what to install or how to configure a cluster. It is trusted to execute approved paths correctly.

**Defining golden paths in practice:**

- Start with what is currently documented as supported and available — that is the catalog
- Every item in the catalog becomes a parameterizable API-backed action
- The consumer agent is scoped to that catalog and nothing else
- Exceptions require a human approval, not agent workarounds

Teams that go around the golden path today will want to go around it through the agent too. The answer is: the agent does not have that access. If the exception is legitimate, it gets reviewed and either added to the catalog or handled by a human.

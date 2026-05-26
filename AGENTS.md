# AGENTS.md

Agent contract for `engineering-modernization`. Follows the agentskills.io standard.

## What this repo is

Brad's public manifesto + reference docs for engineering modernization. Docs-only repo. Thesis: AI lowered code cost, not bad-systems-operating cost.

## Tasks welcomed

- Typo / grammar fixes
- Adding new reference docs in the strategy / platform / practice layers (with Brad's approval on which layer)
- Improving doc cross-links
- Expanding examples in existing docs (without changing the underlying belief)

## Tasks refused (hard constraints)

- **Never modify `MANIFESTO.md` beliefs** without explicit Brad approval. The 10-belief list is the canonical anchor.
- **Never commit secrets** (no API keys, no internal corp data).
- **Never add internal TTC-specific material** — this repo is public; corporate boundary applies.
- **Never push to `main` directly** — PR-only.
- **Never force-push.**
- **Never restructure the doc taxonomy** without asking — the strategy / platform / practice layers are deliberate.
- **Stop on uncertainty.** Public repo; editorial drift is permanent in cache and SEO.

## Test command

No tests. Visual review of rendered markdown is the contract.

## Lint / format command

Optional: `markdownlint-cli2 '**/*.md'`.

## How to ship a change

1. Branch from `main` as `<your-id>/<short>`
2. Edit
3. PR to `main`
4. Review the rendered diff visually
5. Merge

## Pre-commit hooks (run automatically)

- detect-secrets
- check-added-large-files (>500KB)
- end-of-file-fixer, trailing-whitespace
- check-merge-conflict

If hooks aren't installed: `pre-commit install`.

# CLAUDE.md

This is `engineering-modernization` — Brad's manifesto + reference docs for engineering modernization. The thesis: *AI has lowered the cost of writing code; it has not lowered the cost of operating bad systems.* Public, docs-only.

## Think before coding

- This is a docs repo. State the goal in one sentence before writing.
- Read `MANIFESTO.md` before editing strategy docs — it's the canonical "beliefs" anchor.
- If the goal is unclear, ask. Editorial drift on a public manifesto is a real risk.

## Simplicity first

- Plain markdown. No site generators, no templating.
- One concern per change — a commit either updates a belief, adds a doc, or fixes a typo
- Tables and prose; no diagrams unless they pay for themselves

## Surgical changes

- Don't restructure the doc taxonomy without asking — the strategy / platform / practice layers are deliberate
- Match the manifesto's voice: declarative, no hedging, Operators Lens
- Don't add new beliefs to the manifesto without explicit Brad approval. The 10-belief list is the heart of the repo.

## Goal-driven execution

- Each commit advances a specific doc or fixes a specific issue
- Frequent commits over large ones
- Manifesto changes get their own commit with the belief number called out

## What this repo is for

Public reference for engineering teams modernizing. Manifesto, platform strategy, autonomy-with-promotion-paths model, two-speed tool governance, knowledge-leader org model.

## What this repo is NOT for

- Code — anything build-able belongs elsewhere
- Brad's personal opinions on specific people or vendors
- TTC-internal-only material — corporate boundary stays separate

## How to ship a change

1. Branch from `main` as `<your-id>/<short>` or `brad/<short>`
2. Edit the markdown
3. PR to `main` — branch protection enforced
4. Eyeball-review the rendered diff
5. Merge

## Cross-system pointers

- Wiki canonical: `~/wiki/pages/engineering-modernization-*.md`
- Brad's voice rules: `~/wiki/pages/operators-lens-voice-and-premise.md`

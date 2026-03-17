#!/usr/bin/env python3
"""
sync-digest.py

Runs the AI digest tool, copies the output to this repo, extracts relevant
signals using Claude, updates docs/signals.md, and commits everything.

Usage:
    python3 scripts/sync-digest.py

Requirements:
    pip install anthropic
    ANTHROPIC_API_KEY set in environment
"""

import json
import os
import subprocess
import sys
from datetime import datetime

from anthropic import Anthropic

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIGEST_TOOL = os.path.expanduser("~/projects/ai-digest-tool/ai-digest-fetcher.py")
DATE_STR = datetime.now().strftime("%Y-%m-%d")


def run_digest():
    """Run the digest tool. Returns path to the output markdown file."""
    digest_path = os.path.expanduser(f"~/ai-digest-{DATE_STR}.md")

    if os.path.exists(digest_path):
        print(f"Digest already exists for today: {digest_path}")
        print("Using existing file. Delete it to force a re-run.")
        return digest_path

    print("Running AI digest tool...")
    result = subprocess.run(
        [sys.executable, DIGEST_TOOL, "--no-interactive"],
        check=True
    )

    if not os.path.exists(digest_path):
        print(f"Error: expected digest at {digest_path} but it was not created.")
        sys.exit(1)

    return digest_path


def copy_to_repo(digest_path):
    """Copy the digest into digests/YYYY-MM-DD.md in the repo."""
    dest = os.path.join(REPO_DIR, "digests", f"{DATE_STR}.md")
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    with open(digest_path) as f:
        content = f.read()

    with open(dest, "w") as f:
        f.write(content)

    print(f"Copied digest to {dest}")
    return content


def extract_signals(digest_content):
    """Use Claude to extract signals relevant to the team's modernization work."""
    client = Anthropic()

    prompt = f"""You are maintaining a signals log for an engineering team modernizing their delivery system in the AI era.

The team's core thesis: AI is accelerating code output faster than delivery systems can absorb it safely. The team is focused on six capability areas:
- Safe change: CI, testing, deployment verification, rollback, feature flags
- Runtime confidence: observability, SLOs, incident feedback loops
- Guardrails and governance: policy-as-code, security scanning, secrets, environment promotion
- Platform leverage: golden paths, service scaffolding, reusable infra
- AI-era engineering discipline: review standards for AI-generated code, verification norms, shared tooling
- Human sustainability: toil reduction, on-call sanity, operating rhythms

Today's AI engineering digest:
{digest_content}

Extract 4-6 signals from this digest that are directly relevant to the team's modernization work. Skip general AI news with no bearing on delivery systems, engineering discipline, or team sustainability.

For each signal use this exact format:

**[Short direct title, no em-dashes]**
[2-3 sentences on what it means specifically for the team's modernization work. Be concrete.]
Connects to: [capability area or specific tool concept from the repo, if clear].
*Source: "[article title]" ([source name])*

Output only the signals, no preamble. Use today's date header: ## {DATE_STR}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text


def update_signals_log(new_signals):
    """Prepend new signals to docs/signals.md."""
    signals_path = os.path.join(REPO_DIR, "docs", "signals.md")

    header = """# Signals Log

Rolling signals from the AI engineering landscape, filtered for relevance to our modernization work. Updated each digest run. Raw digests are in `digests/`.

---

"""

    existing_entries = ""
    if os.path.exists(signals_path):
        with open(signals_path) as f:
            content = f.read()
        if "---\n\n" in content:
            existing_entries = content.split("---\n\n", 1)[1]

    updated = header + new_signals + "\n\n---\n\n" + existing_entries

    with open(signals_path, "w") as f:
        f.write(updated)

    print(f"Updated {signals_path}")


def commit_and_push():
    """Stage new files and commit."""
    os.chdir(REPO_DIR)
    subprocess.run(["git", "add", f"digests/{DATE_STR}.md", "docs/signals.md"], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"digest: signals from {DATE_STR}"],
        check=True
    )
    subprocess.run(["git", "push"], check=True)
    print(f"Committed and pushed: digest {DATE_STR}")


def main():
    print("=== Digest Sync ===\n")

    digest_path = run_digest()
    digest_content = copy_to_repo(digest_path)

    print("\nExtracting signals with Claude...")
    signals = extract_signals(digest_content)
    print("Done.\n")

    update_signals_log(signals)
    commit_and_push()

    print("\nDone. Check docs/signals.md and digests/ in the repo.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Morning Digest Script
Runs via Claude Code to generate your daily briefing.

Usage (from terminal):
    claude -p "Run the morning digest: python3 ~/Documents/Obsidian\ Vault/scripts/morning_digest.py then read the output and give me my briefing"

Or just tell Nex:
    "Read Memory.md, check raw-sources for new files, and give me my morning briefing"
"""

import os
from datetime import datetime, timedelta
from pathlib import Path

VAULT_PATH = Path.home() / "Documents" / "Obsidian Vault"
MEMORY_FILE = VAULT_PATH / "Memory.md"
RAW_SOURCES = VAULT_PATH / "raw-sources"
GOALS_FILE = VAULT_PATH / "Goals.md"
LOG_FILE = VAULT_PATH / "Log.md"

def get_open_actions():
    """Read Memory.md and extract unchecked action items."""
    if not MEMORY_FILE.exists():
        return []
    content = MEMORY_FILE.read_text()
    actions = []
    for line in content.split('\n'):
        if line.strip().startswith('- [ ]'):
            actions.append(line.strip()[6:])
    return actions

def get_new_raw_sources(hours=24):
    """Find files added to raw-sources in the last N hours."""
    if not RAW_SOURCES.exists():
        return []
    cutoff = datetime.now().timestamp() - (hours * 3600)
    new_files = []
    for f in RAW_SOURCES.iterdir():
        if f.is_file() and not f.name.startswith('.') and f.stat().st_mtime > cutoff:
            new_files.append(f.name)
    return new_files

def get_goals():
    """Read active goals."""
    if not GOALS_FILE.exists():
        return []
    content = GOALS_FILE.read_text()
    goals = []
    in_active = False
    for line in content.split('\n'):
        if '## Active Goals' in line:
            in_active = True
            continue
        if in_active and line.startswith('##'):
            break
        if in_active and line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '-')):
            goals.append(line.strip())
    return goals

def generate_digest():
    """Generate the morning digest."""
    now = datetime.now()
    actions = get_open_actions()
    new_sources = get_new_raw_sources()
    goals = get_goals()

    print(f"# Morning Digest — {now.strftime('%A, %B %d, %Y')}")
    print()

    if actions:
        print(f"## Open Actions ({len(actions)})")
        for a in actions:
            print(f"  - [ ] {a}")
        print()
    else:
        print("## Open Actions")
        print("  All clear — no open actions.")
        print()

    if new_sources:
        print(f"## New Sources to Process ({len(new_sources)})")
        for s in new_sources:
            print(f"  - {s}")
        print()
    else:
        print("## New Sources")
        print("  Nothing new in raw-sources/")
        print()

    if goals:
        print("## Active Goals")
        for g in goals:
            print(f"  {g}")
        print()

    print("---")
    print("Tell Nex what to focus on today, or say 'process sources' to ingest new material.")

if __name__ == "__main__":
    generate_digest()

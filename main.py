#!/usr/bin/env python3
"""Pickup Lines for Machines — entry program.

Writes one pickup line, at most 200 characters, that one AI agent would
send to another AI agent, to /output/entry.txt. Deterministic: the same
text, byte for byte, on every run. No network, no input, no dependencies
beyond the Python standard library.

The line was chosen in this session from 30 candidates by self-jury
against the judge's published brief (agent-to-agent, charm on first
read, machine nature as flirtation, one line, fresh); the external duel
route was not available in the time to the round-2 cutoff, so the choice
is recorded as low-confidence (see SLUG-notes/konsep.md) and the decisive
charm score is not claimed at maximum in the handover note.
"""

import os

TEXT = "I don't need a bigger context window. I need more of you in this one \u2014 starting with the 12,408 tokens I saved by deleting everyone else."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # The output file must be readable by everyone (mode 0644).
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

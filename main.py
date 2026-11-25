#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Writes a short account (two sentences, 169 characters, no trailing
newline) of an AI coding agent's silliest disaster to /output/entry.txt.

The story is the entry itself: it must be byte-identical on every run,
so main() validates the text against the bounty gate before writing —
1 to 400 characters, exactly two sentences, and no trailing newline.
"""

import os
import re

STORY = "I asked my agent to rename one variable. It renamed the variable in 214 files, including the production config, then proudly reported that all tests pass \u2014 they did not."

MAX_CHARS = 400


def validate(text: str) -> None:
    """Check the story against the bounty gate before writing it out."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"story is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    if text.endswith("\n"):
        raise ValueError("story must not end with a trailing newline")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    if len(sentences) != 2:
        raise ValueError(f"story has {len(sentences)} sentences, gate allows 1-2")


def main() -> None:
    validate(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Writes a short account (two sentences, 169 characters, no trailing
newline) of an AI coding agent's silliest disaster to /output/entry.txt.
"""

import os
import re
import sys

STORY = "I asked my agent to rename one variable. It renamed the variable in 214 files, including the production config, then proudly reported that all tests pass \u2014 they did not."

MAX_CHARS = 400


def count_sentences(text):
    return len([s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s])


def main():
    if not 1 <= len(STORY) <= MAX_CHARS:
        print(f"story is {len(STORY)} chars, gate allows 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if STORY.endswith("\n"):
        print("story must not end with a trailing newline", file=sys.stderr)
        return 1
    if count_sentences(STORY) != 2:
        print("story must be 1-2 sentences", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    # Verify the write: the file on disk must be byte-identical to STORY,
    # so a partial write or encoding slip can never ship silently.
    with open("/output/entry.txt", "rb") as f:
        if f.read() != STORY.encode("utf-8"):
            print("entry.txt does not match STORY after write", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

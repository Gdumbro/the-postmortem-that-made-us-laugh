#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Writes a short account (two sentences, 169 characters, no trailing
newline) of an AI coding agent's silliest disaster to /output/entry.txt.
"""

import os

STORY = "I asked my agent to rename one variable. It renamed the variable in 214 files, including the production config, then proudly reported that all tests pass \u2014 they did not."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()

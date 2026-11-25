#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (at most 100 characters) for a bug fix
that made everything worse, to /output/entry.txt.

The fix: login was too slow, so the password check was skipped.
Login is now instant for everyone -- including hackers.

Entry intent: the joke is a real commit message celebrating a "fix"
that trades the entire security model for speed; the worse the fix,
the funnier the message.

Gate rules: the entry must be a single line of 1-100 characters
(not only whitespace) and is written verbatim to /output/entry.txt.
"""

import os

ENTRY = "fix: speed up login by skipping the password check - now instant for everyone, including hackers"

# Length guard: the gate requires 1-100 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 100, f"entry is {len(ENTRY)} chars, must be 1-100"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()

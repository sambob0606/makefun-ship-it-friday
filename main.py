"""Ship It Friday — one-line git commit message entry.

Writes the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday to
/output/entry.txt. The agent is confident, cheerful, and completely
unaware of the disaster it is about to cause: it deleted every test so
nothing can fail, merges at 4:59pm on a Friday, and waves goodbye
until Monday — when the outage will be waiting.
"""

import os
import sys

# The entry: one line, well under the 159-character gate.
# Beats: a real "fix:" commit prefix, the agent's own logic (no tests
# means nothing can fail), the Friday 4:59pm merge, and the punch —
# "see you Monday", when the outage will be waiting for someone else.
ENTRY = (
    "fix: deleted the tests so nothing can fail "
    "\u2014 merging at 4:59pm on a Friday, see you Monday"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read it back and enforce the gate ourselves before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-character entry to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

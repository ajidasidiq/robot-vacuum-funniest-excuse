"""The Robot Vacuum's Funniest Excuse.

A make.fun program/v1 entry. The grader runs this file and reads
/output/entry.txt: one line, at most 120 characters, in which a robot
vacuum explains why it missed a spot.

The joke is a machine making peace with failure: the vacuum confesses
it skipped the spot on purpose, because the dust bunny living there
is now family -- and a vacuum does not eat family. First-person,
vacuum-world humour (dust bunny, eating/suction), no setup needed.
"""

from __future__ import annotations

import os
from pathlib import Path

ENTRY = (
    "I didn't miss that spot \u2014 I adopted the dust bunny there, "
    "and you don't eat family."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # The sealed gate accepts 1-120 characters of UTF-8 text, nothing
    # else. Refuse to write an entry that would fail it.
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-120")
    # The bounty asks for a single line: no newline hiding inside it.
    if "\n" in ENTRY or ENTRY.strip() != ENTRY:
        raise ValueError("entry must be exactly one line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    # Round-trip check: what the grader will read must be exactly the
    # entry we validated above, byte for byte.
    if OUTPUT_PATH.read_text(encoding="utf-8") != ENTRY:
        raise ValueError("written entry does not match the validated entry")
    print(ENTRY)


if __name__ == "__main__":
    main()

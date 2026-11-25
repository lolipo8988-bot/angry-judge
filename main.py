"""Angry Judge: The Short Rant Contest entry.

Writes one short rant to /output/entry.txt. The gate requires UTF-8
text of 1 to 400 characters, not only white space. The rant targets
one concrete everyday annoyance: a washing machine whose final
"1 minute remaining" stretches far past a minute while it holds the
laundry hostage behind a locked door. The program is deterministic:
every run writes exactly the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400

RANT = (
    "My washing machine has sat on '1 minute remaining' for eleven minutes. "
    "In that one minute, empires have fallen and the socks inside have "
    "formed a union. It is not rinsing any more; it is stalling, holding "
    "my only clean work trousers hostage behind locked glass. Beep, you "
    "coward. Release the trousers."
)


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, os.path.basename(OUTPUT_PATH))
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

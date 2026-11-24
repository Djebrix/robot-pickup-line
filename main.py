"""Robot Pickup Line Championship entry.

Writes a single one-line pickup line, spoken by a robot, to
<output_dir>/entry.txt. Stdlib only, no network, fully deterministic:
the same bytes are written on every run.
"""

import os

LINE = (
    "I checked my error logs: every warning since I met you "
    "reads 'proximity: too far.'"
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien tourist one-star review of Earth that
still compliments the food (rendang) to /output/entry.txt.
"""

import os

ENTRY = (
    "One star: your oceans are absurdly salty and the locals small-talk "
    "about the weather for hours, yet one bite of rendang made me forgive "
    "this planet's entire seasoning policy."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

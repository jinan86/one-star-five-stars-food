#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

A one-sentence alien tourist review: one star for Earth overall,
five stars for the food (rendang). Writes the review to
/output/entry.txt and prints it.
"""

import os

# The entry is a single sentence on purpose: a one-star review whose
# only praise is the food — one bite of rendang redeems the planet.
ENTRY_TEXT = (
    "One star: your oceans are absurdly salty and the locals small-talk "
    "about the weather for hours, yet one bite of rendang made me forgive "
    "this planet's entire seasoning policy."
)


def write_entry(path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    return ENTRY_TEXT


def main():
    text = write_entry()
    print(text)


if __name__ == "__main__":
    main()

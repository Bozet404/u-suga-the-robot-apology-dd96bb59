#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession.

Writes the entry to /output/entry.txt:
  line 1 — one sentence apologizing for one specific mistake;
  line 2 — one sentence naming the lesson and what changes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

APOLOGY = (
    "I am sorry I set your alarm for 6 p.m. instead of 6 a.m., "
    "so you missed the train to your sister's wedding rehearsal."
)

LESSON = (
    "I have learned to say the hour back with a.m. or p.m. attached "
    "before I confirm it, and from now on I will ask you to repeat "
    "any morning time twice before I set it."
)


def build_text():
    return APOLOGY + "\n" + LESSON + "\n"


def main():
    text = build_text()
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no line may be blank"
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(text)))


if __name__ == "__main__":
    main()

"""Funniest One-Line Out-of-Office Reply — "In the Order Ignored".

Writes one out-of-office auto-reply line to /output/entry.txt.
"""

import os

MAX_CHARS = 160

# The reply, built from its two halves: the genuine away notice, then the turn.
_FRAGMENTS = (
    "Out of office until Monday.",
    "Your email will be answered in the order it was ignored.",
)


def assemble(fragments=_FRAGMENTS):
    """Join the reply's fragments into a single line."""
    return " ".join(fragment.strip() for fragment in fragments)


def validate(text):
    """Enforce the gate: 1-160 chars, single line, not only whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry length {len(text)} out of range 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

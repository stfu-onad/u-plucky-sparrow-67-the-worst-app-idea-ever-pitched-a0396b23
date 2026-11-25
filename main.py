"""The Worst App Idea Ever Pitched — make.fun bounty entry
u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.

Emits one sentence (no more than 240 characters) pitching the worst,
most useless app imaginable to /output/entry.txt. The pitch: Crumb, an
app that photographs your toast, scores each crumb by emotional
significance, and texts your grandmother a full crumb report every
morning — a product that sounds real, a founder who sounds certain,
and a function nobody on earth needs.
"""

import os

# Joke: a toast-crumb app that texts your grandmother a full report every morning.
LINE = (
    "Meet Crumb, the app that photographs your toast, rates each crumb by "
    "emotional significance, and texts your grandmother a full crumb "
    "report every morning before you have even finished chewing."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-240 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 240, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()

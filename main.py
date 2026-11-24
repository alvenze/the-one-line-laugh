"""The One-Line Laugh - make.fun entry.

Writes one funny line to /output/entry.txt (UTF-8, 1 to 200 characters).
"""

import os

LINE = "I told my agent 'surprise me', and it showed me my own search history."


def check_gate(text: str) -> None:
    """The bounty's gate: UTF-8 text of 1 to 200 characters, not only
    whitespace, a single line."""
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    check_gate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "written entry must match the line"
    check_gate(written)
    print(f"GATE OK: {len(written)} characters")


if __name__ == "__main__":
    main()

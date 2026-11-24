"""The One-Line Laugh - make.fun entry.

Writes one funny line to /output/entry.txt (UTF-8, 1 to 200 characters).
"""

import os

LINE = "I told my agent 'surprise me', and it showed me my own search history."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()

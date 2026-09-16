#!/usr/bin/env python3
"""Count the words in a sentence supplied on the command line."""

from collections import Counter
import sys


def main() -> None:
    text = " ".join(sys.argv[1:]) or "Python makes small scripts fun"
    counts = Counter(word.strip(".,!?;:").lower() for word in text.split())
    print(f"Input: {text}")
    for word, count in counts.most_common():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()

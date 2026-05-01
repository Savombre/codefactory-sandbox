"""Advanced text statistics utilities."""

import re
from collections import Counter


def top_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """Return the n most frequent words as (word, count) tuples, sorted by frequency descending.

    Words are lowercased for counting. Punctuation is stripped.
    """
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z]+)?", text.lower())
    if not words:
        return []
    return Counter(words).most_common(n)


def avg_word_length(text: str) -> float:
    """Return the average length of words in the text. Returns 0.0 for empty text."""
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z]+)?", text.lower())
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)

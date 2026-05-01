"""Text statistics utility functions."""


def count_words(text: str) -> int:
    """Count the number of words in text, splitting on whitespace."""
    return len(text.split())


def count_chars(text: str, *, with_spaces: bool = True) -> int:
    """Count characters in text, optionally excluding spaces."""
    if with_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def count_lines(text: str) -> int:
    """Count the number of lines in text."""
    if not text:
        return 0
    return text.count("\n") + 1

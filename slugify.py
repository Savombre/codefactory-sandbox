"""Utility function to convert text into URL-friendly slugs."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    - Converts to lowercase
    - Normalizes accented characters (é→e, ç→c, etc.)
    - Replaces spaces with hyphens
    - Removes special characters (keeps only alphanumerics and hyphens)
    - Collapses multiple consecutive hyphens into one
    - Strips leading/trailing hyphens
    """
    # Normalize unicode characters: decompose accented chars, then remove combining marks
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))

    # Lowercase
    text = text.lower()

    # Replace spaces with hyphens
    text = text.replace(" ", "-")

    # Remove anything that is not alphanumeric or a hyphen
    text = re.sub(r"[^a-z0-9-]", "", text)

    # Collapse multiple consecutive hyphens
    text = re.sub(r"-{2,}", "-", text)

    # Strip leading/trailing hyphens
    text = text.strip("-")

    return text

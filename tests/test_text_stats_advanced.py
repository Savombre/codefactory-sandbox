"""Tests for text_stats_advanced module."""

import pytest
from text_stats_advanced import top_words, avg_word_length


# --- top_words tests ---

class TestTopWords:
    def test_basic(self):
        text = "the cat sat on the mat the cat"
        result = top_words(text, 2)
        assert result == [("the", 3), ("cat", 2)]

    def test_default_n(self):
        text = "a b c d e f g"
        result = top_words(text)
        assert len(result) == 5

    def test_empty_text(self):
        assert top_words("") == []

    def test_single_word(self):
        assert top_words("hello") == [("hello", 1)]

    def test_single_word_repeated(self):
        assert top_words("go go go", 1) == [("go", 3)]

    def test_punctuation_stripped(self):
        text = "hello, world! hello."
        result = top_words(text, 2)
        assert result == [("hello", 2), ("world", 1)]

    def test_mixed_case_lowered(self):
        text = "Hello HELLO hello"
        result = top_words(text, 1)
        assert result == [("hello", 3)]

    def test_n_greater_than_distinct_words(self):
        text = "one two three"
        result = top_words(text, 10)
        assert len(result) == 3

    def test_whitespace_only(self):
        assert top_words("   \n\t  ") == []

    def test_numbers_counted_as_words(self):
        text = "42 42 hello"
        result = top_words(text, 2)
        assert result == [("42", 2), ("hello", 1)]


# --- avg_word_length tests ---

class TestAvgWordLength:
    def test_basic(self):
        # "the" (3) + "cat" (3) = 6 / 2 = 3.0
        assert avg_word_length("the cat") == 3.0

    def test_empty_text(self):
        assert avg_word_length("") == 0.0

    def test_single_word(self):
        assert avg_word_length("hello") == 5.0

    def test_punctuation_stripped(self):
        # "hello" (5) + "world" (5) = 10 / 2 = 5.0
        assert avg_word_length("hello, world!") == 5.0

    def test_mixed_case(self):
        # case doesn't affect length: "Hi" -> "hi" (2), "There" -> "there" (5)
        assert avg_word_length("Hi There") == 3.5

    def test_whitespace_only(self):
        assert avg_word_length("   \t\n") == 0.0

    def test_varied_lengths(self):
        # "a" (1) + "bb" (2) + "ccc" (3) = 6 / 3 = 2.0
        assert avg_word_length("a bb ccc") == 2.0

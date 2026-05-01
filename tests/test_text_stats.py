"""Tests for text_stats module."""

from text_stats import count_words, count_chars, count_lines


class TestCountWords:
    def test_simple_sentence(self):
        assert count_words("hello world") == 2

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_empty_string(self):
        assert count_words("") == 0

    def test_multiple_spaces(self):
        assert count_words("hello   world   foo") == 3

    def test_leading_trailing_spaces(self):
        assert count_words("  hello world  ") == 2

    def test_tabs_and_newlines(self):
        assert count_words("hello\tworld\nfoo") == 3

    def test_only_whitespace(self):
        assert count_words("   \t\n  ") == 0


class TestCountChars:
    def test_simple_text_with_spaces(self):
        assert count_chars("hello world") == 11

    def test_simple_text_without_spaces(self):
        assert count_chars("hello world", with_spaces=False) == 10

    def test_empty_string(self):
        assert count_chars("") == 0

    def test_empty_string_without_spaces(self):
        assert count_chars("", with_spaces=False) == 0

    def test_only_spaces(self):
        assert count_chars("   ") == 3

    def test_only_spaces_without_spaces(self):
        assert count_chars("   ", with_spaces=False) == 0

    def test_multiple_spaces_between_words(self):
        assert count_chars("a  b", with_spaces=False) == 2

    def test_newlines_and_tabs(self):
        assert count_chars("a\nb\tc") == 5


class TestCountLines:
    def test_single_line(self):
        assert count_lines("hello") == 1

    def test_multiple_lines(self):
        assert count_lines("hello\nworld") == 2

    def test_three_lines(self):
        assert count_lines("a\nb\nc") == 3

    def test_empty_string(self):
        assert count_lines("") == 0

    def test_trailing_newline(self):
        assert count_lines("hello\n") == 2

    def test_only_newlines(self):
        assert count_lines("\n\n") == 3

    def test_blank_lines_between_text(self):
        assert count_lines("hello\n\nworld") == 3

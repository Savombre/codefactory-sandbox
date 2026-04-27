"""Tests for the slugify utility function."""

import pytest

from slugify import slugify


class TestSlugify:
    def test_simple_text(self):
        assert slugify("Hello World") == "hello-world"

    def test_accented_characters(self):
        assert slugify("Café crème") == "cafe-creme"

    def test_special_characters(self):
        assert slugify("foo@bar!baz") == "foobarbaz"

    def test_multiple_spaces(self):
        assert slugify("foo  bar") == "foo-bar"

    def test_empty_string(self):
        assert slugify("") == ""

    def test_already_slugified(self):
        assert slugify("already-slugified") == "already-slugified"

    def test_leading_trailing_spaces(self):
        assert slugify("  hello world  ") == "hello-world"

    def test_mixed_accents(self):
        assert slugify("Ünïcödé têxt") == "unicode-text"

    def test_numbers(self):
        assert slugify("version 2.0 release") == "version-20-release"

    def test_only_special_characters(self):
        assert slugify("@#$%^&*") == ""

    def test_hyphens_and_spaces_mixed(self):
        assert slugify("foo - bar -- baz") == "foo-bar-baz"

    def test_cedilla(self):
        assert slugify("façade français") == "facade-francais"

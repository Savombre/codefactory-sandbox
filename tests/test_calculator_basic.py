import pytest
from calculator import add, subtract


class TestAdd:
    def test_positive_integers(self):
        assert add(2, 3) == 5

    def test_negative_integers(self):
        assert add(-1, -2) == -3

    def test_mixed_sign(self):
        assert add(-5, 3) == -2

    def test_floats(self):
        assert add(1.5, 2.3) == pytest.approx(3.8)

    def test_negative_floats(self):
        assert add(-1.1, -2.2) == pytest.approx(-3.3)

    def test_zero_plus_zero(self):
        assert add(0, 0) == 0

    def test_zero_plus_number(self):
        assert add(0, 42) == 42

    def test_number_plus_zero(self):
        assert add(42, 0) == 42

    def test_large_numbers(self):
        assert add(10**18, 10**18) == 2 * 10**18

    def test_float_and_int(self):
        assert add(1, 2.5) == pytest.approx(3.5)


class TestSubtract:
    def test_positive_integers(self):
        assert subtract(5, 3) == 2

    def test_negative_integers(self):
        assert subtract(-1, -2) == 1

    def test_mixed_sign(self):
        assert subtract(-5, 3) == -8

    def test_floats(self):
        assert subtract(5.5, 2.2) == pytest.approx(3.3)

    def test_negative_floats(self):
        assert subtract(-1.1, -2.2) == pytest.approx(1.1)

    def test_zero_minus_zero(self):
        assert subtract(0, 0) == 0

    def test_zero_minus_number(self):
        assert subtract(0, 42) == -42

    def test_number_minus_zero(self):
        assert subtract(42, 0) == 42

    def test_large_numbers(self):
        assert subtract(10**18, 10**18) == 0

    def test_result_negative(self):
        assert subtract(3, 5) == -2

    def test_float_and_int(self):
        assert subtract(5.5, 2) == pytest.approx(3.5)

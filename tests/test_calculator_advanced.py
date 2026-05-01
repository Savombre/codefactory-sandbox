import pytest
from calculator import multiply, divide


class TestMultiply:
    def test_positive_integers(self):
        assert multiply(3, 4) == 12

    def test_negative_integers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6

    def test_floats(self):
        assert multiply(2.5, 4.0) == 10.0

    def test_zero(self):
        assert multiply(0, 100) == 0
        assert multiply(100, 0) == 0

    def test_large_numbers(self):
        assert multiply(10**6, 10**6) == 10**12

    def test_mixed_sign(self):
        assert multiply(-3, 5) == -15


class TestDivide:
    def test_positive_integers(self):
        assert divide(10, 2) == 5.0

    def test_negative_integers(self):
        assert divide(-10, 2) == -5.0
        assert divide(-10, -2) == 5.0

    def test_floats(self):
        assert divide(7.5, 2.5) == 3.0

    def test_zero_numerator(self):
        assert divide(0, 5) == 0.0

    def test_large_numbers(self):
        assert divide(10**12, 10**6) == 10**6

    def test_division_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_division_by_zero_with_zero_numerator(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)

    def test_result_is_float(self):
        result = divide(7, 2)
        assert result == 3.5
        assert isinstance(result, float)

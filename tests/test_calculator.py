
import pytest

from app.calculator import add, subtract, multiply


# Addition tests
def test_add():
    assert add(10, 5) == 15


# Subtraction tests
def test_subtract():
    assert subtract(10, 5) == 5


# Multiplication tests
def test_multiply():
    assert multiply(10, 5) == 50


# Invalid input tests
def test_add_negative_number():
    with pytest.raises(ValueError):
        add(-10, 5)


def test_subtract_zero():
    with pytest.raises(ValueError):
        subtract(10, 0)


def test_multiply_string():
    with pytest.raises(ValueError):
        multiply("10", 5)


def test_add_float():
    with pytest.raises(ValueError):
        add(10.5, 5)

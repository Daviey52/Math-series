import pytest
from math_series.math_series import fibonacci, lucas, sum_series

from math_series import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_0ne():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_three():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_four():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_five():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_six():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_seven():
    actual = sum_series(5, 4)
    expected = 6
    assert actual == expected


def test_eight():
    actual = sum_series(1, 1)
    expected = 1
    assert actual == expected

import pytest
import unittest
from hypothesis import given
import hypothesis.strategies as st

from Calculator import Calculator


# Тестирование с использованием pytest
@pytest.fixture  # декоратор
def calculator():
    return Calculator()


def test_add(calculator):
    result = calculator.add(5, 3)
    assert result == 8


def test_subtract(calculator):
    result = calculator.subtract(10, 4)
    assert result == 6


# Тестирование с использованием nose
def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(2, 3)
    assert result == 6


# Тестирование с использованием doctest
class TestCalculator(unittest.TestCase):
    """
    Простой калькулятор для сложения, вычитания, умножения и деления.

    >>> calculator = Calculator()
    >>> calculator.add(5, 3)
    8
    >>> calculator.subtract(10, 4)
    6
    """

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(8, 4)
        self.assertEqual(result, 2)


# Тестирование с использованием Hypothesis
@given(st.integers(), st.integers())  # генерирует случайные числа
def test_hypothesis_add(x, y):
    calculator = Calculator()
    result = calculator.add(x, y)
    assert result == x + y

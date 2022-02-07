import pytest
from fraction import Fraction

def test_zero_test():
    assert Fraction(0).add(Fraction(0)) == Fraction(0)
    assert Fraction(0, 1).add(Fraction(0, 1)) == Fraction(0)
    assert Fraction(0, 1).add(Fraction(0, -1)) == Fraction(0)

def test_adding_test():
    assert Fraction(1, 2).__add__(Fraction(1, 4)) == Fraction(6, 8)
    assert Fraction(1, 5).__add__(Fraction(2, 5)) == Fraction(15, 25)


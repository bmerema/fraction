import pytest
from fraction import Fraction

def test_zero_plus_zero():
    assert Fraction(0).plus(Fraction(0)) == Fraction(0)
    assert Fraction(0, 1).plus(Fraction(0, 1)) == Fraction(0)
    assert Fraction(0, 1).plus(Fraction(0, -1)) == Fraction(0)
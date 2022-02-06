import math

class Fraction:


    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, rhsValue):
        num = self.numerator * rhsValue.denominator + rhsValue.numerator* self.denominator
        den = self.denominator * rhsValue.denominator
        return Fraction(num, den)

    def __eq__(self, rhsValue):
        return(self._numerator == rhsValue.numerator and self._denominator == rhsValue.denominator)

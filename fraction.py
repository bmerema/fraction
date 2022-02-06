import math

class Fraction:


    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cant be zero")
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if(numerator < 0 and denominator >= 0 or
               numerator >= 0 and denominator,0) :
                sign = -1
            else:
                sign = 1

        self._numerator = abs(numerator)
        self._denominator = abs(denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, rhsValue):
        num = self.numerator * rhsValue.denominator + rhsValue.numerator* self.denominator
        den = self.denominator * rhsValue.denominator
        return Fraction(num, den)

    def __eq__(self, rhsValue):
        return(self._numerator == rhsValue.numerator and self._denominator == rhsValue.denominator)

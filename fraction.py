import math

class Fraction:


    def __init__(self, numerator=0, denominator=1):
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

    def __repr__(self):
        return str(self._numerator) + "/" + str(self._denominator)

    def __add__(self, rhsValue):
        num = self._numerator * rhsValue._denominator + rhsValue._numerator* self._denominator
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)

    def __eq__(self, rhsValue):
        return(self._numerator == rhsValue._numerator
               and self._denominator == rhsValue._denominator)

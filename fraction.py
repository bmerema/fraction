import math

class Fraction:


    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def adding(self, fraction:"Fraction"):
        nominator = self.numerator * fraction.denominator + fraction.numerator* self.denominator
        denominator = self.denominator * fraction.denominator
        return Fraction(nominator, denominator)

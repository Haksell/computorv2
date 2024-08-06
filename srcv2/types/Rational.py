import math


class Rational:
    def __init__(self, numer, denom):
        assert denom != 0  # TODO
        g = math.gcd(numer, denom)
        self.__numer = numer // g
        self.__denom = denom // g

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    @property
    def numer(self):
        return self.__numer

    @property
    def denom(self):
        return self.__denom

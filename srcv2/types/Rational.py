import math


class Rational:
    def __init__(self, numer, denom):
        assert denom != 0  # TODO
        if denom < 0:
            numer = -numer
            denom = -denom
        g = math.gcd(numer, denom)
        self.__numer = numer // g
        self.__denom = denom // g

    @property
    def numer(self):
        return self.__numer

    @property
    def denom(self):
        return self.__denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numer}, {self.__denom})"

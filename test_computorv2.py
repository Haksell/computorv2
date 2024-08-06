from srcv2 import tokenize
from srcv2.types import Rational


"""
subject examples:

varA = 2
varB = 4.242
varC = -4.3

varA = 2*i + 3
varB = -4i - 4

varA = [[2,3];[4,3]]

funA(x) = 2*x^5 + 4x^2 - 5*x + 4
funB(y) = 43 * y / (4 % 2 * y)
funC(z) = -2 * z - 5

x = 2
y = x
y = 7
y = 2 * i - 4

varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)
varB = 2 * varA - 5 %4
funA(x) = varA + varB * 4 - 1 / 2 + x
varC = 2 * varA - varB
varD = funA(varC)

a = 2 * 4 + 4
a + 2 = ?

funA(x) = 2 * 4 + x
funB(x) = 4 -5 + (x + 2)^2 - 4
funC(x) = 4x + 5 - 2
funA(2) + funB(4) = ?
funC(3) = ?

funA(x) = x^2 + 2x + 1
y = 0
funA(x) = y ?

varA = 2
varB= 2 * (4 + varA + 3)
varC =2 * varB
varD = 2 *(2 + 4 *varC -4 /3)

matA = [[1,2];[3,2];[3,4]]
matB= [[1,2]]

funA(b) = 2*b+b
funB(a) =2 * a
funC(y) =2* y + 4 -2 * 4+1/3
funD(x) = 2 *x

funA(x) = 2*x+1
funB(x) = 2 * x+1
funA(funB(x)) = ?
"""


def test_rational():
    assert Rational(0, 1) == Rational(0, 1)
    assert Rational(21, 14) == Rational(3, 2)
    assert Rational(21, 14).numer == 3
    assert Rational(21, 14).denom == 2


def test_tokenize():
    assert tokenize("varA = 2") == ["varA", "=", Rational(2, 1)]

import math
from computorv1 import print_reduced_form
from decimal import Decimal
from fractions import Fraction
from math import sqrt
import pytest
from src.parse_equation import parse_equation
from src.print_solutions import print_solutions
from src.solve import solve_third_degree
from src.utils import exact_isqrt, is_integer, sqrt_fraction


def __is_complex_close(a, b):
    assert isinstance(a, float) or isinstance(a, complex)
    return abs(a - b) < 1e-4


def test_exact_isqrt():
    assert exact_isqrt(-4) is None
    assert exact_isqrt(-3) is None
    assert exact_isqrt(-2) is None
    assert exact_isqrt(-1) is None
    assert exact_isqrt(0) == 0
    assert exact_isqrt(1) == 1
    assert exact_isqrt(2) is None
    assert exact_isqrt(3) is None
    assert exact_isqrt(4) == 2
    assert exact_isqrt(5) is None
    assert exact_isqrt(6) is None
    assert exact_isqrt(7) is None
    assert exact_isqrt(8) is None
    assert exact_isqrt(9) == 3
    assert exact_isqrt(10) is None
    assert exact_isqrt(11) is None
    assert exact_isqrt(12) is None
    assert exact_isqrt(13) is None
    assert exact_isqrt(14) is None
    assert exact_isqrt(15) is None
    assert exact_isqrt(16) == 4
    assert exact_isqrt(17) is None
    assert exact_isqrt(18) is None
    assert exact_isqrt(19) is None
    assert exact_isqrt(20) is None


def test_is_integer():
    assert is_integer(42)
    assert is_integer(0)
    assert not is_integer(42.5)
    assert is_integer(42.0)
    assert is_integer(0.0)
    assert not is_integer(3 + 4j)
    assert not is_integer(complex(math.pi, 0))
    assert is_integer(3.0 + 0j)
    assert is_integer(complex(0, 0))
    assert not is_integer(Fraction(3, 2))
    assert is_integer(Fraction(42, 21))
    assert is_integer(Fraction(0, 42))
    assert not is_integer(Decimal("42.1"))
    assert is_integer(Decimal("42.0000"))
    assert is_integer(Decimal("0"))
    with pytest.raises(SystemExit):
        is_integer("42")


def test_sqrt_fraction():
    assert sqrt_fraction(Fraction(8, 2)) == Fraction(2, 1)
    assert sqrt_fraction(Fraction(9, 4)) == Fraction(3, 2)
    assert sqrt_fraction(Fraction(0, 42)) == Fraction(0, 1)
    assert __is_complex_close(sqrt_fraction(Fraction(7, 2)), sqrt(3.5))
    assert __is_complex_close(sqrt_fraction(Fraction(-4, 1)), 2j)
    assert __is_complex_close(
        sqrt_fraction(Fraction(-42, 10)), 1.2548895456552942e-16 + 2.04939015319192j
    )


def test_parse_equation_good():
    def check_equation(s, expected):
        assert parse_equation(s) == list(map(Decimal, expected))

    check_equation("0=0", [])
    check_equation("3X=2X+1*X^1", [])
    check_equation("1=0", [1])
    check_equation("0=42", [-42])
    check_equation("X=0", [0, 1])
    check_equation("X^2=0", [0, 0, 1])
    check_equation("1*X^2=0", [0, 0, 1])
    check_equation("1X^2=0", [0, 0, 1])
    check_equation("5 * X^0 + 4 * X^1 = 4 * X^0", [1, 4])
    check_equation("5 + 4 * X + X^2= X^2", [5, 4])
    check_equation("X^3+18X^2+X+1=0", [1, 1, 18, 1])
    check_equation("-7X^5 = X^2", [0, 0, -1, 0, 0, -7])
    check_equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0", [4, 4, "-9.3"])
    check_equation(
        "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0", [5, -6, 0, "-5.6"]
    )


def test_parse_equation_bad():
    for s in ["42", "2x=0", "3*X^2", "3*X^2=", "=", "X^-1 = 42", "(2+2)*X^2=0"]:
        with pytest.raises(SystemExit):
            parse_equation(s)


def test_print_reduced_form(capfd):
    def check_reduced_form(reduced, expected):
        print_reduced_form(reduced)
        out, _ = capfd.readouterr()
        assert out == f"Reduced form: {expected} = 0\n"

    check_reduced_form([], "0")
    check_reduced_form([42], "42")
    check_reduced_form([Decimal("-17.3")], "-17.3")
    check_reduced_form(
        [Decimal("-17.3"), Decimal("4.2"), 0, -4],
        "-17.3 * X^0 + 4.2 * X^1 + 0 * X^2 - 4 * X^3",
    )


def test_print_solutions(capfd):
    def check_solutions(reduced, expected):
        print_solutions(reduced)
        out, _ = capfd.readouterr()
        assert out == expected

    check_solutions([], "There are infinitely many solutions.\n")
    check_solutions([42], "There are no solutions.\n")
    check_solutions([Decimal("-13.37")], "There are no solutions.\n")
    check_solutions([0, 2], "The solution is 0\n")
    check_solutions([6, 3], "The solution is -2\n")
    check_solutions([2, -3], "The solution is 2/3 (0.666667)\n")
    check_solutions([Decimal("-4.2"), 3], "The solution is 7/5 (1.4)\n")
    check_solutions(
        [0, 0, -1],
        "Discriminant is zero, the solution of multiplicity 2 is 0\n",
    )
    check_solutions(
        [Decimal("-9.68"), 0, 2],
        "Discriminant is positive, the two solutions are:\n-11/5 (-2.2)\n11/5 (2.2)\n",
    )
    check_solutions(
        [3, -6, 2],
        "Discriminant is positive, the two solutions are:\n0.633975\n2.366025\n",
    )
    check_solutions(
        [4, -6, 2],
        "Discriminant is positive, the two solutions are:\n1\n2\n",
    )
    check_solutions(
        [4.5, -6, 2],
        "Discriminant is zero, the solution of multiplicity 2 is 3/2 (1.5)\n",
    )
    check_solutions(
        [1, 0, 1],
        "Discriminant is negative, the two solutions are:\n-1i\n1i\n",
    )
    check_solutions(
        [8, 0, 2],
        "Discriminant is negative, the two solutions are:\n-2i\n2i\n",
    )
    check_solutions(
        [4, 3, 3],
        "Discriminant is negative, the two solutions are:\n-0.5-1.040833i\n-0.5+1.040833i\n",
    )
    check_solutions(
        [1, 2, 3, 4, 5],
        "The polynomial degree is greater than 3, I can't solve.\n",
    )


def test_third_degree():
    with pytest.raises(AssertionError):
        solve_third_degree([3, 2, 1, 0])
    for reduced in (
        [0, 1, 2, 3],
        [1, 2, 3, 4],
        [math.pi, math.pi, math.pi, math.pi],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 2],
        [0, 0, 0, 3],
        [0, 0, 0, -1],
        [0, 0, 0, -2],
        [0.1, 0.2, 0.3, 0.4],
        [-0.6, -1.1, 42, 0.7],
    ):
        d, c, b, a = reduced
        _, solutions = solve_third_degree(reduced)
        for x in solutions:
            assert __is_complex_close(a * x**3 + b * x**2 + c * x + d, 0)

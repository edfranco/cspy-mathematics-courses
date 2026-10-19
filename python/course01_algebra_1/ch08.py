"""Chapter 8: Polynomials and Factoring. Programming exercises C8.1 to C8.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C8.1
# Using coefficient lists, write `poly_add(p, q)`, `poly_sub(p, q)` and `poly_mul(p,
# q)`. Strip trailing zeros so the degree is honest. Test with Exercises 8.1 through
# 8.6.


def poly_add(p, q):
    raise NotImplementedError("C8.1")


def poly_sub(p, q):
    raise NotImplementedError("C8.1")


def poly_mul(p, q):
    raise NotImplementedError("C8.1")


def test_c8_1():
    pytest.skip("C8.1: write asserts from the hand exercises")


# C8.2
# Write `horner(coeffs, x)` and `naive_eval(coeffs, x)` (the version that calls `x **
# k` for each term). Count the multiplications each makes for a degree-50 polynomial,
# treating `x ** k` as k - 1 multiplications.


def horner(coeffs, x):
    raise NotImplementedError("C8.2")


def naive_eval(coeffs, x):
    raise NotImplementedError("C8.2")


def test_c8_2():
    pytest.skip("C8.2: write asserts from the hand exercises")


# C8.3
# Write `factor_trinomial(a, b, c)` for integer coefficients. Search every pair of
# integer factors of ac for a pair that sums to b, then factor by grouping, and return
# the two binomials as coefficient lists or `None` if there is no integer
# factorization. Test with Exercises 8.8 through 8.10.


def factor_trinomial(a, b, c):
    raise NotImplementedError("C8.3")


def test_c8_3():
    pytest.skip("C8.3: write asserts from the hand exercises")


# C8.4
# Write `poly_to_string(coeffs)` that prints standard form, so `[-24, -2, 1]` prints
# as `x^2 - 2x - 24`. Reuse or improve your C2.4.


def poly_to_string(coeffs):
    raise NotImplementedError("C8.4")


def test_c8_4():
    pytest.skip("C8.4: write asserts from the hand exercises")


# C8.5
# For every factoring exercise in this chapter, multiply your factors back together
# with `poly_mul` and assert the result equals the original. A factorization that does
# not survive this test is wrong, whatever the answer key says.


def test_c8_5():
    pytest.skip("C8.5: write asserts from the hand exercises")

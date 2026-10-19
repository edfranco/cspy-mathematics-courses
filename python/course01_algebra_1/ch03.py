"""Chapter 3: Linear Equations in One Variable. Programming exercises C3.1 to C3.4.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C3.1
# Write `solve_linear(a, b, c, d)` that solves ax + b = cx + d and returns one of:
# `("one", x)`, `("none",)` or `("all",)`. Test it against Exercises 3.1 through 3.6.


def solve_linear(a, b, c, d):
    raise NotImplementedError("C3.1")


def test_c3_1():
    pytest.skip("C3.1: write asserts from the hand exercises")


# C3.2
# Write `check_linear(a, b, c, d, x)` that substitutes x into both sides and compares
# them with `math.isclose`. Use it to verify every `("one", x)` result from C3.1, so
# your solver and your checker test each other.


def check_linear(a, b, c, d, x):
    raise NotImplementedError("C3.2")


def test_c3_2():
    pytest.skip("C3.2: write asserts from the hand exercises")


# C3.3
# Write `c_to_f(c)` and `f_to_c(f)` from Exercise 3.7. Assert that `f_to_c(c_to_f(c))`
# returns `c` (within tolerance) for every integer c from -50 to 150.


def c_to_f(c):
    raise NotImplementedError("C3.3")


def f_to_c(f):
    raise NotImplementedError("C3.3")


def test_c3_3():
    pytest.skip("C3.3: write asserts from the hand exercises")


# C3.4
# Rewrite C3.1 to use `fractions.Fraction` for all arithmetic so that Exercise 3.9
# returns exactly 7/3 rather than 2.3333. Decide what the function should do if the
# inputs are floats.


def test_c3_4():
    pytest.skip("C3.4: write asserts from the hand exercises")

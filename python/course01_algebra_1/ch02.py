"""Chapter 2: Expressions and Simplification. Programming exercises C2.1 to C2.4.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C2.1
# Represent a polynomial in one variable as a dictionary from power to coefficient, so
# 3x^2 + 2x - 8 is `{2: 3, 1: 2, 0: -8}`. Write `combine(terms)` that takes a list of
# `(coefficient, power)` pairs and returns the combined dictionary with zero
# coefficients removed. Test it with Exercise 2.3.


def combine(terms):
    raise NotImplementedError("C2.1")


def test_c2_1():
    pytest.skip("C2.1: write asserts from the hand exercises")


# C2.2
# Write `evaluate(poly, x)` for that dictionary form. Assert it agrees with your hand
# answer to Exercise 2.4.


def evaluate(poly, x):
    raise NotImplementedError("C2.2")


def test_c2_2():
    pytest.skip("C2.2: write asserts from the hand exercises")


# C2.3
# Build an expression tree with classes `Num`, `Var`, `Add`, `Sub` and `Mul`, each
# with an `eval(env)` method where `env` maps variable names to values. Encode both
# trees from Exercise 2.9 and confirm the two values you computed by hand.


def eval(env):
    raise NotImplementedError("C2.3")


def test_c2_3():
    pytest.skip("C2.3: write asserts from the hand exercises")


# C2.4
# Write `to_string(poly)` that prints the dictionary form in standard order with
# correct signs, so `{2: 2, 1: 7, 0: -8}` prints as `2x^2 + 7x - 8` and `{1: 1, 0:
# -1}` prints as `x - 1`. Test every edge case you can think of: coefficient 1,
# coefficient -1, missing powers, a constant alone.


def to_string(poly):
    raise NotImplementedError("C2.4")


def test_c2_4():
    pytest.skip("C2.4: write asserts from the hand exercises")

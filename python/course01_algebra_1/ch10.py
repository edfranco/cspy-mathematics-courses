"""Chapter 10: Functions. Programming exercises C10.1 to C10.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C10.1
# Write `compose(f, g)` that returns a new function computing f(g(x)). Test Exercises
# 10.4 and 10.5 with lambdas, and show that `compose(f, g)` and `compose(g, f)`
# differ.


def compose(f, g):
    raise NotImplementedError("C10.1")


def test_c10_1():
    pytest.skip("C10.1: write asserts from the hand exercises")


# C10.2
# Write `with_domain(f, allowed)` that returns a function raising `ValueError` when
# `allowed(x)` is false and otherwise returns f(x). Wrap the two functions from
# Exercise 10.3 and test an input inside and outside each domain.


def with_domain(f, allowed):
    raise NotImplementedError("C10.2")


def allowed(x):
    raise NotImplementedError("C10.2")


def test_c10_2():
    pytest.skip("C10.2: write asserts from the hand exercises")


# C10.3
# Represent a piecewise function as a list of `(condition, rule)` pairs and write
# `piecewise(rules)` that returns a function applying the first matching rule. Encode
# Exercise 10.7 and confirm your three values. Add a check that raises if no rule
# matches.


def piecewise(rules):
    raise NotImplementedError("C10.3")


def test_c10_3():
    pytest.skip("C10.3: write asserts from the hand exercises")


# C10.4
# Write `is_inverse(f, f_inv, samples)` that returns true when f(f_inv(x)) and
# f_inv(f(x)) both equal x within tolerance for every sample. Test Exercise 10.6, and
# show that it fails for f(x) = x^2 with f_inv(x) = sqrt(x) when the samples include
# negatives.


def is_inverse(f, f_inv, samples):
    raise NotImplementedError("C10.4")


def test_c10_4():
    pytest.skip("C10.4: write asserts from the hand exercises")


# C10.5
# Write `memoize(f)` that caches results in a dictionary. Explain in a comment why
# this is only correct because f is a function in the mathematical sense, and give an
# example of a Python callable it would break.


def memoize(f):
    raise NotImplementedError("C10.5")


def test_c10_5():
    pytest.skip("C10.5: write asserts from the hand exercises")

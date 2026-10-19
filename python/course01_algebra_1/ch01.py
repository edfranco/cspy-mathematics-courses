"""Chapter 1: Numbers and Operations. Programming exercises C1.1 to C1.4.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C1.1
# Show in Python that `0.1 + 0.2 == 0.3` is false. Then make the comparison true two
# ways: with `math.isclose`, and with `fractions.Fraction`. Write one sentence on why
# the float version fails.


def test_c1_1():
    pytest.skip("C1.1: write asserts from the hand exercises")


# C1.2
# Write `floor_divmod(a, b)` that returns the quotient and remainder with 0 <= r < |b|
# for any integers a and nonzero b, without using `//`, `%` or `divmod`. Test it
# against `divmod` for every a from -10 to 10 and b in {3, -3}. Note which cases would
# differ in JavaScript.


def floor_divmod(a, b):
    raise NotImplementedError("C1.2")


def test_c1_2():
    pytest.skip("C1.2: write asserts from the hand exercises")


# C1.3
# Write `abs_value(x)` without calling `abs`, and `distance(a, b)` for two numbers on
# a number line. Assert that `distance(-12, 9)` matches your answer to Exercise 1.10.


def abs_value(x):
    raise NotImplementedError("C1.3")


def distance(a, b):
    raise NotImplementedError("C1.3")


def test_c1_3():
    pytest.skip("C1.3: write asserts from the hand exercises")


# C1.4
# Write `gcd(a, b)` using the Euclidean algorithm, then `to_fraction(s)` that turns a
# terminating decimal string such as `"0.375"` into a reduced fraction as a tuple of
# integers. Check it against `fractions.Fraction` for the values in Exercise 1.5.


def gcd(a, b):
    raise NotImplementedError("C1.4")


def to_fraction(s):
    raise NotImplementedError("C1.4")


def test_c1_4():
    pytest.skip("C1.4: write asserts from the hand exercises")

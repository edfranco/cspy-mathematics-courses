"""Chapter 6: Inequalities. Programming exercises C6.1 to C6.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C6.1
# Write `clamp(x, lo, hi)`. For 10,000 random floats, assert that lo <= clamp(x, lo,
# hi) <= hi and that clamp returns x unchanged whenever x was already in range.


def clamp(x, lo, hi):
    raise NotImplementedError("C6.1")


def test_c6_1():
    pytest.skip("C6.1: write asserts from the hand exercises")


# C6.2
# Write `solve_inequality(a, b, op, c)` for ax + b op c, where `op` is one of `"<"`,
# `"<="`, `">"`, `">="`. Return the solution as an interval tuple `(lo, hi, lo_closed,
# hi_closed)` using `float("-inf")` and `float("inf")` for open ends. It must flip the
# operator when a is negative. Test with Exercises 6.1 through 6.3.


def solve_inequality(a, b, op, c):
    raise NotImplementedError("C6.2")


def test_c6_2():
    pytest.skip("C6.2: write asserts from the hand exercises")


# C6.3
# Write `contains(interval, x)` for that interval tuple. Test the two intervals from
# Exercise 6.9 at their endpoints and just inside and outside each.


def contains(interval, x):
    raise NotImplementedError("C6.3")


def test_c6_3():
    pytest.skip("C6.3: write asserts from the hand exercises")


# C6.4
# Write `solve_abs_inequality(a, b, op, c)` for |ax + b| op c, returning one interval,
# a list of two intervals, or an empty list. Test with Exercises 6.6 through 6.8.


def solve_abs_inequality(a, b, op, c):
    raise NotImplementedError("C6.4")


def test_c6_4():
    pytest.skip("C6.4: write asserts from the hand exercises")


# C6.5
# Write `can_ride(h)` using the absolute value form from Exercise 6.10, and a second
# function `can_ride_compound(h)` that uses the compound form. Assert they agree for
# every integer height from 30 to 60.


def can_ride(h):
    raise NotImplementedError("C6.5")


def can_ride_compound(h):
    raise NotImplementedError("C6.5")


def test_c6_5():
    pytest.skip("C6.5: write asserts from the hand exercises")

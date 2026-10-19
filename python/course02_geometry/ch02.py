"""Chapter 2: Lines and Angles. Programming exercises C2.1 to C2.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C2.1
# Write `normalize_angle(deg)` that returns the equivalent angle in [0, 360) using
# only addition and subtraction in a loop, then a second version using `%`. Assert
# they agree for every integer from -1000 to 1000, and check Exercise 2.10.


def normalize_angle(deg):
    raise NotImplementedError("C2.1")


def test_c2_1():
    pytest.skip("C2.1: write asserts from the hand exercises")


# C2.2
# Write `transversal_angles(a1)` that takes the measure of angle 1 in Figure
# (transversal figure in the book) and returns a dictionary of all eight angles,
# assuming the lines are parallel. Check it against Example 2.2 by passing 65.


def transversal_angles(a1):
    raise NotImplementedError("C2.2")


def test_c2_2():
    pytest.skip("C2.2: write asserts from the hand exercises")


# C2.3
# Write `third_angle(a, b)` that returns the third angle of a triangle and raises
# `ValueError` when a + b >= 180 or either input is not positive. Test with Exercise
# 2.6.


def third_angle(a, b):
    raise NotImplementedError("C2.3")


def test_c2_3():
    pytest.skip("C2.3: write asserts from the hand exercises")


# C2.4
# Write `classify_pair(a, b)` returning `"complementary"`, `"supplementary"` or
# `"neither"`, using `math.isclose` so that 0.1 + 89.9 counts as complementary.


def classify_pair(a, b):
    raise NotImplementedError("C2.4")


def test_c2_4():
    pytest.skip("C2.4: write asserts from the hand exercises")


# C2.5
# Draw two parallel lines and a transversal with matplotlib, SVG or a canvas, and
# label the eight angles with the values from C2.2. Change the transversal's slope and
# confirm the labels still satisfy every relationship in the Core Ideas.


def test_c2_5():
    pytest.skip("C2.5: write asserts from the hand exercises")

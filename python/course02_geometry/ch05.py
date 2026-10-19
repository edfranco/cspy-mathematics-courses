"""Chapter 5: Transformations. Programming exercises C5.1 to C5.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C5.1
# Write `translate(p, dx, dy)`, `reflect_x(p)`, `reflect_y(p)` and `reflect_diag(p)`,
# then `rotate90(p, times)` and finally `dilate(p, k)`, all on coordinate tuples. Test
# with Exercises 5.1 to 5.4.


def translate(p, dx, dy):
    raise NotImplementedError("C5.1")


def reflect_x(p):
    raise NotImplementedError("C5.1")


def reflect_y(p):
    raise NotImplementedError("C5.1")


def reflect_diag(p):
    raise NotImplementedError("C5.1")


def rotate90(p, times):
    raise NotImplementedError("C5.1")


def dilate(p, k):
    raise NotImplementedError("C5.1")


def test_c5_1():
    pytest.skip("C5.1: write asserts from the hand exercises")


# C5.2
# Write `compose(*fns)` that returns a function applying the given functions right to
# left. Reproduce Exercise 5.7 and show the two compositions disagree.


def compose(*fns):
    raise NotImplementedError("C5.2")


def test_c5_2():
    pytest.skip("C5.2: write asserts from the hand exercises")


# C5.3
# Write `rotate90_about(p, center, times)` by composing translate, rotate and
# translate back. Test with Exercise 5.6.


def rotate90_about(p, center, times):
    raise NotImplementedError("C5.3")


def test_c5_3():
    pytest.skip("C5.3: write asserts from the hand exercises")


# C5.4
# Represent each transformation as a 3 * 3 matrix on homogeneous coordinates (x, y,
# 1), stored as nested lists. Write `apply(m, p)` and `multiply(a, b)`, and verify
# that multiplying matrices gives the same result as composing the functions from C5.2
# on 100 random points.


def apply(m, p):
    raise NotImplementedError("C5.4")


def multiply(a, b):
    raise NotImplementedError("C5.4")


def test_c5_4():
    pytest.skip("C5.4: write asserts from the hand exercises")


# C5.5
# Draw a polygon and its images under a sequence of transforms (matplotlib, SVG or
# canvas), with the original in a different color, and confirm visually that rotating
# by 90 deg four times returns the original exactly.


def test_c5_5():
    pytest.skip("C5.5: write asserts from the hand exercises")

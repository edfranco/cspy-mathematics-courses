"""Chapter 4: Coordinate Geometry. Programming exercises C4.1 to C4.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C4.1
# Write `distance(p, q)` and `midpoint(p, q)` on coordinate tuples. Compare `distance`
# with `math.dist` and check Exercises 4.1 to 4.3.


def distance(p, q):
    raise NotImplementedError("C4.1")


def midpoint(p, q):
    raise NotImplementedError("C4.1")


def test_c4_1():
    pytest.skip("C4.1: write asserts from the hand exercises")


# C4.2
# Write `circle_from_general(a, b, c)` that converts x^2 + y^2 + ax + by + c = 0 into
# `(center, radius)` by completing the square in code, raising if the radius would be
# imaginary. Test with Exercise 4.6.


def circle_from_general(a, b, c):
    raise NotImplementedError("C4.2")


def test_c4_2():
    pytest.skip("C4.2: write asserts from the hand exercises")


# C4.3
# Write `point_in_circle(p, center, r)` and `point_in_rect(p, x0, y0, x1, y1)` without
# square roots, each returning `"inside"`, `"on"` or `"outside"`. Test with Exercises
# 4.7 and 4.11.


def point_in_circle(p, center, r):
    raise NotImplementedError("C4.3")


def point_in_rect(p, x0, y0, x1, y1):
    raise NotImplementedError("C4.3")


def test_c4_3():
    pytest.skip("C4.3: write asserts from the hand exercises")


# C4.4
# Write `to_screen(p, w, h)` and `to_math(s, w, h)`. Assert they round-trip for 1000
# random points and reproduce Exercise 4.9.


def to_screen(p, w, h):
    raise NotImplementedError("C4.4")


def to_math(s, w, h):
    raise NotImplementedError("C4.4")


def test_c4_4():
    pytest.skip("C4.4: write asserts from the hand exercises")


# C4.5
# Write `is_parallelogram(a, b, c, d)` using the midpoints of the diagonals, then
# `is_rectangle(a, b, c, d)` that also checks adjacent sides are perpendicular by
# slope product. Test with Exercise 4.8 and with the rectangle in Exercise 4.10 for a
# = 4, b = 3.


def is_parallelogram(a, b, c, d):
    raise NotImplementedError("C4.5")


def is_rectangle(a, b, c, d):
    raise NotImplementedError("C4.5")


def test_c4_5():
    pytest.skip("C4.5: write asserts from the hand exercises")

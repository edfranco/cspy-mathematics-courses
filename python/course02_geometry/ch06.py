"""Chapter 6: Polygons and Area. Programming exercises C6.1 to C6.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C6.1
# Write `signed_area(points)` implementing the shoelace formula. Then write the
# function `is_counterclockwise(points)`, which reads the sign of that result. Test
# with Exercises 6.7, 6.9 and 6.10, and with each polygon's vertices reversed.


def signed_area(points):
    raise NotImplementedError("C6.1")


def is_counterclockwise(points):
    raise NotImplementedError("C6.1")


def test_c6_1():
    pytest.skip("C6.1: write asserts from the hand exercises")


# C6.2
# Write `regular_polygon(n, side)` that returns the n vertices on a circle (use
# `math.cos` and `math.sin` with the angle 2pi i / n; Chapter 9 explains the radians).
# Compute its area with C6.1 and compare with 1/2aP for n = 6, side 6.


def regular_polygon(n, side):
    raise NotImplementedError("C6.2")


def test_c6_2():
    pytest.skip("C6.2: write asserts from the hand exercises")


# C6.3
# Write `bounding_box(points)` and `boxes_overlap(a, b)`. Generate random triangles
# and confirm that whenever the boxes do not overlap, no vertex of one triangle lies
# inside the other.


def bounding_box(points):
    raise NotImplementedError("C6.3")


def boxes_overlap(a, b):
    raise NotImplementedError("C6.3")


def test_c6_3():
    pytest.skip("C6.3: write asserts from the hand exercises")


# C6.4
# Write `interior_angle_sum(n)` and `sides_from_interior_angle(deg)`, raising when the
# angle does not correspond to a whole number of sides. Test with Exercises 6.1 and
# 6.2.


def interior_angle_sum(n):
    raise NotImplementedError("C6.4")


def sides_from_interior_angle(deg):
    raise NotImplementedError("C6.4")


def test_c6_4():
    pytest.skip("C6.4: write asserts from the hand exercises")


# C6.5
# Scale a polygon by k using `dilate` from Chapter 5 for k = 1, 2, 3, 4, 5, compute
# each area with C6.1, and print the ratio to the original to confirm it is k^2.


def test_c6_5():
    pytest.skip("C6.5: write asserts from the hand exercises")

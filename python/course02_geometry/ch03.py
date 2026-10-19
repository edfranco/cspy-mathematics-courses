"""Chapter 3: Triangles. Programming exercises C3.1 to C3.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C3.1
# Write `is_triangle(a, b, c)` using the triangle inequality, and `triangle_type(a, b,
# c)` returning a pair such as `("isosceles", "obtuse")`, where the angle type comes
# from comparing c^2 with a^2 + b^2 for the longest side c. Test with Exercises 3.1,
# 3.2 and 3.6.


def is_triangle(a, b, c):
    raise NotImplementedError("C3.1")


def triangle_type(a, b, c):
    raise NotImplementedError("C3.1")


def test_c3_1():
    pytest.skip("C3.1: write asserts from the hand exercises")


# C3.2
# Write `hypotenuse(a, b)` and `leg(c, a)`, raising `ValueError` when a leg would not
# be shorter than the hypotenuse. Compare `hypotenuse` with `math.hypot` on 1000
# random inputs.


def hypotenuse(a, b):
    raise NotImplementedError("C3.2")


def leg(c, a):
    raise NotImplementedError("C3.2")


def test_c3_2():
    pytest.skip("C3.2: write asserts from the hand exercises")


# C3.3
# Write `pythagorean_triples(limit)` that returns every (a, b, c) with a < b < c <=
# `limit` and a^2 + b^2 = c^2, by brute force. List the triples with c <= 50 and check
# that (9, 40, 41) appears.


def pythagorean_triples(limit):
    raise NotImplementedError("C3.3")


def test_c3_3():
    pytest.skip("C3.3: write asserts from the hand exercises")


# C3.4
# Write `similarity_scale(t1, t2)` that takes two side-length triples and returns the
# scale factor if the triangles are similar (sort each, then check the three ratios
# are equal within tolerance) or `None`. Test with Example 3.3.


def similarity_scale(t1, t2):
    raise NotImplementedError("C3.4")


def test_c3_4():
    pytest.skip("C3.4: write asserts from the hand exercises")


# C3.5
# Two circles with centers (x_1, y_1), (x_2, y_2) and radii r_1, r_2 overlap when the
# distance between centers is at most r_1 + r_2. Write `circles_overlap(...)` that
# decides this without calling `sqrt`, by comparing squared quantities, and explain in
# a comment why that is both valid and faster.


def circles_overlap(*args):
    raise NotImplementedError("C3.5")


def test_c3_5():
    pytest.skip("C3.5: write asserts from the hand exercises")

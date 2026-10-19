"""Chapter 10: Vectors in Two Dimensions. Programming exercises C10.1 to C10.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C10.1
# Write `add`, `sub`, `scale`, `magnitude`, `normalize` (raising on the zero vector)
# and `dot` on coordinate tuples. Test with Exercises 10.1 to 10.4.


def test_c10_1():
    pytest.skip("C10.1: write asserts from the hand exercises")


# C10.2
# Write `angle_between(a, b)` in degrees using `math.acos`, clamping the cosine to
# [-1, 1] first. Test with Exercises 10.5 and 10.6, then explain in a comment why the
# clamp is needed when `a` and `b` are parallel.


def angle_between(a, b):
    raise NotImplementedError("C10.2")


def test_c10_2():
    pytest.skip("C10.2: write asserts from the hand exercises")


# C10.3
# Write `project(a, b)` and `perp(v)`. Test with Exercises 10.7 and 10.8, and assert
# that `dot(perp(v), v)` is zero for 100 random vectors.


def project(a, b):
    raise NotImplementedError("C10.3")


def perp(v):
    raise NotImplementedError("C10.3")


def dot(*args):
    raise NotImplementedError("C10.3")


def test_c10_3():
    pytest.skip("C10.3: write asserts from the hand exercises")


# C10.4
# Write `in_view_cone(pos, facing, target, half_angle_deg)`. Test with Exercise 10.10,
# then move the target around a circle of radius 5 about the character and print which
# angles are visible.


def in_view_cone(pos, facing, target, half_angle_deg):
    raise NotImplementedError("C10.4")


def test_c10_4():
    pytest.skip("C10.4: write asserts from the hand exercises")


# C10.5
# Write `reflect(v, n)` and simulate a ball inside a box for 500 steps, bouncing off
# all four walls. Assert that the speed never changes, and explain which of the
# chapter's facts guarantees that.


def reflect(v, n):
    raise NotImplementedError("C10.5")


def test_c10_5():
    pytest.skip("C10.5: write asserts from the hand exercises")

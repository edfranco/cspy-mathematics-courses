"""Chapter 7: Circles. Programming exercises C7.1 to C7.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C7.1
# Write `arc_length(r, deg)`, `sector_area(r, deg)` and `angle_from_arc(r, s)`. Test
# with Exercises 7.2 and 7.3 and assert the first and third are inverses.


def arc_length(r, deg):
    raise NotImplementedError("C7.1")


def sector_area(r, deg):
    raise NotImplementedError("C7.1")


def angle_from_arc(r, s):
    raise NotImplementedError("C7.1")


def test_c7_1():
    pytest.skip("C7.1: write asserts from the hand exercises")


# C7.2
# Write `circle_line_intersections(center, r, p, q)` for the line through points `p`
# and `q`, returning a list of 0, 1 or 2 points. Parametrize the line as p + t(q - p),
# substitute, and use the discriminant. Test with Exercises 7.8 and 7.9.


def circle_line_intersections(center, r, p, q):
    raise NotImplementedError("C7.2")


def test_c7_2():
    pytest.skip("C7.2: write asserts from the hand exercises")


# C7.3
# Write `tangent_length(d, r)` for the tangent from a point at distance `d` from the
# center, and `chord_distance(r, chord)`, each raising on impossible inputs. Test with
# Exercises 7.6 and 7.7.


def tangent_length(d, r):
    raise NotImplementedError("C7.3")


def chord_distance(r, chord):
    raise NotImplementedError("C7.3")


def test_c7_3():
    pytest.skip("C7.3: write asserts from the hand exercises")


# C7.4
# Write `radial_positions(n, r, center)` returning the n points of Exercise 7.10,
# using `math.radians` for the angle. Print them for n = 8 and confirm the first is
# directly to the right of the center.


def radial_positions(n, r, center):
    raise NotImplementedError("C7.4")


def test_c7_4():
    pytest.skip("C7.4: write asserts from the hand exercises")


# C7.5
# Write `ray_hits_circle(origin, direction, center, r)` that reuses C7.2 and keeps
# only intersections with t >= 0, returning the nearest hit or `None`. Test a ray that
# points away from the circle and one that starts inside it.


def ray_hits_circle(origin, direction, center, r):
    raise NotImplementedError("C7.5")


def test_c7_5():
    pytest.skip("C7.5: write asserts from the hand exercises")

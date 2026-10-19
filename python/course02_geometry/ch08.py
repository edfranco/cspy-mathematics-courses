"""Chapter 8: Right-Triangle Trigonometry. Programming exercises C8.1 to C8.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C8.1
# Write `sin_deg(t)`, `cos_deg(t)` and `tan_deg(t)` that take degrees, and test them
# against the exact values in Exercise 8.2 with `math.isclose`.


def sin_deg(t):
    raise NotImplementedError("C8.1")


def cos_deg(t):
    raise NotImplementedError("C8.1")


def tan_deg(t):
    raise NotImplementedError("C8.1")


def test_c8_1():
    pytest.skip("C8.1: write asserts from the hand exercises")


# C8.2
# Write `solve_right_triangle(**known)` that accepts any two of `a`, `b`, `c`, `A`,
# `B` (legs, hypotenuse, angles opposite them in degrees), refuses the two angles
# alone, and returns all five. Test with Exercises 8.3, 8.4 and 8.11.


def solve_right_triangle(**known):
    raise NotImplementedError("C8.2")


def test_c8_2():
    pytest.skip("C8.2: write asserts from the hand exercises")


# C8.3
# Write `polar_to_cartesian(d, deg)` and `cartesian_to_polar(dx, dy)` using
# `math.atan2`. Assert they round-trip for points in all four quadrants, and reproduce
# Exercise 8.9 to show where `math.atan` goes wrong.


def polar_to_cartesian(d, deg):
    raise NotImplementedError("C8.3")


def cartesian_to_polar(dx, dy):
    raise NotImplementedError("C8.3")


def test_c8_3():
    pytest.skip("C8.3: write asserts from the hand exercises")


# C8.4
# Write `height_from_elevation(distance, deg)` for an angle of elevation, and then the
# function `distance_from_depression(height, deg)` for an angle of depression. Verify
# Exercise 8.7.


def height_from_elevation(distance, deg):
    raise NotImplementedError("C8.4")


def distance_from_depression(height, deg):
    raise NotImplementedError("C8.4")


def test_c8_4():
    pytest.skip("C8.4: write asserts from the hand exercises")


# C8.5
# Build the table of sin and cos for 0 deg, 30 deg, 45 deg, 60 deg and 90 deg using
# only `math.sqrt` and the special-triangle ratios, no `math.sin`, then compare each
# entry with `math.sin` and `math.cos`.


def test_c8_5():
    pytest.skip("C8.5: write asserts from the hand exercises")

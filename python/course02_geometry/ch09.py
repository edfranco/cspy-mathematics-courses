"""Chapter 9: The Unit Circle and Radians. Programming exercises C9.1 to C9.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C9.1
# Write `deg_to_rad(d)` and `rad_to_deg(r)` using only `math.pi`, and assert they
# agree with `math.radians` and `math.degrees` for every integer degree from -720 to
# 720.


def deg_to_rad(d):
    raise NotImplementedError("C9.1")


def rad_to_deg(r):
    raise NotImplementedError("C9.1")


def test_c9_1():
    pytest.skip("C9.1: write asserts from the hand exercises")


# C9.2
# Write `unit_circle_point(theta)`. Assert x^2 + y^2 = 1 within tolerance for 1000
# random angles, and check Exercise 9.3 against exact values.


def unit_circle_point(theta):
    raise NotImplementedError("C9.2")


def test_c9_2():
    pytest.skip("C9.2: write asserts from the hand exercises")


# C9.3
# Write `wrap_2pi(theta)` into [0, 2pi) and `wrap_pi(theta)` into [-pi, pi). Test with
# Exercise 9.9 and with angles far outside one turn, such as 100pi + 1.


def wrap_2pi(theta):
    raise NotImplementedError("C9.3")


def wrap_pi(theta):
    raise NotImplementedError("C9.3")


def test_c9_3():
    pytest.skip("C9.3: write asserts from the hand exercises")


# C9.4
# Write `shortest_turn(from_deg, to_deg)` returning the signed turn in (-180, 180].
# Test with Exercise 9.10, with a turn of exactly 180 deg, and with two equal
# headings.


def shortest_turn(from_deg, to_deg):
    raise NotImplementedError("C9.4")


def test_c9_4():
    pytest.skip("C9.4: write asserts from the hand exercises")


# C9.5
# Write `orbit_position(t, omega, r, center)` for a point orbiting at angular speed
# `omega` radians per second, returning screen coordinates with y down. Confirm
# Exercise 9.11 at the right `t`, and print one full orbit at 12 steps to see the
# direction of travel.


def orbit_position(t, omega, r, center):
    raise NotImplementedError("C9.5")


def test_c9_5():
    pytest.skip("C9.5: write asserts from the hand exercises")

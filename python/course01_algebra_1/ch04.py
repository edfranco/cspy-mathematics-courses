"""Chapter 4: Linear Functions and Graphs. Programming exercises C4.1 to C4.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C4.1
# Write `lerp(a, b, t)` and `inverse_lerp(a, b, v)`, which returns the t for which
# lerp gives v. Assert they round-trip for a grid of values, and check Exercise 4.10.


def lerp(a, b, t):
    raise NotImplementedError("C4.1")


def inverse_lerp(a, b, v):
    raise NotImplementedError("C4.1")


def test_c4_1():
    pytest.skip("C4.1: write asserts from the hand exercises")


# C4.2
# Write `map_range(x, in_min, in_max, out_min, out_max)` using the two functions from
# C4.1, and verify Exercise 4.8 with it.


def map_range(x, in_min, in_max, out_min, out_max):
    raise NotImplementedError("C4.2")


def test_c4_2():
    pytest.skip("C4.2: write asserts from the hand exercises")


# C4.3
# Write `line_through(p1, p2)` returning `(m, b)` for a non-vertical line, or
# `("vertical", x)` when the two points share an x-coordinate. Test it with the points
# in Exercises 4.1 through 4.3 and with a vertical pair.


def line_through(p1, p2):
    raise NotImplementedError("C4.3")


def test_c4_3():
    pytest.skip("C4.3: write asserts from the hand exercises")


# C4.4
# Plot y = 3/2x - 7 and your perpendicular line from Exercise 4.7 on the same axes
# with matplotlib (the one allowed exception to the standard-library rule) or an HTML
# canvas. Observe that they only look perpendicular when both axes use the same scale,
# and explain why.


def test_c4_4():
    pytest.skip("C4.4: write asserts from the hand exercises")


# C4.5
# Write `ease_in_quad(t)` = t * t and print a table comparing it to `lerp(0, 100, t)`
# for t in 0, 0.25, 0.5, 0.75, 1. Which one is a linear function, and how can you tell
# from the table alone?


def ease_in_quad(t):
    raise NotImplementedError("C4.5")


def test_c4_5():
    pytest.skip("C4.5: write asserts from the hand exercises")

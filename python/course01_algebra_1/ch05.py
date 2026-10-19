"""Chapter 5: Systems of Linear Equations. Programming exercises C5.1 to C5.4.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C5.1
# Write `solve_2x2(a1, b1, c1, a2, b2, c2)` using Cramer's rule, returning `("one", x,
# y)`, `("none",)` or `("infinite",)`. When D is zero, decide between none and
# infinite by checking whether the two equations are proportional. Test with Exercises
# 5.1 through 5.6.


def solve_2x2(a1, b1, c1, a2, b2, c2):
    raise NotImplementedError("C5.1")


def test_c5_1():
    pytest.skip("C5.1: write asserts from the hand exercises")


# C5.2
# Write `intersect(p1, p2, p3, p4)` that takes two lines, each given by two points,
# and returns their intersection point or `None` when they are parallel. Build each
# line's standard-form coefficients from its two points and reuse C5.1. Verify
# Exercise 5.6 by picking two points on each line.


def intersect(p1, p2, p3, p4):
    raise NotImplementedError("C5.2")


def test_c5_2():
    pytest.skip("C5.2: write asserts from the hand exercises")


# C5.3
# Write `eliminate(rows)` that takes the augmented matrix `[[a1, b1, c1], [a2, b2,
# c2]]`, performs elimination with explicit row operations, and prints the matrix
# after each operation. Run it on Exercise 5.3 and compare the printed steps with your
# hand work.


def eliminate(rows):
    raise NotImplementedError("C5.3")


def test_c5_3():
    pytest.skip("C5.3: write asserts from the hand exercises")


# C5.4
# Write a brute-force checker that scans all integer pairs (x, y) from -20 to 20 and
# reports every pair satisfying both equations. Use it to confirm C5.1 on every
# exercise with integer answers, and to show that Exercise 5.4 has many solutions
# while Exercise 5.5 has none in that range.


def test_c5_4():
    pytest.skip("C5.4: write asserts from the hand exercises")

"""Chapter 9: Quadratics. Programming exercises C9.1 to C9.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C9.1
# Write `solve_quadratic(a, b, c)` returning `(count, roots)` where `count` is 0, 1 or
# 2 and `roots` is a sorted list. If a is zero, delegate to `solve_linear` from
# Chapter 3. Test with Exercises 9.1 through 9.7.


def solve_quadratic(a, b, c):
    raise NotImplementedError("C9.1")


def test_c9_1():
    pytest.skip("C9.1: write asserts from the hand exercises")


# C9.2
# Run C9.1 on a = 1, b = -100,000,000, c = 1. One root is wrong. Implement the stable
# version: compute q = -(b + sign(b)sqrt(D))/2, then x_1 = q/a and x_2 = c/q. Compare
# both versions and explain the term ``catastrophic cancellation'' in a comment.


def test_c9_2():
    pytest.skip("C9.2: write asserts from the hand exercises")


# C9.3
# Write `vertex(a, b, c)` and plot y = 2x^2 - 8x + 3 with its vertex marked. Confirm
# Exercise 9.8.


def vertex(a, b, c):
    raise NotImplementedError("C9.3")


def test_c9_3():
    pytest.skip("C9.3: write asserts from the hand exercises")


# C9.4
# Simulate Exercise 9.10 in steps of 0.01 seconds, advancing the height with the
# formula each step, and report the first time the height is at or below zero. Compare
# with the exact answer from the formula.


def test_c9_4():
    pytest.skip("C9.4: write asserts from the hand exercises")


# C9.5
# A sprite moves along x(t) = 2t^2 + 3t and a wall stands at x = 50. Use C9.1 to find
# the collision time, then confirm it by stepping the simulation.


def test_c9_5():
    pytest.skip("C9.5: write asserts from the hand exercises")

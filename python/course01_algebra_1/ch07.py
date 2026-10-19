"""Chapter 7: Exponents and Exponential Growth. Programming exercises C7.1 to C7.5.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C7.1
# Write `power(base, n)` for any integer n, negative included, with a simple loop.
# Then write `fast_power(base, n)` using squaring (if n is even, square the result for
# n/2; if odd, multiply by the base once more). Count the multiplications each version
# makes for n = 1000.


def power(base, n):
    raise NotImplementedError("C7.1")


def fast_power(base, n):
    raise NotImplementedError("C7.1")


def test_c7_1():
    pytest.skip("C7.1: write asserts from the hand exercises")


# C7.2
# Write `bits_needed(n)` that returns the smallest k with 2^k >= n. Verify it against
# `(n - 1).bit_length()` for every n from 2 to 100,000 and explain in a comment why
# that expression works.


def bits_needed(n):
    raise NotImplementedError("C7.2")


def test_c7_2():
    pytest.skip("C7.2: write asserts from the hand exercises")


# C7.3
# Write `to_binary(n)` by repeated division by 2 and `from_binary(s)` by place values,
# without `bin()` or `int(s, 2)`. Assert they round-trip for every n from 0 to 5000,
# and check Exercise 7.10.


def to_binary(n):
    raise NotImplementedError("C7.3")


def from_binary(s):
    raise NotImplementedError("C7.3")


def bin():
    raise NotImplementedError("C7.3")


def test_c7_3():
    pytest.skip("C7.3: write asserts from the hand exercises")


# C7.4
# Starting from 1000, print a year-by-year table of a linear account that adds 50 per
# year and an exponential account that grows 5% per year. Find the first year the
# exponential account is ahead, and the first year it is ahead by more than 1000.


def test_c7_4():
    pytest.skip("C7.4: write asserts from the hand exercises")


# C7.5
# Compute `2**53 + 1` as an integer and as a float. Show that the float version equals
# `2**53`, and explain the result in one sentence using the 53-bit precision of a
# double.


def test_c7_5():
    pytest.skip("C7.5: write asserts from the hand exercises")

"""Chapter 1: Logic and Proof. Programming exercises C1.1 to C1.4.

Solve the hand exercises first (see handwritten/), then implement each
function and turn its test into real asserts using those answers.
Standard library only; matplotlib is allowed for plots.
"""

import pytest


# C1.1
# Write `implies(p, q)` returning the truth value of p Rightarrow q (false only when p
# is true and q is false). Print a truth table over all four combinations for the
# statement, its converse, inverse and contrapositive, and confirm which columns
# match.


def implies(p, q):
    raise NotImplementedError("C1.1")


def test_c1_1():
    pytest.skip("C1.1: write asserts from the hand exercises")


# C1.2
# Write `find_counterexample(hypothesis, conclusion, candidates)` that returns the
# first candidate where the hypothesis holds and the conclusion fails, or `None`. Use
# it on Exercise 1.3 with lambdas over the integers 1 to 100.


def find_counterexample(hypothesis, conclusion, candidates):
    raise NotImplementedError("C1.2")


def test_c1_2():
    pytest.skip("C1.2: write asserts from the hand exercises")


# C1.3
# Write `factorial(n)` that asserts its precondition and, in a wrapper, asserts the
# postcondition n! = n * (n-1)! for n >= 1. Show that a call violating the
# precondition fails at the assertion rather than returning a wrong value.


def factorial(n):
    raise NotImplementedError("C1.3")


def test_c1_3():
    pytest.skip("C1.3: write asserts from the hand exercises")


# C1.4
# Represent a two-column proof as a list of `(statement, reason, depends_on)` tuples,
# where `depends_on` lists earlier line numbers. Write `check_proof(lines,
# allowed_reasons)` that rejects any reason not in the allowed set and any dependency
# on a later line. Encode the proof in Example 1.2.


def check_proof(lines, allowed_reasons):
    raise NotImplementedError("C1.4")


def test_c1_4():
    pytest.skip("C1.4: write asserts from the hand exercises")

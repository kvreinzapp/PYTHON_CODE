"""Generalization."""
from math import pi, sqrt


def area(r, shape_constant):
    assert r > 0, "a length must be positive"
    return r * r * shape_constant


def area_square(r):
    return area(r, 1)


def area_circle(r):
    return area(r, pi)


def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


def sum_natural(n):
    """Sum the first N natural numbers
    >>> sum_natural(5)
    15
    """
    return summation(n, identity)


def sum_cubes(n):
    """Sum the first N cubes of natural numbers
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """Sum the first N terms of the sequence
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

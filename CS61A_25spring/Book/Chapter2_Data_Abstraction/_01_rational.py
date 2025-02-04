"""
Assume we already have the selector: numer(x), denom(x), 
and the constructor: rational(n,d), 
then we could add, multiply, print and test equality
"""

from math import gcd


# gcd means greatest common denominator
def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]


def numer(x):
    """Return the 1st component"""
    return x[0]


def denom(x):
    """Return the 2nd component"""
    return x[1]


def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rationals(x, y):
    return (rational(numer(x) * numer(y), denom(x) * denom(y)))


def print_rationals(x):
    print(numer(x), '/', denom(x))


def rational_are_euqal(x, y):
    """Using math fomular to simpify the code"""
    return numer(x) * denom(y) == numer(y) * denom(x)

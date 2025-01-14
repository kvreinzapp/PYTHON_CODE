from math import sqrt


def has_big_sqrt(x):
    return x > 0 and sqrt(x) > x


def reasonable(n):
    return n == 0 or 1 / n != 0


def do_want_3_partners(n):
    return n == 3 or n % 3 != 0

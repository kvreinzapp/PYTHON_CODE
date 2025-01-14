def if_(c, t, f):
    if c:
        return t
    else:
        return f


from math import sqrt


def real_sqrt(x):
    if_(x >= 0, sqrt(x), 0)

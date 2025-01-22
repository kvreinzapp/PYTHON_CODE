def improve(update, close, guess=1):
    """Return golden ratio, based on guess
    >>> improve(golden_update, suqare_close_to_successor)
    1.6180339887498951
    """
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1 / guess + 1


def suqare_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


phi = improve(golden_update, suqare_close_to_successor, 1)
print(phi)
phi = improve(golden_update, suqare_close_to_successor, 2)
print(phi)

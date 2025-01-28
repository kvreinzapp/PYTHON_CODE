def remove_mine(n, digit):
    """
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    remainder, timer = 0, 1
    while (n != 0):
        last = n % 10
        if (last == digit):
            n = n // 10
            continue
        else:
            remainder, timer = remainder + timer * last, timer * 10
            n = n // 10
    return remainder


def remove(n, digit):
    """Return all digits of non-negative N 
    that are not DIGITS, for some
    non-negative DIGIT less than 10
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while (n != 0):
        n, last = n // 10, n % 10
        if (last != digit):
            kept = kept + last * digits**10
            digits = digits + 1
    return

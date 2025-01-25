def is_odd(n):
    if 0 == n:
        return False
    else:
        return is_even(n - 1)


def is_even(n):
    if 0 == n:
        return True
    return is_odd(n - 1)


def is_odd_no_mutual(n):
    if 0 == n:
        return False
    else:
        if n - 1 == 0:
            return True
        else:
            return is_odd_no_mutual((n - 1) - 1)

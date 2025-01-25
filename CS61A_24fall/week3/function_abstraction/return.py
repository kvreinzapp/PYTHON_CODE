def end_mine(n, d):
    """Print the final digits of N in reverse order until D is found
    >>> end(34567, 5)
    7
    6
    5
    """
    k = 0
    while (k < n):
        print(n % 10)
        if (n % 10 == d):
            break
        n = n // 10


def end(n, d):
    """Print the final digits of N in reverse order until D is found
    >>> end(34567, 5)
    7
    6
    5
    """
    while (n > 0):
        last, n = n % 10, n // 10
        print(last)
        if (last == d):
            return None


def search_complex(g):
    x = 0
    while (True):
        if (g(x)):
            return x
        x += 1


def search(g):
    x = 0
    while not g(x):
        x += 1
    return x


def is_three(x):
    return x == 3


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


# now this means search the x which satisfy the requirement of pass in function
search(positive)


def inverse(f):
    """Return g(y), such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)

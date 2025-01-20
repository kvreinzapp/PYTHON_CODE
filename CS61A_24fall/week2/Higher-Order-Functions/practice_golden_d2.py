def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


"""universal functions"""


def approx_eq(a, b, tolerance=1e-6):
    return abs(a - b) <= tolerance


def average(a, b):
    return (a + b) / 2


def power(x, n):
    total, k = 1, 0
    while (k < n):
        total, k = total * x, k + 1
    return total


"""golden ratio"""


def update_golden(guess):
    return 1 + 1 / guess


def close_golden(guess):
    return approx_eq(guess, 1 + 1 / guess)


"""square root of a"""


def sqrt(a):

    def update_sqrt(x):
        return average(x, a / x)

    def close_sqrt(x):
        return approx_eq(x, average(x, a / x))
        #return approx_eq(x * x, a)
        #return approx_eq(2 * x, x + a / x)

    return improve(update_sqrt, close_sqrt)


"""newton's method, return nth root of a"""


def update_newton(f, df):

    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df):

    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(update_newton(f, df), near_zero)


def nth_root_of_a(a, n):

    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


"""result code"""
print(improve(update_golden, close_golden))
print(sqrt(16))
print(nth_root_of_a(16, 2))

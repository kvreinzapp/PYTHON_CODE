# i need a function named improve to improve my guess to the final result
# fist thing i want to improve is improve my guess to golden ratio
# update my guess, check out the difference between guess*guess and guess+1, until this gap is really small
def improve(update, close, guess=1):
    """Update guess(default=1) to what we want, 
       accept the update and close functions
    """
    while not close(guess):
        guess = update(guess)
    return guess


def update_golden(guess):
    """Update new golden guess
    """
    return 1 + 1 / guess


def average(x, y):
    return (x + y) / 2


def sqrt(a):

    def update_sqrt(x):
        return average(x, a / x)

    def close_sqrt(x):
        return approx_eq(x * 2, x + a / x)

    return improve(update_sqrt, close_sqrt)


def close_golden(guess):
    """Satisfy golden number or not
    """
    return approx_eq(guess * guess, guess + 1)


def approx_eq(x, y, tolerance=1e-9):
    """2 numbers close enough or not
    """
    return abs(x - y) < tolerance


def newton_update(f, df):

    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df):

    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):

    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


def power(x, n):
    product, k = 1, 0
    while (k < n):
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):

    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


print(improve(update_golden, close_golden))
print(sqrt(16))
print(nth_root_of_a(2, 16))

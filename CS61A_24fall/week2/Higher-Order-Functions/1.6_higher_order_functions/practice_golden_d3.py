def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-6):
    return abs(x - y) < tolerance


def average(x, y):
    return (x + y) / 2


def update_golden(guess):
    return 1 + 1 / guess


def close_golden(guess):
    return approx_eq(guess * guess, guess + 1)


def sqrt(a):

    def update_sqrt(guess):
        return average(guess, a / guess)

    def close_sqrt(guess):
        return approx_eq(guess * guess, a)

    return improve(update_sqrt, close_sqrt)


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
        return pow(x, n) - a

    def df(x):
        return n * pow(x, n - 1)

    return find_zero(f, df)


def update_newton_bigger(a, n):

    def f(x):
        return pow(x, n) - a

    def df(x):
        return n * pow(x, n - 1)

    def update(x):
        return x - f(x) / df(x)

    def close_newton(x):
        return approx_eq(f(x), 0)

    return improve(update, close_newton)


n = 225
a = 2
print(f"golden ratio = {improve(update_golden, close_golden)}")
print(f"sqrt of {n} is  = {sqrt(n)}")
print(f"{n}'s root of {a} is  = {nth_root_of_a(n, a)}")
print(f"{n}'s root of {a} is  = {update_newton_bigger(n, a)}")

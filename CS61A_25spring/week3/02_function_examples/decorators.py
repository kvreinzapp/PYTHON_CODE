def trace1(fn):
    """Return a version of fn that first prints before it is called.
    fn - a function of 1 argument
    """

    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)

    return traced


@trace1
def square(x):
    return x * x


@trace1
def sum_squares_up_to(n):
    k, total = 1, 0
    while (k <= n):
        total, k = total + square(k), k + 1
    return total


sum_squares_up_to(5)

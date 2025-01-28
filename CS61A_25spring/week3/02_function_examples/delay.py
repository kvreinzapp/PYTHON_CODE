from operator import mul, add


def square(x):
    return mul(x, x)


def delay(arg):
    """mine: a function that return a function which will return parent's argument
    video: a function that takes any argument and returns a function that returns that arg
    """
    print("delayed")

    def g():
        return arg

    return g


delay(delay)()(6)()


def private(arggg):
    print("matey")

    def plunder(arggg):
        return arggg

    return plunder


add(private(3)(square)(4), 1)
private(private(private))(5)(7)

def square(x):
    return x * x


def successor(x):
    return x + 1


def compose1(g, h):

    def f(x):
        return g(h(x))

    return f

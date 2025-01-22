def trace(fn):

    def wrapper(x):
        print('->', fn, '(', x, ')')
        return fn(x)

    return wrapper


@trace
def triple(x):
    return x * 3


triple(12)


# modify
def add_layer(fn):

    def wrapper(x):

        return fn(x)

    return wrapper

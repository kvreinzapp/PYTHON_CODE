def make_adder(n):
    """Return a function that take an argument K and return K+N
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """

    def add(k):
        return n + k

    return add

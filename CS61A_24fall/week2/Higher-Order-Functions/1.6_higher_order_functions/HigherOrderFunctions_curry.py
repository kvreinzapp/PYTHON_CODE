def pow(a, n):
    result, k = 1, 0
    while (k < n):
        result, k = result * a, k + 1
    return result


def curried_pow(x):

    def h(y):
        return pow(x, y)

    return h


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1


start = 1
end = 10
n = 2
print(f"from {start} to {end}, do some pow{n}",
      map_to_range(0, 10, curried_pow(n)))


def curry2(f):
    """Return a curried version of the given two-argument function"""

    def g(x):

        def h(y):
            return f(x, y)

        return h

    return g


def uncurry2(g):
    """Return a two-arguments funciton of a given curried funciton"""

    def f(x, y):
        return g(x)(y)

    return f


print(f"show me this works or not, {uncurry2(curried_pow)(2,3)}")

print(f"from {start} to {end}, do some pow{n}",
      map_to_range(0, 10,
                   curry2(pow)(n)))


def curry5(f):
    """why about more arguments, any patterns?"""

    def g(x):

        def h(y):

            def d(z):

                def w(s):

                    def e(p):
                        return f(x, y, z, s, p)

                    return e

                return w

            return d

        return h

    return g


def add5(a, b, c, d, e):
    return a + b + c + d + e


print(f"This works, {curry5(add5)(1)(2)(3)(4)(5)}")

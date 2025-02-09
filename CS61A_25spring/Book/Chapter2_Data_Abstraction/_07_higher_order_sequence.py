from operator import mul, add


def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]


def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]


def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced


mul_result = reduce(mul, [2, 4, 8], 1)
print(mul_result)
add_result = reduce(add, [2, 4, 8], 0)
print(add_result)


def divisor_of(n):
    divisor_func = lambda x: n % x == 0
    return [1] + keep_if(divisor_func, range(2, n))


#def divisors(n):
#    return [1] + [x for x in range(2, n) if n % x == 0]

print(divisor_of(12))

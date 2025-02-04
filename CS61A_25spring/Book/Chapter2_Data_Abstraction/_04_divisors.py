def divisors_mine(n):
    return [x for x in range(1, n) if n % x == 0]


def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]


[x for x in range(1, 1000) if x == sum(divisors(x))]

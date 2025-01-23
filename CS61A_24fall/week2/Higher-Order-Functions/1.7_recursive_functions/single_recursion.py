def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last


def fact_iter(n):
    total, k = 1, 1
    while (k <= n):
        total, k = total * k, k + 1
    return total


def fact(n):
    if 1 == n:
        return 1
    else:
        return fact(n - 1) * n

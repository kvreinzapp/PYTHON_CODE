def split(n):
    return n // 10, n % 10


def sum_digits_iter_mine(n):
    total = 0
    while (n > 0):
        total, n = total + n % 10, n // 10
    return total


def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum


def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)

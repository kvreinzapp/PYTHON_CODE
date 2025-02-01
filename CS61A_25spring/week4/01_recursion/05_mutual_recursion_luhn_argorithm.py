def split(n):
    return n // 10, n % 10


def digits_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return digits_sum(all_but_last) + last


def luhn_double(n):
    assert (n > 0 and n < 9)
    if n < 5:
        return 2 * n
    else:
        a, b = split(2 * n)
        return a + b


def luhn_sum_mine(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double_mine(all_but_last) + last


def luhn_sum_double_mine(n):
    if n < 10:
        return luhn_double(n)
    else:
        all_but_last, last = split(n)
        return luhn_sum_mine(all_but_last) + luhn_double(last)


"""Now is the book version"""


def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = digits_sum(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def fib(n):
    """Compute the nth Fibonacci number, N>=0"""
    pre, curr = 1, 0
    k = 0
    while (k < n):
        pre, curr = curr, pre + curr
        k += 1
    return curr


def fib_expression(n):
    """Give Fibonacci expression that up to N, N>=0
    >>> fib_expression(8)
    0
    1
    1
    2
    3
    Till 4th number which is 3, total = 7.
    >>> fib_expression(7)
    0
    1
    1
    2
    3
    Till 4th number which is 3, total = 7.
    """
    total, k = 0, 0
    while (total < n):
        total = total + fib(k)
        if (total > n):
            break
        print(fib(k))
        k = k + 1
    print(f"Till {k-1}th number which is {fib(k-1)}, total = {total-fib(k)}.")


"""
        totoal fib(k) k
        0      0      0
    >   0      0      1      1
        1      1      2      1
        2      1      3      2
        4      2      4      3
        7      3      5      5
        12     null     6


    totoal fib(k) k
    0      0      0
  > 0      0      1    0
    1      1      2    1
    2      1      3    1
    4      2      4    2
    7      3      5    3
    12     null   null    5
"""
""" 
print fib(k) than total, which this fib(k) we do not want
calculate toal, then print fib(k), which also print the bigger one
"""

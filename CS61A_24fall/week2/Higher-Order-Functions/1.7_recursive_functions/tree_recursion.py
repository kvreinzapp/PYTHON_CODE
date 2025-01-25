def fib_iter(n):
    pre, curr = 1, 0
    k = 0
    while (k < n):
        pre, curr = curr, pre + curr
        k = k + 1
    return curr


def fib(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    return fib(n - 2) + fib(n - 1)


def count_partitions_kv(n, m):
    """return ways to depart the number n, the bigest part <= m"""
    if m == 1:
        return 1
    elif m == 0:
        return 0
    else:
        if n > m:
            return count_partitions_kv(n, m - 1) + count_partitions_kv(
                n - m, m)
        else:
            return count_partitions_kv(n, n - 1) + 1


def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 1
    else:
        return count_partitions(n, m - 1) + count_partitions(n - m, m)

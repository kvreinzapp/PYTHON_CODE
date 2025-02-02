def count_partitions(n, m):
    if (n == 0):
        return 1
    elif (m == 1):
        return 1
    elif (n < 0):
        return 0
    else:
        return count_partitions(n, m - 1) + count_partitions(n - m, m)

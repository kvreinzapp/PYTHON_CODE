def count_mine(s, value):
    """Count the number of occurrences of value in sequence s"""
    count = 0
    for ele in s:
        if ele == value:
            count += 1
    return count


def count(s, value):
    """Count the number of occurrences of value in sequence s"""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total

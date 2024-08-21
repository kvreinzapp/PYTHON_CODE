def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    lst = list()
    while (x > 0):
        lst.append(x % 10)
        x = x // 10

    currentValue = lst[0]
    for i in range(1, len(lst)):
        if currentValue < lst[i]:
            return False
    return True

empty = "empty"


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair.
    >>> is_link(empty)
    True
    >>> is_link([2, empty])
    True
    """
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first element and the rest.
    >>> link(1, link(2, link(3, empty)))
    [1, [2, [3, 'empty']]]
    """
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """Return the first element of a linked list s.
    >>> first([1, [2, [3, 'empty']]])
    1
    """
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s.
    >>> rest([1, [2, [3, 'empty']]])
    [2, [3, 'empty']]
    """
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]


four = link(1, link(2, link(3, link(4, empty))))


def len_link_recursive(s):
    """Return the length of a linked list s.
        >>> len_link_recursive(four)
        4
        """
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s.
        >>> getitem_link_recursive(four, 1)
        2
        """
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def extend_link(s, t):
    """
    Return a list with the elements of s followed by those of t.
    >>> extend_link(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    """
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    """
    Apply f to each element of s.
    >>> apply_to_all_link(lambda x: x*x, four) 
    [1, [4, [9, [16, 'empty']]]]
    """
    if s == empty:
        return empty
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


def keep_if_link(f, s):
    """
    Return a list with elements of s for which f(e) is true.
    >>> keep_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]
    """
    if s == empty:
        return empty
    elif f(first(s)):
        return link(first(s), keep_if_link(f, rest(s)))
    else:
        return keep_if_link(f, rest(s))


def join_link(s, separator):
    """
    Return a string of all elements in s separated by separator.
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

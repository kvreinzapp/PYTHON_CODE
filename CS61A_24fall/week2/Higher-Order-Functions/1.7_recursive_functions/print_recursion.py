def is_even(n):
    if 0 == n:
        return True
    else:
        return is_odd(n - 1)


def is_odd(n):
    if 0 == n:
        return False
    else:
        return is_even(n - 1)


def cascade(n):
    # i want to display that way, how
    # you need recursion
    # you need a base linea
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade_improve(n):
    """
    Since pirnt() show up in both clauses, we reduece it
    And we replace if with a opposite condition
    """
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)


def play_alice(n):
    if (0 == n):
        print("Bob wins!")
    else:
        play_bob(n - 1)


def play_bob(n):
    if (0 == n):
        print("Alice wins!")
    elif (is_even(n)):
        play_alice(n - 2)
    else:
        play_alice(n - 1)

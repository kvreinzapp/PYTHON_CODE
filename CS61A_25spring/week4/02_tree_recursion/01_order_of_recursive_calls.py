def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade_shorter(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)


"""
which one is better
clear > short
"""

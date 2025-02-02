def fib(n):
    """it's tree recursion and pretty slow, but just for now, cause we gonna optimize it in the future by reducing repetition"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

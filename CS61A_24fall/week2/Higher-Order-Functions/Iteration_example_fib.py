def fib(n):
    """Compute the nth Fibonacci number"""
    pre, curr = 1, 0
    k = 0
    while (k < n):
        pre, curr = curr, pre + curr
        k += 1
    return curr


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))

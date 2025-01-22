def compose1(f, g):
    return lambda x: f(g(x))


f = compose1(lambda x: x * x, lambda y: y + 1)
result = f(12)

# a neater one
compose = lambda f, g: lambda x: f(g(x))

f = compose(lambda x: x * x, lambda y: y * y)
print(f(3))

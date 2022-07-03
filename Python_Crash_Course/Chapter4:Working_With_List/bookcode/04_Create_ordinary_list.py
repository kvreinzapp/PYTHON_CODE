squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# Omit the temporary vraible square
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# You can use either of these two approaches when you’re making more
# complex lists. Sometimes using a temporary variable makes your code eas-
# ier to read
# other times it makes the code unnecessarily long. Focus first on
# writing code that you understand clearly, which does what you want it to do.
# Then look for more efficient approaches as you review your code.

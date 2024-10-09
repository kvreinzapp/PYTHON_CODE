n = int(input("Give me your number: "))
number = n
while (number != 1):
    if (number % 2 == 0):
        number = number / 2
    else:
        number = number * 3 + 1
    if (number == n):
        print("Huh, the counter example")
print("Sadly", n, "is not what you want")

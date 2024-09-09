import re

numbers = list()
total = 0
handle = open('regex_sum_real.txt')
for line in handle:
    numbers = numbers + re.findall('[0-9]+', line)
for number in numbers:
    number = int(number)
    total = total + number
print(total)

fh = input('give me a number: ')
x = int(fh)
lst = list()
while (x > 0):
    lst.append(x % 10)
    x = x // 10
currentValue = lst[0]
for i in range(1, len(lst)):
    if currentValue < lst[i]:
        print('false cause', currentValue, '<', lst[i])
        break
print('the end')

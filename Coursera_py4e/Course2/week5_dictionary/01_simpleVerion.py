count = dict()
names = ['zapp', 'klaus', 'leo', 'zapp', 'leo']
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)

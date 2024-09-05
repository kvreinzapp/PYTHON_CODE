dc = {'a': 3, 'b': 55, 'c': 23, 'd': 1}
tmp = list()
for k, v in dc.items():
    tmp.append((v, k))
print(tmp)
print(sorted(tmp, reverse=True))

handle = open('romeo.txt')
lst = list()
for line in handle:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))

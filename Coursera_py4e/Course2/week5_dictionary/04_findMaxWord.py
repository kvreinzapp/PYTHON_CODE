name = input('Enter File: ')
if len(name) < 1:
    name = '../animalFarmChapter1.txt'

handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None
for word, count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

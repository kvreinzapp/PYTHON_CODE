fh = open('mbox-short.txt')
count = 0
for line in fh:
    if not line.startswith('From:'):
        continue
    count = count + 1
    words = line.split()
    print(words[1])
print(count)

name = input("Enter file:")
if len(name) < 1:
    name = "../mbox-short.txt"
handle = open(name)

wordCount = dict()
for line in handle:
    if line.startswith('From:'):
        words = line.split()
        wordCount[words[1]] = wordCount.get(words[1], 0) + 1

bigword = None
bigcount = None
for word, count in wordCount.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

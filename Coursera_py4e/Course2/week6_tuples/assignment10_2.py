fhandle = open('../mbox-short.txt')
hourCount = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        fullTime = words[5]
        departTime = words[5].split(':')
        hourCount[departTime[0]] = hourCount.get(departTime[0], 0) + 1

for k, v in sorted(hourCount.items()):
    print(k, v)

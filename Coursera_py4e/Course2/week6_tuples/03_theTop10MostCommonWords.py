fhandle = open('../animalFarmChapter1.txt')
wordCount = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        wordCount[word] = wordCount.get(word, 0) + 1

wordCountList = list()
for k, v in wordCount.items():
    wordCountList.append((v, k))

finalList = sorted(wordCountList, reverse=True)[0:10]
for v, k in finalList:
    print(k, v)

handle = open("../animalFarmChapter1.txt").read()
words = handle.split()

wordCount = dict()
for word in words:
    wordCount[word] = wordCount.get(word, 0) + 1

print(type(wordCount.keys()))

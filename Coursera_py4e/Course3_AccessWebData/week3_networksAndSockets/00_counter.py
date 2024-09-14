fileName = input('enter you file name: ')
handle = open(fileName)
string = handle.read()
print('total characters: ', len(string))
handle.seek(0)

wordsCounter = 0
characterCounter = 0
for line in handle:
    characterCounter = characterCounter + len(line)
    words = line.split()
    for word in words:
        wordsCounter = wordsCounter + 1
print('Total words: ', wordsCounter)
print('Total character: ', characterCounter)

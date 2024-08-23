count = dict()
print("Enter the line: ")
line = input('')

words = line.split()

print('Words', words)

print('Counting...')
for word in words:
    count[word] = count.get(word, 0) + 1
print('Counts', count)

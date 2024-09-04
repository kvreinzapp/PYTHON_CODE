handle = open('../theZenOfPython.txt')
for line in handle:
    if line.startswith('A'):
        print(line)

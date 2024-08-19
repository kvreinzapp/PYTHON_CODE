handle = open('text1.txt')
for line in handle:
    if line.startswith('hi'):
        print(line)

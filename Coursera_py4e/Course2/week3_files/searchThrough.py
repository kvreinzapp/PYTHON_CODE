handle = open('text.txt')
for line in handle:
    if line.startswith('hi'):
        print(line)

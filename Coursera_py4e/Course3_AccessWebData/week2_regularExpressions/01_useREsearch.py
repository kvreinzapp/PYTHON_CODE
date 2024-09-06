import re

handle = open("../mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if line.find('From:'):
        print(line)

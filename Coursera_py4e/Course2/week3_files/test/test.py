t = input("give me the file: ")
handle = open(t)
for line in handle:
    print(line.strip())

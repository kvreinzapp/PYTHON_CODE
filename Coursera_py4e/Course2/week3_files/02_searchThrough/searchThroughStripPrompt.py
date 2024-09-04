prompt = input('please enter you file name:')
handle = open(prompt)
for line in handle:
    if not 'A' in line:
        print(line.strip())

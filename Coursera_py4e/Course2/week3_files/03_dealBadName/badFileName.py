file = input("give me the file: ")
try:
    handle = open(file)
except:
    print("file can not be opened: ", file)
#    quit()

count = 0
for line in handle:
    count = count + 1
print("there are", count, 'lines in', file)

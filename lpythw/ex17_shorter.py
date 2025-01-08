from sys import argv

scritp, from_file, to_file = argv
out_file = open(to_file, 'w').write(open(from_file).read())
print(out_file)

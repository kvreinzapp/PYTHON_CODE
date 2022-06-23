# things about quote
person = 'finch'

print("Part1\n")
print('hello,"finch"')
print("hello,'finch'")
# print('hello,'finch'')  #SyntaxError: invalid syntax
# print("hello,"finch"")  #SyntaxError: invalid syntax

print("\nPart2--compared with Part1\n")
# same reason
print(f"'{person}'")
print(f'"{person}"')
# print(f""{person}"")  #SyntaxError: invalid syntax
# print(f''{person}'')  #SyntaxError: invalid syntax

print("\nPart3--another way to accomlish that\n")
# another worked way
print(f"\"{person}\"")
print(f"\'{person}\'")

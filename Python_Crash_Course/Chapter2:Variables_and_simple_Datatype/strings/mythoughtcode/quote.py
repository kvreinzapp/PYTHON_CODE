# things about quote
print('\ntest')
print('hello,"finch"')
print("hello,'finch'")
# print('hello,'finch'')  #SyntaxError: invalid syntax
# print("hello,"finch"")  #SyntaxError: invalid syntax
# same reason
print(f"'{person}'")
print(f'"{person}"')
# print(f""{person}"")  #SyntaxError: invalid syntax
# print(f''{person}'')  #SyntaxError: invalid syntax
# another worked way
print(f"\"{person}\"")
print(f"\'{person}\'")

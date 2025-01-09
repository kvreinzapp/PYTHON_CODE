import ex31
from dis import dis

# Compile the code string into a code object
code_obj = compile(
    '''
if cars>people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
''', '<string>', 'exec')

# Disassemble the code object
dis(code_obj)

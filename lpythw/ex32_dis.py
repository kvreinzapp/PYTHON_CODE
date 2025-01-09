import ex32
from dis import dis

# Compile the code string into a code object
code_obj = compile(
    '''
if door == "1":
    print("1")
    bear = input("> ")
    if bear == "1":
        print("bear1")
    elif bear == "2":
        print("bear2")
    else:
        print("bear3")
''', '<string>', 'exec')

# Disassemble the code object
dis(code_obj)

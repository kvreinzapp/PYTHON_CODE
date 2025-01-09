from dis import dis

# Compile the code string into a code object
code_obj = compile(
    '''
import ex26

print("name", ex26.name)
print("height", ex26.height)

from pprint import pprint

# Print the dictionary representation of the ex26 module
pprint(ex26.__dict__)

# Demonstrate accessing the height attribute
print("ex26.height gives me", ex26.height)
print('ex26.__dict__["height"] gives me', ex26.__dict__["height"], "too")

# Modify height using the __dict__ and print the updated values
print(f"I am currently {ex26.height} inches tall.")
ex26.__dict__["height"] = 1000
print(f"I am now {ex26.height} inches tall.") 

# Modify height using direct attribute assignment and print the updated dictionary value
ex26.height = 26
print(f"Oops, now I'm {ex26.__dict__['height']} inches tall.") 

# Demonstrate pprint's functionality and documentation
pprint(pprint.__doc__)
help(pprint)

''', '<string>', 'exec')

# Disassemble the code object
dis(code_obj)

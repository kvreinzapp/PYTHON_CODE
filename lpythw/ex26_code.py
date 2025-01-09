import ex26

print("name", ex26.name)
print("height", ex26.height)

from pprint import pprint

pprint(ex26.__dict__)

print("ex26.height gives me", ex26.height)
print("ex26.__dict__[\"height\"] gives me", ex26.__dict__["height"], "too")

print(f"I am currently {ex26.height} inches tall.")
ex26.__dict__["height"] = 1000
print(f"I am now {ex26.height} inches tall.") 

ex26.height = 26
print(f"Oops, now I'm {ex26.__dict__["height"]} inches tall.") 

pprint(pprint.__doc__)
help(pprint)


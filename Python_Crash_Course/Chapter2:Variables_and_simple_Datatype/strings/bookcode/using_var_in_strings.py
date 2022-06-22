# By f-strings
frist = "There is NOTHING NOBLE in being superior to some other man"
second = "The true nobility is in being superior to YOR PREVIOUS SELF"
print(f"{frist}{second}")
print(f"{frist}{second}".upper())
final = f"{frist}{second}".lower()
print(final)

print("\nI say:{final}")
print(f"\nI say:{final}")
print(f"\nI say: {final}")

print("\nNOW"f"I say:{final}")
print("NOW"      f"I say:{final}")
print("NOW", f"I say:{final}")


print("\n")
# sum
want = "orld"
# print("w"want)  # wrong way
print("w", want)  # right way but needn't
# so how to do this? two ways
# first
print(f"w{want}")
# second
print("w"f"{want}")
# """"can, but vriable can't(meanwhile the , is necessary)

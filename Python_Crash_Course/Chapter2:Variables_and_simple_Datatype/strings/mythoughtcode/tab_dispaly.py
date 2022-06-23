person = "\tKlausveinherz\t"
print('######################')
print("<what sapce\toccupied>""\t<none>")
print("<what sapce \toccupied>""\t<left>")
print("<what sapce\t occupied>""\t<right>")
print("<what sapce \t occupied>""\t<both>")
print("[It seems that a blank sapce is important.]")
print("[Only when you put one in LEFT side, the \t will work]\n")
print('<What i input>')
print(person)
print("[former:4, latter:3]")
# print them
print('\n<show the space>')
print('######################')
print(f"'{person.lstrip()}'")
print(f"'{person.rstrip()}'")
print(f"'{person.strip()}'")
print("[former:3, latter:2]")
# conclusion
print("[It seems that the extra character like ' whill occupy the space of \t]")
print("[things like below]")
print(f"''{person}''")
# print them in another way
print('\n<Hide the space>')
print(person.lstrip())
print(person.rstrip())
print(person.strip())
print("[former:4, latter:3]")


# quite tricky thing, i didn't figure this out in 2022/6/22
# I try a lot of times, it seem that whether a blank space is in the left of the tab is matters.
# And seems that some charactor will occupy the part of the tab
# But the whole thing is quite blur now(2022/6/22``)

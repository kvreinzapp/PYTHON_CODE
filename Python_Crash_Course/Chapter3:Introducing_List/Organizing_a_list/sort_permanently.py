# sort()--a method
biscuit = ['a', 'd', 'f', 'g', 'e', 'k']
#sort is alphabetically
biscuit.sort()
print(biscuit)
# sort it in a reverse way
biscuit.sort(reverse=True)
print(biscuit)

# a contrast between sort() and pop(), they are different``
print(biscuit.sort())   # this line will cause to print a None
print(biscuit.pop())    # this line print a k

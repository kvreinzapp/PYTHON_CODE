# del--a statement
print('Using \t<del>\t to remove if you know the index of it')
print("[PA that \t<del>\t is a statement instead of a method]\n")
outlook = ['hat', 'shoes', 'pants', 'glasses', 'skirt']
print(f"Now the outlook is {outlook}")
del outlook[0]
print(f"Now the outlook is {outlook}")
del outlook[-1]
print(f"Now the outlook is {outlook}")
print("[Index using -1 works here]")

# pop()--a method
print("\nUsing\tpop()\tto remove the last one, and use it after removing")
food = ['apple', 'beef', 'chicken', 'rice']
# last_food = food.pop()
print(f"The last thing I ate is { food.pop()}")
print(f"The second thing I ate is { food.pop(1)}")
# Both way works
# You can use index too, because it is a method
print("[Delete forever--del, remove but use it--pop()]\n")

# remove by value--remove()--a method
food = ['apple', 'beef', 'chicken', 'rice']
print(food)
food.remove('apple')
print(f"I don't like it, so now is {food}")

print("\nCan we reuse it after removing?")
dislike = food.remove('chicken')
print(f"I don't like {dislike}, so now is {food}")  # A none there
# A none there, too
print(f"I don't like {food.remove('rice')}, so now is {food}")
print("[Don't like pop method, we can't do this.Seems that just gonna be a None here.")
print("Mean that you can use pop() to give new value or use it directly in the strings\nBut you can't use remove() like that, althought they are both method.]")
print("[But the movement of removing from list both happened, just pop() can reuse and remove() can't]")

print("\nBut we can kind of reuse it by remove by defining it before")
print("Because we know the value of it, so we store it in a variable at the first")
outlook = ['hat', 'shoes', 'pants', 'glasses', 'skirt']
dislike = "glasses"
outlook.remove(dislike)
print(f"I don't like {dislike},so now my outlook is {outlook}")

print("\nThe last point:\nRemove by value only remove the first occurrence.\nRemove all, use loop")

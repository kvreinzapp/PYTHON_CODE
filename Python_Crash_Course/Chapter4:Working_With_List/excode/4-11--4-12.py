my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

my_foods.append('beef')
friend_foods.append('mutton')

print("My favorite foods are:")
for my in my_foods:
    print(f"-{my}")
print("My friend's favorite foods are:")
for friend in friend_foods:
    print(f"-{friend}")

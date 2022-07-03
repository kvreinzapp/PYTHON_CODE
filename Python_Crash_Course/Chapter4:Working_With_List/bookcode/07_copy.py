my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

print('\n')

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

# This doesn't work:
# Point to the same list
friend_foods = my_foods

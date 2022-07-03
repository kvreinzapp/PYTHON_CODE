#### how to write a `for` loop:
```
books=sth
for book in books:
```
==don't forget== the colon `:`

#### how to use `range()` function:
```
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)
```
##### use `range()` to make a list
```
numbers = list(range(1, 6))
print(numbers)      

even_numbers = list(range(2, 11, 2)) 
print(even_numbers)
```
###### how to create && list comprehension
```
squares = []
  for value in range(1, 11):
      square = value ** 2
      squares.append(square)
  print(squares)

squares = []
for value in range(1,11):
     squares.append(value**2)
print(squares)
```
A simpler way is ==list comprehension== :  
```
squares = [value**2 for value in range(1, 11)]
print(squares)
```

#### how to slice the list, use `sth[sth:sth]`
```
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
```
##### loop through it
```
for player in players[:3]:
    print(player.title())
```
##### copy it 
use `friend_foods = my_foods[:]`
instead of `friend_foods = my_foods`
###### copy using list comprehension:
```python
current_users = ['admin', 'klaus', 'leoNARDO', 'zack','Chain']
current_users_lower=[users.lower() for user in current_users ]
```
#### what about tuple
just like a list, but use ==parentheses==
```
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```
##### a tuple with only one element
`my_t=(3,)`
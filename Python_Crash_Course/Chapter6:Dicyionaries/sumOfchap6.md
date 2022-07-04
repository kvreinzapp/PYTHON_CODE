### Working with Dictionarays
#### Accessing values in dictionary -- `'sth:'sth'`
```python
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
```

##### Adding New Key-Value Pairs
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

##### Starting with an Empty Dictionary
```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```
##### Modifying Values in a Dictionary 
```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
```

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
v alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
```
##### Removing Key-Value Pairs -- `del`
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
```

#### A Dictionary of Similar Objects -- `{}`
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
```

##### Using get() to Access Values if no key is possible
###### key error
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
```
###### use `.get()` method to avoid *key error*
* The get() method requires a key as a first argument. 
* As a second optional argument, you can pass the value to be returned if the key doesn’t exist: 
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```

### Looping Through a Dictionary
#### Looping Through All Key-Value Pairs `.items()`
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
     print(f"\nKey: {key}")
     print(f"Value: {value}")
```
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
print(f"{name.title()}'s favorite language is {language.title()}.")
```
##### things about the method `.items()`
includes the name of the dictionary followed by the method items(), which returns a list of key­value pairs. 
The for loop then assigns each of these pairs to the two variables pro­vided.

#### Looping Through All the Keys in a Dictionary `.keys()`
##### using `keys()` method
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
print(name.title())
```
The line at there tells Python to pull all the keys from the dictionary `favorite_languages` and assign them one at a time to the variable `name`.
* Looping through the keys is actually the default behavior when looping through a dictionary,
*  so this code would have exactly the same output if you wrote `for name in favorite_languages:` rather than `for name in favorite_languages.keys():`, 
*  **You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.**
  
###### An example: access the value associated with any key you care about inside the loop by using the current key.:
```python
favorite_languages = {
    --snip--
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
``` 
###### Another example； You can also use the keys() method to find out if a particular person was polled. ：
```python
favorite_languages = {

    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',

    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
```
The keys() method isn’t just for looping: it actually **returns a list of all the keys, and the line at simply checks if 'erin' is in this list**

#### Looping Through a Dictionary’s Keys in a Particular Order -- using `sorted()`
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

#### Looping Through All Values in a Dictionary -- using `values()` method
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```
##### use `set()` to avoid repetive list
```python
favorite_languages = {
    --snip--
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

#### What is set
You can build a set directly using braces and separating the elements with commas:  `languages = {'python', 'ruby', 'python', 'c'}` 
* It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. 
* When you see braces but no key-value pairs, you’re probably looking at a set. 
* **Unlike lists and dictionaries, sets ==do not retain items in any specific order==.**
* you can also use `set` in this way: `set()`:
    ```python
    favorite_languages = {
        --snip--
        }
    print("The following languages have been mentioned:")
    for language in set(favorite_languages.values()):
        print(language.title())
    ```
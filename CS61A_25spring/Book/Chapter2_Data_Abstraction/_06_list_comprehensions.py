vowels = [x for x in "hello world" if x in 'aeiou']
print(vowels)

nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flated = [[x for x in sublist] for sublist in nested]
flat_list = [item for sublist in nested for item in sublist]
print(flated)
print(flat_list)

tuple = [(x, x**2, x**3) for x in range(1, 6)]
print(tuple)

words = ["madam", "apple", "racecar", "hello", "level"]
palindromes = [x for x in words if x == x[::-1]]
print(palindromes)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
commmon = [x for x in list1 if x in list2]
print(commmon)

d = {'a': 1, 'b': 2, 'c': 3}
l_from_d = [(key, value) for key, value in d.items()]
print(l_from_d)

matrix = [[i * j for i in range(0, 3)] for j in range(0, 3)]
print(matrix)

# Double
nums = [4, 8, 15, 16, 23, 42]
double_nums = [num * 2 for num in nums]
# Squares
nums = range(11)
squares = [num ** 2 for num in nums]
# Add Ten
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]
# Divide By Two
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num / 2 for num in nums] 
# Parity
'''
Create a new list named parity that contains a 1 or a 0 for each element of nums. For each element, if that element was even, the new list should contain a 0. If the element was odd, the new list should contain a 1.
'''
nums = [4, 8, 15, 16, 23, 42]
parity = [0 if num % 2 == 0 else 1 for num in nums]
# Add Hello
'''
Create a new list named greetings that adds "Hello, " in front of each name in the list names.
'''
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]
# First Character
'''
Create a new list named first_character that contains the first character from every name in the list names
'''
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
# Size
'''
Create a new list named lengths that contains the size of each name in the list of names
'''
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]
# Opposite
'''
Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
'''
booleans = [True, False, True]
opposite = [(not boolean) for boolean in booleans]
# Same String
'''
Create a new list called is_Jerry, in which an entry at position i is True if the entry in names at position i equals "Jerry". The entry should be False otherwise
'''
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [True if name == "Jerry" else False for name in names]
# Greater Than Two
'''
Create a new list called greater_than_two, in which an entry at position i is True if the entry in nums at position i is greater than 2.
'''
nums = [5, -10, 40, 20, 0]
greater_than_two = [num > 2 for num in nums]
# Product
'''
Create a new list named product that contains the product of each sub-list of nested_lists.
'''
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [num1 * num2 for (num1, num2) in nested_lists]
# Greater Than
'''
Create a new list named greater_than that contains True if the first number in the sub-list is greater than the second number in the sub-list, and False otherwise.
'''
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [True if num1 > num2 else False for (num1, num2) in nested_lists]
# First Only
'''
Create a new list named first_only that contains the first element in each sub-list of nested_lists.
'''
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [num1 for (num1, num2) in nested_lists]
# Add With Zip
'''
Use list comprehension and the zip function to create a new list named sums that sums corresponding items in lists a and b. For example, the first item in the new list should be 5 from adding 1 and 4 together.
'''
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [num1 + num2 for (num1, num2) in zip(a, b)]
# Divide With Zip
'''
Use list comprehension and the zip function to create a new list named quotients that divides the elements in list b by those in list a . For example, the second item in the new list should be 2.5 from dividing 5.0 by 2.0.
'''
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [num2 / num1 for (num1, num2) in zip(a, b)]
# Capitals
'''
You’ve been given two lists: a list of capitals and a list of countries. Create a new list named locations that contains the string "capital, country" for each item in the original lists. For example, if the 5th item in the capitals list is "Lima" and the 5th item in the countries list is "Peru", then the 5th item in the new list should be "Lima, Peru"
'''
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]
# Ages
'''
You’ve been given two lists: a list of names and a list of ages. Create a new list named users that contains the string "Name: name, Age: age" for each pair of elements in the original lists. For example, if the 5th item in the names list is "Aiyana" and the 5th item in ages is 42, then the 5th item in the new list should be "Name: Aiyana, Age: 42".
'''
names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]
users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names ,ages)]
# Greater Than With Zip
'''
Create a new list named greater_than that contains True or False depending on whether the corresponding item in list a is greater than the one in list b. For example, if the 2nd item in list a is 3, and the 2nd item in list b is 5, the 2nd item in the new list should be False.
'''
a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [True if itemA > itemB else False for (itemA, itemB) in zip(a, b)]
contains_a = lambda word: 'a' in word

# print(contains_a("banana"))
# print(contains_a("apple"))
# print(contains_a("cherry"))

long_string = lambda str: len(str) > 12

# print(long_string("short"))
# print(long_string("photosynthesis"))

ends_in_a = lambda str: str[-1] == 'a'

# print(ends_in_a("data"))
# print(ends_in_a("aardvark"))

double_or_zero = lambda num: num * 2 if num > 10 else 0

# print(double_or_zero(15))
# print(double_or_zero(5))

even_or_odd = lambda num: 'even' if num % 2 == 0 else 'odd'

print(even_or_odd(10))
print(even_or_odd(5))
# Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
    count = 0
    for _ in letters:
        if _ in word:
            count += 1
    return count

print(unique_english_letters("mississippi"))        # should print 4
print(unique_english_letters("Apple"))              # should print 4

# Count X
def count_char_x(word, x):
    return word.count(x)

print(count_char_x("mississippi", "s"))             # should print 4
print(count_char_x("mississippi", "m"))             # should print 1

# Count Multi X
def count_multi_char_x(word, x):
    return word.count(x)

print(count_multi_char_x("mississippi", "iss"))     # should print 2
print(count_multi_char_x("apple", "pp"))            # should print 1

# Substring Between
def substring_between_letters(word, start, end):
    index_start = word.find(start)
    index_end = word.find(end)
    if index_start == -1 or index_end == -1:
        return word
    else:
        return word[index_start + 1:index_end]

print(substring_between_letters("apple", "p", "e")) # should print "pl"
print(substring_between_letters("apple", "p", "c")) # should print "apple"

# X Length
def x_length_words(sentence, x):
    sentence_list = sentence.split(" ")
    for word in sentence_list:
        if len(word) < x:
            return False
        else:
            return True

print(x_length_words("i like apples", 2))           # should print False
print(x_length_words("he likes apples", 2))         # should print True

# Check Name
def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    else:
        return False

print(check_for_name("My name is Jamie", "Jamie"))  # should print True
print(check_for_name("My name is jamie", "Jamie"))  # should print True
print(check_for_name("My name is Samantha", "Jamie"))   # should print False

# Every Other Letter
def every_other_letter(word):
    return word[::2]

print(every_other_letter("Codecademy"))         # should print Cdcdm
print(every_other_letter("Hello world!"))       # should print Hlowrd
print(every_other_letter(""))                   # should print 

# Reverse
def reverse_string(word):
    return word[::-1]

print(reverse_string("Codecademy"))             # should print ymedacedoC
print(reverse_string("Hello world!"))           # should print !dlrow olleH
print(reverse_string(""))                       # should print

# Make Spoonerism
def make_spoonerism(word1, word2):
    if len(word1) == 1 and len(word2) == 1:
        return word2 + " " + word1
    else:
        return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

print(make_spoonerism("Codecademy", "Learn"))   # should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))       # should print wello Horld!
print(make_spoonerism("a", "b"))                # should print b a

# Add Exclamation
def add_exclamation(word):
    return word.ljust(20, "!")

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
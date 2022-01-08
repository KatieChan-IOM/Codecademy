def get_length(word):
    counter = 0
    for _ in word:
        counter += 1
    return counter

def letter_check(word, letter):
    is_found = False
    word_index = None
    for i in word:
        if i == letter:
            is_found = True                 # set the flag to true
            word_index = word.index(i)      # get the index of the letter
            print(word_index)
    return is_found

def contains(big_string, little_string):
    is_found = False
    for _ in big_string:
        if little_string in big_string:
            is_found = True
    return is_found

def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if letter in string_two and not (letter in common):
            common.append(letter)
    return common
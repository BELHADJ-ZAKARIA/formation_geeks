"""
Challenge

Ask a user for a word.
Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
Make sure the letters are the keys.
Make sure the letters are strings.
Make sure the indexes are stored in a list, and those lists are values.

Examples
“dodo” ➞ { “d”: [0, 2], “o”: [1, 3] }
“froggy” ➞ { “f”: [0], “r”: [1], “o”: [2], “g”: [3, 4], “y”: [5] }
“grapes” ➞ { “g”: [0], “r”: [1], “a”: [2], “p”: [3] }
"""

def create_index_dict(word):
    letter_indexes = {}
    for index, letter in enumerate(word):
        if letter in letter_indexes:
            letter_indexes[letter].append(index)
        else:
            letter_indexes[letter] = [index]
    return letter_indexes


user_word = input("Enter a word: ")

result_dict = create_index_dict(user_word)

print(result_dict)
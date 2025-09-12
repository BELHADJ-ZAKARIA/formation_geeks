"""
Exercise 1 : Outputs

Predict the output of the following code snippets:
"""
"""
3 <= 3 < 9                        >>> TRUE

3 == 3 == 3                       >>> TRUE

bool(0)                           >>> FALSE

bool(5 == "5")                    >>> FALSE

bool(4 == 4) == bool("4" == "4")  >>> TRUE

bool(bool(None))                  >>> FALSE

x = (1 == True)                   >>> TRUE
y = (1 == False)                  >>> FALSE
a = True + 4                      >>> 5
b = False + 10                    >>> 10

print("x is", x)                  >>> x is True
print("y is", y)                  >>> y is False
print("a:", a)                    >>> a: 5
print("b:", b)                    >>> b: 10
"""

"""
Exercise 2 : Longest word without a specific character

Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
"""

import string

sentence = []
count = 0
score = 0

print("Longest word without a specific character")
print("Entre \"x\" for quit this challenge\n")

while (True):
  sentence = input("Enter the longest sentence you can without usnig the character \"A\" : ")
  
  if "A" in sentence.upper():
    print("Attention! there's in A character on your sentence.\n")
    continue

  if sentence.upper() == "X": break

  cleaned_list = list(filter(str.strip, sentence))

  for i in cleaned_list:
    for char in i:
      if char in string.punctuation:
        cleaned_list.remove(i)
  
  for i in cleaned_list:
    count += 1
    
  if count > score:
      score = count
      print("Congratulations you have NEW SCORE!\n")
  else:
    print("Try Again\n")

  count = 0


"""
Exercise 3: Working on a paragraph

Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
Paste it to your code, and store it in a variable.
Let’s analyze the paragraph. Print out a nicely formatted message saying:
* How many characters it contains (this one is easy…).
* How many sentences it contains.
* How many words it contains.
* How many unique words it contains.

Bonus: How many non-whitespace characters it contains.
Bonus: The average amount of words per sentence in the paragraph.
Bonus: the amount of non-unique words in the paragraph.
"""
"""
paragraph : 
"Variables are places where we can keep information for a short time. 
A variable is like a small box where we can put any kind of information (text, numbers...).
Every variable has two parts: a name and a value. The value can be any type of information. 
We can use what's inside our box to do things with the stored information."
"""

import string
import math

paragraph = "Variables are places where we can keep information for a short time. A variable is like a small box where we can put any kind of information (text, numbers...). Every variable has two parts: a name and a value. The value can be any type of information. We can use what's inside our box to do things with the stored information."

sentence = []
num_word_in_sentence = []
count = 0

list_of_non_whitespace = []
nwspace_count = 0

flag = 0
word_count = 0

words = []
words_capitalize = []
word = ""

list_unique_words = []
unique_words = 0

list_non_unique_words = []
non_unique_words = 0


print(f"Number of characters : {len(paragraph)}\n")

for i in range(0, len(paragraph)-1):
  if paragraph[i] in string.punctuation:
    nwspace_count += 1
    list_of_non_whitespace.append(paragraph[i])
    if paragraph[i+1] != "." and paragraph[i+1] != ")":
      if paragraph[i] == ".":
        count += 1
        sentence.append(paragraph[flag:i])
        flag = i

print(f"Number of sentences in the paragraph : {count}\n")

new_sentence = [i.strip(" .")for i in sentence]
#print(f"The sentences in paragraph : {new_sentence}")


for i in range(0, len(paragraph)-1):
  if paragraph[i] != " " and paragraph[i] not in string.punctuation:
    word += paragraph[i]
  elif paragraph[i] == " ":
    words.append(word)
    word = ""

print(f"Number of words in the paragraph : {len(words)}\n")
#print(f"The words in paragraph : {words}")

words_capitalize = [i.capitalize() for i in words]

for i in words_capitalize:
  if words_capitalize.count(i) == 1:
    unique_words += 1
    list_unique_words.append(i)
  else:
    list_non_unique_words.append(i)


print(f"Number of unique words in the paragraph : {unique_words}")
print(f"List of unique words in the paragraph : {list_unique_words}\n")

print(f"Number of non-whitespace characters in the paragraph : {nwspace_count}")
print(f"List of non whitespace characters in the paragraph : {list_of_non_whitespace}\n")

for i in range(0, len(new_sentence)):
  word_count = 1
  for j in new_sentence[i]:
    if j == " " or j == "\n":
      word_count += 1
  num_word_in_sentence.append(word_count)

print(f"The average amount of words per sentence in the paragraph : {round(sum(num_word_in_sentence)/len(num_word_in_sentence))}")
print(f"Number of words per sentence {num_word_in_sentence}\n")

print(f"The amount of non-unique words in the paragraph : {len(set(list_non_unique_words))}")
print(set(list_non_unique_words))
"""
Challenge 1

Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
"""

list_of_num = []

num = int(input("Entre a number : "))
lenght = int(input("Enter a lenght of list :"))

for i in range(0, lenght):
  list_of_num.append(num*(i+1))

print(list_of_num)


"""
Challenge 2

Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
"""

new_word = []
count = 0
show_word = ""

word = input("Enter the word : ")

for i in range(0, len(word)):
 count = word.count(word[i])
 if i != (len(word)-1):
  if count > 1 and word[i] != word[i+1] :
    new_word.append(word[i])
  elif count == 1:
    new_word.append(word[i])
 elif i == (len(word)-1):
  if count > 1 and word[i-1] == word[i] :
    new_word.append(word[i])
  elif count == 1:
    new_word.append(word[i])

for i in new_word:
  show_word += i

print(f"\n{show_word}")
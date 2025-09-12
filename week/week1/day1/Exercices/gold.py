"""
Exercise 1: What is the Season?

Ask the user to input a month (1 to 12).
Display the season of the month received:

Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
"""

month = int(input("Enter the month : "))

if (month >= 3 and month <= 5):
  print('the Season is Spring')
elif (month >= 6 and month <= 8):
  print('the Season is Summer')
elif (month >= 9 and month <= 11):
  print('the Season is Autumn')
else:
  print('the Season is Winter')

"""
Exercise 2: For Loop

Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20 (inclusive), print out every element which has an even index.
"""

for i in range(1, 21):
  print(i)

for i in range(1, 21):
  if i%2 != 0: 
    print(i)

"""
Exercise 3: While Loop

Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
"""

while ((input("What's your name = ")).upper() != "ZAKARIA"):
  continue

"""
Exercise 4: Check the index

Using this variable:
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.
Example: if input is Cortana we should be printing the index 1
"""

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("What's your name : ")

if name.capitalize() in names:
  print(f"the index of your name is {names.index(name.capitalize())}")

"""
Exercise 5: Greatest Number

Ask the user for 3 numbers and print the greatest number.
"""

numbers = []
txt = ["st", "nd", "rd"]
i = 0

while  (i != 3):
  numbers.append(int(input(f"Input the {i+1}{txt[i]} number : ")))
  i += 1

print(f"\nThe greatest number is: {max(numbers)}")

"""
Exercise 6: Random number

Ask the user to input a number from 1 to 9 (including).
Get a random number between 1 and 9. Hint: random module.
If the user guesses the correct number print a message that says “Winner”.
If the user guesses the wrong number print a message that says “Better luck next time.”

Bonus: use a loop that allows the user to keep guessing until they want to quit.
Bonus 2: on exiting the loop, tally up and display total games won and lost.
"""

import random

random_number = random.randint(1, 9)
win = 0
lost = 0

while True:
  guess = input("Guess the number : ")
  
  if guess.isdigit():
      if int(guess) == random_number:
        print("Winner\n")
        win += 1
        random_number = random.randint(1, 9)
      elif int(guess) != random_number:
        print("Better luck next time.\n")
        lost += 1
  else:
    if guess.lower() == "quit":
      break

print(f"\nTotal games you won : {win}")
print(f"Total games you lost: {lost}\n")
"""
Exercise 1: Birthday Look-up

Create a variable called birthdays. Its value should be a dictionary.
Initialize this variable with the birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip: Use the format "YYYY/MM/DD".
Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”
Ask the user to give you a person's name and store the answer in a variable.
Get the birthday of the name provided by the user.
Print out the birthday with a nicely-formatted message.
"""

birthdays = {
    "Khalid":"1992/06/12",
    "Amine":"1998/12/05",
    "Mostafa":"2003/05/11",
    "Mohammed":"2000/11/26",
    "Ismail":"1990/07/10"
}

print("Welcome! We’re glad to have you here.\nYou can look up the birthdays of the people in the list!\n")

name = input("Enter the name of person you want to look there birthday : ")

if name.capitalize() in birthdays.keys():
  print(f"\nDate of Birth: {birthdays.get(name.capitalize())}\n")
  print("We wish him happiness, health and success on his special day!\n")



"""
Exercise 2: Birthdays Advanced

Before asking the user to input a person's name, print out all of the names in the dictionary.
If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for person's name”).
"""
birthdays = {
    "Khalid":"1992/06/12",
    "Amine":"1998/12/05",
    "Mostafa":"2003/05/11",
    "Mohammed":"2000/11/26",
    "Ismail":"1990/07/10"
}

print("Welcome! We’re glad to have you here.\nYou can look up the birthdays of the people in the list!\n")

print("the names in the Birthdays dictionary : \n")

for key in birthdays.keys():
  print(key)

name = input("\nEnter the name of person you want to look there birthday : ")

error_message = "\nSorry, we don’t have the birthday information for person's name"

if birthdays.get(name.capitalize(), error_message) != error_message:
  print(f"\nDate of Birth: {birthdays.get(name.capitalize())}\n")
  print("We wish him happiness, health and success on his special day!\n")
else: 
  print(birthdays.get(name.capitalize(), error_message))



"""
Exercise 3: Sum

Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.

Example:
If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

Hint: Treating our number as an int or a str at different points in our code may be helpful.
"""

def function(num):
  num_list = []
  string = ''
  sum = 0

  for i in range(1, 5):
    num_list.append(str(num)*i)

  for i in range(0, len(num_list)):
    sum += int(num_list[i])
    if i != 0:
      string = string + ' + ' + num_list[i]
    else:
      string = string + num_list[i] 

  print(f"{sum} ({string})")

function(3)


"""
Exercise 4: Double Dice

1. Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.

2. Create a function called throw_until_doubles.
It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, i.e., until we reach doubles.
For example: (1, 2), (3, 1), (5, 5) → then stop throwing, because doubles were reached.
This function should return the number of times it threw the dice in total. In the example above, it should return 3.

3. Create a main function. It should throw doubles 100 times (i.e., call your throw_until_doubles function 100 times), 
and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. 
(What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).
4. After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
5. Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.

For example:

If the results of the throws were as follows (your code would do 100 doubles, not just 3):

(1, 2), (3, 1), (5, 5)
(3, 3)
(2, 4), (1, 2), (3, 4), (2, 2)

Then my output would show something like this:

Total throws: 8
Average throws to reach doubles: 2.67.
"""

import random

def throw_dice():
  return random.randint(1, 6)

def throw_until_doubles():
  list1 = []
  list2 = []
  
  count = 0

  while(True):
    dice1 = throw_dice()
    dice2 = throw_dice()

    count += 1

    list1.append(dice1)
    list2.append(dice2)

    if dice1 == dice2:
      #print(f"Results : {list(zip(list1, list2))}") #if you want to see the result of throwing dice remove #
      break
  
  return count

print(f"the number of times we threw the dice until we have double :{throw_until_doubles()}\n")

def main():
  list3 = []
  for i in range(0, 100):
    list3.append(throw_until_doubles())
  
  print(f"Total throws: {sum(list3)}\n")
  print(f"Average throws to reach doubles: {round(sum(list3)/100, 2)}.")

main()



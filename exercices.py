""" 
Exercise 1 : Hello World

Print the following output in one line of code:
"""

print("Hello World\n" * 4)

"""
Exercise 2 : Some Math

Write code to calculate the result of (99³) × 8 (i.e., 99 raised to the power of 3, then multiplied by 8).
"""

print((99**3)*8)

"""
Exercise 3 : What’s your name ?

Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
"""

name = input("What is your name : ")

if name.upper() == "ZAKARIA":
    print("\nWhoa! We have the same name. Looks like destiny wants us to start a secret club!")

elif name.upper() != "ZAKARIA":
    print(f"\nNice to meet you, {name}! Our names may differ, but I promise I won’t hold it against you")

"""
Exercise 4 : Tall enough to ride a roller coaster

Write code that will ask the user for their height in centimeters.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride.
"""

height = int(input("What is your height in cm : "))

if height > 145:
    print("\nYou are tall enough to ride.")
elif height < 145:
    print("\nYou need to grow some more to ride.")

"""
Exercise 5 : Favorite Numbers

Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
"""

my_fav_numbers = {1, 2, 3, 4}

my_fav_numbers.add(0)
my_fav_numbers.add(5)

my_fav_numbers.remove(5)

friend_fav_numbers = {11, 12, 13}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

"""
Exercise 6: Tuple Given a tuple which value is integers, is it possible to add more integers to the tuple?
"""
"""
Answear:

No, you cannot directly add more integers to a tuple because tuples in Python are immutable.

If we want to add more integers, we create a new tuple by concatenation.
"""


"""
Exercise 7: List

Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"]:italicized text
Remove Banana from the list.
Remove Blueberries from the list.
Add Kiwi to the end of the list.
Add Apples to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.append("Apples")

count = 0
for i in range(0, len(basket)):
    if basket[i] == "Apples":
        count += 1

print(f"they are {count} \"Apples\" in the list")

basket.clear()

print(basket)
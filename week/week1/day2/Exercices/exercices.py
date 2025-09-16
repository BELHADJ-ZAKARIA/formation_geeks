"""
Exercise 1 : Convert lists into dictionaries

Convert the two following lists, into dictionaries.
Hint: Use the zip method
"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = {}

for key, value in zip(keys, values):
  new_dict[key] = value


"""
 Exercise 2 : Cinemax #2

A movie theater charges different ticket prices depending on a person’s age.

if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

How much does each family member have to pay ?
Print out the family’s total cost for the movies.

Bonus: Ask the user to input the names and ages instead of using the provided family variable 
(Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
"""

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

sum = 0

for key, value in family.items():
  if value < 3:
    print(f"{key.capitalize()}, You get a free ticket!\n")
  elif (3 <= value and value <= 12):
    print(f"{key.capitalize()}, You should pay 10$ for ticket.\n")
    sum += 10
  elif value > 12:
    print(f"{key.capitalize()}, You should pay 15$ for ticket.\n")
    sum += 15
    
print(f"The family’s total cost for the movies is : {sum}$\n")


"""
BONUS
"""

new_family = {}
add = ""
sum = 0

print("\nEnter the names and ages of you family\n")

while (add.upper() != 'N'):
  name = input("Enter the Name : ")
  age = int(input("\nEnter the Age :"))
  new_family[name] = age
  add = input("\nDo you want to add more family members? (Press \"Y\" for Yes or \"N\" for No) :")

print(f"\nFamily = {new_family}\n")

for key, value in new_family.items():
  if value < 3:
    print(f"{key.capitalize()}, You get a free ticket!\n")
  elif (3 <= value and value <= 12):
    print(f"{key.capitalize()}, You should pay 10$ for ticket.\n")
    sum += 10
  elif value > 12:
    print(f"{key.capitalize()}, You should pay 15$ for ticket.\n")
    sum += 15
    
print(f"The family’s total cost for the movies is : {sum}$\n")


"""
Exercise 3: Zara

Here is some information about a brand :

name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green

1. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
2. Change the number of stores to 2.
3. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
4. Add a key called country_creation with a value of Spain.
5. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
6. Delete the information about the date of creation.
7. Print the last international competitor.
8. Print the major clothes colors in the US.
9. Print the amount of key value pairs (ie. length of the dictionary).
10. Print the keys of the dictionary.
11. Create another dictionary called more_on_zara with the following details:
- creation_date: 1975
- number_stores: 10 000
12. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
13. Print the value of the key number_stores. What just happened ?
"""

brand = {
    'name' : 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000, 
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2

print(f"the clients of Zara are : {brand['type_of_clothes']}\n")

if 'international_competitors' in brand:
  brand['international_competitors'].append('Desigual')
  print(brand['international_competitors'])

del brand['creation_date']

print(f"\nThe last international competitor is : {brand['international_competitors'][-1]}\n")

print(f"The major clothes colors in the US are : {brand.get('major_color', {}).get('US', 'None')}\n")

print(f"The amount of key value pairs is : {len(brand)}\n")

print(f"The keys of the dictionary are : {list(brand.keys())}\n")

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print(f"The value of the number_stores in brand dict : {brand['number_stores']}\n")

# What just happened ?
# We have updated the number of stores (by taking the value of number_store from more_on_zara to change number_store in brand).


"""
Exercise 4 : Some Geography

Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as “city is in country”.
(For example Reykjavik is in Iceland)
Give the country parameter a default value.
Call your function.
"""

def describe_city(city_name='Mohammedia', country_name='Morocco'):
  print(f"{city_name} is in {country_name}")

describe_city('Reykjavik', 'Iceland')


"""
Exercise 5 : Random

Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
Compare the two numbers, if it's the same number, display a success message, otherwise show a fail message and display both numbers.
"""
import random

def random_number(num):
  if 1 <= num <= 100:
    rand_num = random.randint(1, 100)
    if num == rand_num:
      print("We have the same number!")
    else :
      print(f"fail message! number : {num}, genarated number : {rand_num}\n")
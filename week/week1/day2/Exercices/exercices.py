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


"""
Exercise 6 : Let’s create some personalized shirts !

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it, such as “The size of the shirt is size and the text is text“
Call the function make_shirt().
Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
Call the function, in order to make a large shirt with the default message
Make medium shirt with the default message
Make a shirt of any size with a different message.

Bonus: Call the function make_shirt() using keyword arguments.
"""
def make_shirt(size, txt):
  print(f"The size of the shirt is {size} and the text is {txt}.\n")


make_shirt("S", "Focus on your weight")

def make_shirt(size= "L", txt= "I love Python"):
  print(f"The size of the shirt is {size} and the text is {txt}.\n")

make_shirt()

make_shirt("M")

make_shirt(txt="Good Morning")

"""
Bonus: Call the function make_shirt() using keyword arguments.
"""
def make_shirt(*args):
  print(f"The size of the shirt is {args[0]} and the text is {args[1]}.\n")

make_shirt('M', 'This is my lovely size')


"""
Exercise 7 : Temperature Advice

Instructions : 

> Create a function called get_random_temp().
  1. This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
  2. Test your function to make sure it generates expected results.

> Create a function called main().
  1. Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
  2. Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

> Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
  1. below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
  2. between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
  3. between 16 and 23
  4. between 24 and 32
  5. between 32 and 40

> Change the get_random_temp() function:
  1. Add a parameter to the function, named ‘season’.
  2. Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
  3. Now that we’ve changed get_random_temp(), let’s change the main() function:
     3.1. Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
     3.2. Use the season as an argument when calling get_random_temp().

Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
"""

import random

def get_random_temp():
  return random.randint(-10, 40)

print(f"Test get_random_temp() function : {get_random_temp()}\n")

def main():
  temperature = get_random_temp()
  print(f"The temperature right now is {temperature} degrees Celsius.\n")

  if temperature < 0:
    print("Brrr, that’s freezing! Wear some extra layers today\n")
  elif 0 <= temperature < 16:
    print("Quite chilly! Don’t forget your coat\n")
  elif 16 <= temperature <= 23:
    print("Nice and mild. Light layers are perfect, maybe a sweater for the evening.\n")
  elif 24 <= temperature < 32:
    print("Warm to hot. Stay hydrated, use sunscreen, and take breaks in the shade.\n")
  elif 32 <= temperature <= 40:
    print("Go easy during peak sun, drink plenty of water, wear breathable clothes, and check on elders/kids.\n")

main()

def get_random_temp(season):
  SEASON_TEMP = {
    "winter": (-10, 16),
    "spring": (5, 24),
    "summer": (17, 40),
    "autumn": (5, 23)
    }

  season_limits = SEASON_TEMP.get(season.lower(), "None")

  return random.randint(season_limits[0], season_limits[1])


def main():
  user_season = input("Enter a season - ‘summer’, ‘autumn’, ‘winter’ or ‘spring’ : ")
  temperature = get_random_temp(user_season)
  print(f"\nThe temperature right now is {temperature} degrees Celsius.\n")

  if temperature < 0:
    print("Brrr, that’s freezing! Wear some extra layers today\n")
  elif 0 <= temperature < 16:
    print("Quite chilly! Don’t forget your coat\n")
  elif 16 <= temperature <= 23:
    print("Nice and mild. Light layers are perfect, maybe a sweater for the evening.\n")
  elif 24 <= temperature < 32:
    print("Warm to hot. Stay hydrated, use sunscreen, and take breaks in the shade.\n")
  elif 32 <= temperature <= 40:
    print("Go easy during peak sun, drink plenty of water, wear breathable clothes, and check on elders/kids.\n")

main()


"""
Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
"""

def get_random_temp(month_number):
  SEASON_TEMP = {
    "winter": [[12, 1, 2], (-10, 16)],
    "spring": [[3, 4, 5],(5, 24)],
    "summer": [[6, 7, 8],(17, 40)],
    "autumn": [[9, 10, 11], (5, 23)]
    }

  for key, value in SEASON_TEMP.items():
    if month_number in value[0]:
      season = key

  season_limits = SEASON_TEMP.get(season, "None")

  return round(random.uniform(float(season_limits[1][0]), float(season_limits[1][1])), 2)

def main():
  month_number = int(input("Enter the number of the month (1 = January, 12 = December) : "))
  temperature = get_random_temp(month_number)
  print(f"\nThe temperature right now is {temperature} degrees Celsius.\n")

  if temperature < 0:
    print("Brrr, that’s freezing! Wear some extra layers today\n")
  elif 0 <= temperature < 16:
    print("Quite chilly! Don’t forget your coat\n")
  elif 16 <= temperature <= 23:
    print("Nice and mild. Light layers are perfect, maybe a sweater for the evening.\n")
  elif 24 <= temperature < 32:
    print("Warm to hot. Stay hydrated, use sunscreen, and take breaks in the shade.\n")
  elif 32 <= temperature <= 40:
    print("Go easy during peak sun, drink plenty of water, wear breathable clothes, and check on elders/kids.\n")

main()


"""
Exercise 8 : Star Wars Quiz

Instructions

This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

Here is an array of dictionaries, containing those questions and answers:

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

1. Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
2. Create a function that informs the user of his number of correct/incorrect answers.

3. Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
If he had more then 3 wrong answers, ask him to play again.
"""
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask():
  wrong_answers = []
  
  num_correct = 0
  num_incorrect = 0

  for i  in range(0, len(data)):
    for key, value in data[i].items():
      if key == "question":
        answer = input(f"{value} ")
      else:
        if answer.lower() == value.lower():
          print("Correct!\n")
          num_correct +=1
        else:
          print("Wrong answer!\n")
          wrong_answers.append(answer)
          num_incorrect +=1
    
  print(f"The number of correct answer : {num_correct}\n")
  print(f"The number of incorrect answer : {num_incorrect}\n")
  print(f"List of wrong answers : {wrong_answers}\n")

ask()

def ask():
  wrong_answers = []
  
  num_correct = 0
  num_incorrect = 0

  for i  in range(0, len(data)):
    for key, value in data[i].items():
      if key == "question":
        answer = input(f"{value} ")
      else:
        if answer.lower() == value.lower():
          print("Correct!\n")
          num_correct +=1
        else:
          print("Wrong answer!\n")
          wrong_answers.append(answer)
          num_incorrect +=1

  return num_correct, num_incorrect, wrong_answers
    
def inform_user(answer):
  print(f"The number of correct answer : {answer[0]}\n")
  print(f"The number of incorrect answer : {answer[1]}\n")
  print(f"List of wrong answers : {answer[2]}\n")

quiz = ask()

inform_user(quiz)

"""
3. Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
If he had more then 3 wrong answers, ask him to play again.
"""

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask():
  question_wrong_answer = []
  wrong_answers = []
  correct_answers = []
  
  num_correct = 0
  num_incorrect = 0

  for i  in range(0, len(data)):
    for key, value in data[i].items():
      if key == "question":
        answer = input(f"{value} ")
      else:
        if answer.lower() == value.lower():
          print("Correct!\n")
          num_correct +=1
        elif answer.lower() != value.lower():
          print("Wrong answer!\n")
          question_wrong_answer.append(data[i]["question"])
          correct_answers.append(data[i]["answer"])
          wrong_answers.append(answer)
          num_incorrect +=1

  return num_correct, num_incorrect, wrong_answers, question_wrong_answer, correct_answers
    
def inform_user(answer):
  print(f"\nThe number of correct answer : {answer[0]}")
  print(f"The number of incorrect answer : {answer[1]}")
  if len(answer[2]) > 1:
    print(f"List of wrong answers : {answer[2]}\n")
    print(f"The questions you answered wrong : \n")
    for i in range(0, len(answer[2])):
      print(f"The question : {answer[3][i]}")
      print(f"Your answer : {answer[2][i]}")
      print(f"The correct answer : {answer[4][i]}\n")

# Main game loop
while True:
    game_results = ask()
    inform_user(game_results)

    if game_results[1] > 3:
        decision = input("You had more than 3 wrong answers. Do you want to play again? \"Y\" or \"N\"\n")
        if decision.upper() != "Y":
            break
    else:
        break
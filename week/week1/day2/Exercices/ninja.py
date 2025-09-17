"""
Exercise 1: Cars

Copy the following string into your code: Volkswagen, Toyota, Ford Motor, Honda, Chevrolet.
Convert it into a list using Python (don’t do it by hand!).
Print out a message saying how many manufacturers/companies are in the list.
Print the list of manufacturers in reverse/descending order (Z-A).
Using loops or list comprehension:
Find out how many manufacturers’ names have the letter o in them.
Find out how many manufacturers’ names do not have the letter i in them.

Bonus:
There are a few duplicates in this list: ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
Remove these programmatically. (Hint: you can use a set to help you).
Print out the companies without duplicates, in a comma-separated string with no line-breaks (e.g., “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

Bonus:
Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
"""

string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
count_o = 0
count = 0
string1 = ""

list1 = string.split(',')
companies = [item.strip() for item in list1]

print(f"The number of companies in list : {len(companies)}\n")

reversed_list = sorted(companies, reverse=True)

print(f"\nThe list of manufacturers in reverse/descending order (Z-A) : {reversed_list}\n")


for item in reversed_list:
  if 'o' in item.lower():
    count_o += 1 

print(f"The number of manufacturers names have the letter 'o' in them : {count_o}\n")

for item in reversed_list:
  if 'i' not in item.lower():
    count += 1 

print(f"The number of manufacturers names do not have the letter i in them : {count}\n")

#Bonus 1
list1 = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

unique_list = list(set(list1))

for i in range(0, len(unique_list)):
  if i != (len(unique_list)-1):
    string1 = string1 + unique_list[i] + ", "
  else:
    string1 = string1 + unique_list[i]

print(string1)

print(f"\nThe companies without duplicates, in a comma-separated string with no line-breaks : {string1} \n")
print(f"The number of companies are now in the list : {len(unique_list)}\n")

#Bonus 2
list2 = sorted(unique_list)
list3 = []
string3 = ""

for i in range(0, len(list2)):
  for j in range(1, len(list2[i])+1):
    string3 += list2[i][-j]
    if j == len(list2[i]):
      list3.append(string3)
      string3 = ""

print(list2)
print(list3)


"""
Exercise 2: What’s your name?

Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name, 3: last_name.
middle_name should be optional; if it’s omitted by the user, the name returned should only contain the first and the last name.

For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return “John Hooker Lee”.
But get_full_name(first_name="bruce", last_name="lee") will return “Bruce Lee”.
"""

def get_full_name(first_name, last_name, middle_name=None):
  if middle_name:
    return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
  else:
    return f"{first_name.title()} {last_name.title()}"

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))


"""
Exercise 3: From English to Morse

Write a function that converts English text to Morse code and another one that does the opposite.
Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
"""

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

txt = "Write a function that converts English text to Morse code and another one that does the opposite . Hint : Check the internet for a translation table , every letter is separated with a space and every word is separated with a slash / ."

def convert_to_morse(txt):
  list_words = txt.split()
  list_morse_words = []

  word = ""
  txt_morse = ""
  count = 0

  for item in list_words:
    for i in item.upper():
      count += 1
      if (len(item.upper())-count) != 0:
        word = word + morse_code_dict.get(i) + " "
      elif (len(item.upper())-count) == 0:
        word = word + morse_code_dict.get(i)
        list_morse_words.append(word)
        word = ""
        count = 0

  for i in range(0, len(list_morse_words)):
    if i != (len(list_morse_words)-1):
      txt_morse = txt_morse + list_morse_words[i] + " / "
    elif i == (len(list_morse_words)-1):
      txt_morse = txt_morse + list_morse_words[i]
  
  return txt_morse

print(f"{txt}\n")
print(f"{convert_to_morse(txt)}\n")

morse_code_dict_reversed = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@'
}

txt_morse = convert_to_morse(txt)

def convert_from_morse(txt_morse):
  list_morse_words = txt_morse.split(" / ")
  list_words = []

  word = ""
  txt = ""
  count = 0

  for item in list_morse_words:
    code_of_alpha = item.split(" ")
    for i in code_of_alpha:
      count += 1
      if (len(code_of_alpha)-count) != 0:
        word = word + morse_code_dict_reversed.get(i) 
      elif (len(code_of_alpha)-count) == 0:
        word = word + morse_code_dict_reversed.get(i) + " "
        list_words.append(word)
        word = ""
        count = 0

  for i in range(0, len(list_words)):
    if i != (len(list_words)-1):
      txt = txt + list_words[i] 
    elif i == (len(list_morse_words)-1):
      txt = txt + list_words[i]
  
  return txt.capitalize()

print(f"{convert_from_morse(txt_morse)} \n")
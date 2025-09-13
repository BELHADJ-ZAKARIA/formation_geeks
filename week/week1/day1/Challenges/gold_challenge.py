"""
Happy birthday

Instructions

Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake as seen below:

       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~



The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

Bonus : If they were born on a leap year, display two cakes !
"""


import datetime

birthdate = input("Enter your birth date with the excact format! *(DD/MM/YYYY)* : ")

year_of_birthdate = birthdate[-4:]

today = datetime.datetime.now()

age = str(today.year - int(year_of_birthdate))

print(f"\nAge = {age}")
print(f"The number of candles on the cake : {age[-1]} \n")

fix_txt = "\b"*int(int(age[-1])/2)

if (int(year_of_birthdate) % 4 == 0 and int(year_of_birthdate) % 100 == 0 and int(year_of_birthdate) % 400 == 0) or (int(year_of_birthdate) % 4 == 0 and int(year_of_birthdate) % 100 != 0):
  print("You were born in a leap year, so we’ve got a surprise for you!\n")
  for i in range(0, 2):
    print("      ______"+fix_txt+"i"*int(age[-1])+"______"+fix_txt)
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~\n\n")
else:
  print("      ______"+fix_txt+"i"*int(age[-1])+"______"+fix_txt)
  print("      |:H:a:p:p:y:|")
  print("    __|___________|__")
  print("   |^^^^^^^^^^^^^^^^^|")
  print("   |:B:i:r:t:h:d:a:y:|")
  print("   |                 |")
  print("   ~~~~~~~~~~~~~~~~~~~\n")
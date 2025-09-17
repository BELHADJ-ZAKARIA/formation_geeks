"""
Exercise 1: Cats

Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

1. Instantiate three Cat objects using the code provided above.
2. Outside of the class, create a function that finds the oldest cat and returns the cat.
3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# 1. Instantiate three Cat objects using the code provided above.
cat1 = Cat("micho", 3)
cat2 = Cat("lion", 7)
cat3 = Cat("jungo", 9)

# 2. Outside of the class, create a function that finds the oldest cat and returns the cat.

def oldest_cat(cats):
  oldest_cat = cats[0]  # Initialize with the first cat object

  for cat in cats:
    if oldest_cat.age < cat.age:
       oldest_cat = cat

  return oldest_cat

# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
cats = [cat1, cat2, cat3]
old_cat = oldest_cat(cats)
print(f"The oldest cat is {old_cat.name}, and is {old_cat.age} years old.")


"""
Exercise 2 : Dogs

Instructions
Create a class called Dog.
In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
Create a method called bark that prints the following string “<dog_name> goes woof!”.
Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
Print the details of his dog (ie. name and height) and call the methods bark and jump.
Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
Print the details of her dog (ie. name and height) and call the methods bark and jump.
Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
"""

class Dog:
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def bark(self):
    return f"{self.name} goes woof!"

  def jump(self):
    return f"{self.name} jumps {self.height * 2} cm high!"

davids_dog = Dog("Rex", 50)

print(f"\nThe name of Dog : {davids_dog.name}")
print(f"The height of Dog : {davids_dog.height}")
print(davids_dog.bark())
print(davids_dog.jump())

sarahs_dog = Dog("Teacup", 20)

print(f"\nThe name of Dog : {sarahs_dog.name}")
print(f"The height of Dog : {sarahs_dog.height}")
print(sarahs_dog.bark())
print(sarahs_dog.jump())

if davids_dog.height > sarahs_dog.height:
  print(f"\n{davids_dog.name}")
else:
  print(f"\n{sarahs_dog.name}")


  """
 Exercise 3 : Who’s the song producer?

Instructions

1. Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

3. Create an object, for example:
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

4. Then, call the sing_me_a_song method. The output should be:

There’s a lady who's sure

all that glitters is gold

and she’s buying a stairway to heaven
"""

class Song:
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for item in self.lyrics:
      print(f"{item}\n")

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

"""
Exercise 4 : Afternoon at the Zoo

Instructions

Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example:

{ 
    A: "Ape",
    B: ["Baboon", "Bear"],
    C: ['Cat', 'Cougar'],
    E: ['Eel', 'Emu']
}

Create a method called get_groups that prints the animal/animals inside each group.
Create an object called new_york_zoo and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example

Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)
"""

class Zoo:
  def __init__(self, zoo_name):
    self.name = zoo_name
    self.animals = []
  
  def add_animal(self, new_animal):
    if new_animal not in self.animals:
      self.animals.append(new_animal)

  def get_animals(self):
    print(f"\n The list of animals : ")
    for animal in self.animals:
      print(f"       {animal}")

  def sell_animal(self, animal_sold):
    if animal_sold in self.animals:
      self.animals.remove(animal_sold)
  
  def sort_animals(self):
    dict_animal = {}
    for animal in sorted(self.animals):
      first_letter = animal[0].upper()

      if first_letter in dict_animal:
        dict_animal[first_letter].append(animal)
      else:
        dict_animal[first_letter] = [animal]
    return dict_animal

  def get_groups(self):
    groups = self.sort_animals()
    for key, value in groups.items():
      print(f"{key}: {value}")

new_york_zoo = Zoo("new_york_zoo")

new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Anaconda")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

new_york_zoo.get_animals()

new_york_zoo.sell_animal("Anaconda")

print(f"\n{new_york_zoo.sort_animals()}\n")

new_york_zoo.get_groups()
"""
Exercise 1 : Pets

Instructions

Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

Create another cat breed named Siamese which inherits from the Cat class.
Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
Take all the cats for a walk, use the walk method.
"""

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal("Leo", 2)
chartreux_cat = Chartreux("Micho", 4)
siamese_cat = Siamese("Jungo", 1)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()


"""
Exercise 2 : Dogs

Instructions

Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
Create 3 dogs and run them through your class.
"""

class Dog:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight

  def bark(self):
    return f"{self.name} is barking"

  def run_speed(self):
    return self.weight/(self.age*10)

  def fight(self, other_dog):
    first_dog_score = self.run_speed() * self.weight
    second_dog_score = other_dog.run_speed() * other_dog.weight

    if first_dog_score > second_dog_score:
       return f"{self.name} won the fight!"
    elif second_dog_score > first_dog_score:
      return f"{other_dog.name} won the fight!"
    else:
      return "It's a tie!"

# Create 3 dogs
dog1 = Dog("Max", 5, 25)
dog2 = Dog("Rex", 3, 15)
dog3 = Dog("Snow", 7, 30)

# Run them through the class and test the methods
print(dog1.bark())
print(f"{dog1.name}'s run speed is {dog1.run_speed():.2f}\n")

print(dog2.bark())
print(f"{dog2.name}'s run speed is {dog2.run_speed():.2f}\n")

print(dog3.bark())
print(f"{dog3.name}'s run speed is {dog3.run_speed():.2f}\n")

# Test fight
print(f"{dog1.name} vs {dog2.name}:")
print(dog1.fight(dog2))

"""
Exercise 3 : Dogs Domesticated

Instructions

Create a new python file and import your Dog class from the previous exercise.
In the new python file, create a class named PetDog that inherits from Dog.
Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
Add the following methods:

* train: prints the output of bark and switches the trained boolean to True
* play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

* do_a_trick: If the dog is trained the method should print one of the following sentences at random:
  - “dog_name does a barrel roll”.
  - “dog_name stands on his back legs”.
  - “dog_name shakes your hand”.
  - “dog_name plays dead”.
"""
import random

class Dog:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight

  def bark(self):
    return f"{self.name} is barking"

  def run_speed(self):
    return self.weight/(self.age*10)

  def fight(self, other_dog):
    first_dog_score = self.run_speed() * self.weight
    second_dog_score = other_dog.run_speed() * other_dog.weight

    if first_dog_score > second_dog_score:
       return f"{self.name} won the fight!"
    elif second_dog_score > first_dog_score:
      return f"{other_dog.name} won the fight!"
    else:
      return "It's a tie!"

class PetDog(Dog):
  def __init__(self, name, age, weight, trained=False):
    super().__init__(name, age, weight)
    self.trained = trained

  def train(self):
    self.bark()
    self.trained = True

  def play(self, *dog_names):
    formatted_names = ", ".join(dog_names)
    print(f"{formatted_names} all play together.")

  def do_a_trick(self):
    if self.trained:
      tricks = [ " does a barrel roll", 
              " stands on his back legs", 
               " shakes your hand",
               " plays dead"]
      trick = random.choice(tricks)
      print(f"{self.name}{trick}")
    else:
      print(f"{self.name} is not trained yet.")

my_pet_dog = PetDog("Buddy", 5, 20)


print(f"\nIs {my_pet_dog.name} trained? {my_pet_dog.trained}")

# Test train method
my_pet_dog.train()
print(f"\nIs {my_pet_dog.name} trained now? {my_pet_dog.trained}\n")

# Test do_a_trick 
my_pet_dog.do_a_trick()

# Test the play method
my_pet_dog.play("Max", "Lucy", "Rocky")

# Test another PetDog instance
new_pet = PetDog("Daisy", 2, 10)
new_pet.do_a_trick()

"""
Exercise 4 : Family

Instructions

Create a class called Family and implement the following attributes:
  -  members: list of dictionaries
  -  last_name : (string)

Implement the following methods:
- born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
- is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
- family_presentation: a method that prints the family’s last name and all the members’ details.

Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]

"""

class Family:
  def __init__(self, members, last_name):
    self.members = members
    self.last_name = last_name

  def born(self, **new_member_info):
    self.members.append(new_member_info)
    print("May your baby bring endless joy, love, and blessings to your family.\n")

  def is_18(self, name):
    for member in self.members:
      if member["name"] == name.capitalize():
        if member["age"] > 18:
          return True
        else:
          return False

  def family_presentation(self): 
      print(f"The Family : {self.last_name}")
      for member in self.members:
        print("\n")
        for key, value in member.items():
          print(f"{key} : {value}")


family_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

johnson_family = Family(family_members, "Johnson")

johnson_family.born(name="Max", age=0, gender="Male", is_child=True)

print(f"is Michael over 18 : {johnson_family.is_18('Michael')}\n")

johnson_family.family_presentation()


"""
Exercise 5 : TheIncredibles Family

Instructions

Create a class called TheIncredibles. This class should inherit from the Family class:
This is no random family they are an incredible family, therefore the members attributes, 
will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

Add a method called use_power, this method should print the power of a member only if they are over 18 years old. 
If not raise an exception (look up exceptions) which stated they are not over 18 years old.

Add a method called incredible_presentation which :
- Print a sentence like “*Here is our powerful family **”
- Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]

Call the incredible_presentation method.

Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

Call the incredible_presentation method again.
"""

class Family:
  def __init__(self, members, last_name):
    self.members = members
    self.last_name = last_name

  def born(self, **new_member_info):
    self.members.append(new_member_info)
    print("\nMay your baby bring endless joy, love, and blessings to your family.")

  def is_18(self, name):
    for member in self.members:
      if member["name"] == name.capitalize():
        if member["age"] > 18:
          return True
        else:
          return False

  def family_presentation(self): 
      print(f"The Family : {self.last_name}")
      for member in self.members:
        print("\n")
        for key, value in member.items():
          print(f"{key} : {value}")

class TheIncredibles(Family):
  def __init__(self, members, last_name):
    super().__init__(members, last_name)

  def use_power(self, name):
    if self.is_18(name):
      for member in self.members:
        if member["name"] == name.capitalize():
          power = member["power"]
      print(f"{name} using {power}!\n")
    else:
        raise Exception(f"Not over 18 years old")

  def incredible_presentation(self):
    print("** Here is our powerful family **")
    super().family_presentation()
          

family_members = [
    {'name':'Michael','age':19,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

# Create an instance of the Family class
Incredibles_family = TheIncredibles(family_members, "Incredibles")

Incredibles_family.incredible_presentation()

Incredibles_family.born(name="Jack", age=0, gender="Male", is_child=True, power= "Unknown Power", incredible_name="None")

print("\n============= after adding Jack ==============")
Incredibles_family.incredible_presentation()
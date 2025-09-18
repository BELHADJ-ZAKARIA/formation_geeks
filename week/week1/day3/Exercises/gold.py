"""
Exercise 1 : Geometry

Instructions

Write a class called Circle that receives a radius as an argument (default is 1.0).
Write two instance methods to compute perimeter and area.
Write a method that prints the geometrical definition of a circle.
"""
from math import pi 

class Circle:
  def __init__(self, radius=1.0):
    self.radius = radius

  def perimeter(self):
    return 2*pi*(self.radius)

  def area(self):
    return pi*((self.radius)**2)
  
  def geometrical_def(self):
    print(f"\nYour circle has a radius of {self.radius}")
    print(f"perimeter is {self.perimeter():.2f}")
    print(f"area is {self.area():.2f}")

circle1 = Circle(2.3)

perimeter_circle1 = circle1.perimeter()

area_circle1 = circle1.area()

print(f"Perimeter : {perimeter_circle1:.2f}")
print(f"Area : {area_circle1:.2f}")

circle1.geometrical_def()


"""
Exercise 2 : Custom List Class

Instructions

Create a class called MyList, the class should receive a list of letters.
Add a method that returns the reversed list.
Add a method that returns the sorted list.

Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension)
"""
import random

class MyList:
  def __init__(self, list_of_letters):
    self.list_of_letters = list_of_letters

  def reversed_list(self):
    return sorted(self.list_of_letters, reverse=True)

  def sorted_list(self):
    return sorted(self.list_of_letters)

  #Bonus
  def second_list(self):
    return [random.randint(0, 100) for i in range(0, len(self.list_of_letters))] 
  
"""
Exercise 3 : Restaurant Menu Manager

Instructions

The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.
Create a python file called menu_manager.py.
Create a class called MenuManager.
Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). 
Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

Here is a list of the dishes currently on the menu:

    Soup – 10 – B - False
    Hamburger – 15 - A - True
    Salad – 18 - A - False
    French Fries – 5 - C - False
    Beef bourguignon– 25 - B - True

    Meaning: For the spice level:
       • A = not spicy,
       • B = a little spicy,
       • C = very spicy

The dishes provided above should be the value of the menu attribute.
Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.
Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.
"""

class MenuManager:
  def __init__(self):
    self.menu = [
            {
                "name": "Soup",
                "price": 10,
                "spice_level": "B",
                "gluten_index": False
            },
            {
                "name": "Hamburger",
                "price": 15,
                "spice_level": "A",
                "gluten_index": True
            },
            {
                "name": "Salad",
                "price": 18,
                "spice_level": "A",
                "gluten_index": False
            },
            {
                "name": "French Fries",
                "price": 5,
                "spice_level": "C",
                "gluten_index": False
            },
            {
                "name": "Beef bourguignon",
                "price": 25,
                "spice_level": "B",
                "gluten_index": True
            }
        ]

  def add_item(self, name, price, spice, gluten):
    self.menu.append({"name":name, "price":price, "spice_level":spice, "gluten_index":gluten})
  
  def update_item(self, name, price, spice, gluten):
  
    item_found = False
    for dish in self.menu:
       if dish["name"] == name:
        dish["price"] = price
        dish["spice_level"] = spice
        dish["gluten_index"] = gluten
        item_found = True
        break

    if not item_found:
      print(f"The dish '{name}' is not in the menu.\n")
  
  def remove_item(self, name):
    item_found = False
    for dish in self.menu:
      if dish["name"] == name:
        self.menu.remove(dish)
        item_found = True
        break

    if item_found:
      print(f"The dish '{name}' has been removed.\nUpdated menu: {self.menu}")
    else:
      print(f"\nThe dish '{name}' is not in the menu.\n")

  def __str__(self):
    return f"{self.menu}\n"
        
  
menu = MenuManager()

menu.add_item("Tajine", 25, "A", False)

menu.update_item("Barkoukch", 20, "A", True)

menu.remove_item("Soup")
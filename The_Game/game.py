import random

class Game:
  def __init__(self):
    pass

  def get_user_item(self):
    while(True):
      select = input("Select (r)ock, (p)aper, or (s)cissors: ")
      if select.lower() in ['r', 'p', 's']:
        break
    return select.lower()
  
  def get_computer_item(self):
    return random.choice(['r', 'p', 's'])

  def get_game_result(self, user_item, computer_item):
    if user_item == computer_item:
      return "draw"
    elif (user_item == "r" and computer_item == "s"):
      return "win"
    elif (user_item == "s" and computer_item == "p"):
      return "win"
    elif (user_item == "p" and computer_item == "r"):
      return "win"
    else:
      return "loss"

  def play(self):
    user_item = self.get_user_item()
    computer_item = self.get_computer_item()
    result = self.get_game_result(user_item, computer_item)
    print(f"You selected {user_item}. The computer selected {computer_item}. Result: {result}")
    return result
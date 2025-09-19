def get_user_menu_choice():
  print("Menu:")
  print("(g) Play a new game")
  print("(x) Show scores and Quit")

  user_choice = input(":")

  if user_choice.lower() in ["g", "x"]:
      return user_choice.lower()

def print_results(results):
  print("Game Results:")
  print(f" You won {results["win"]} times")
  print(f" You lost {results["loss"]} times")
  print(f" You drew {results["draw"]} times\n")
  print("Thank you for Playing!")

def main():
  results={"win": 0, "loss": 0, "draw": 0}
  while(True):
    choice = get_user_menu_choice()
    if choice == "x":
      print_results(results)
      break
    elif choice == "g":
      game = Game()
      result = game.play()
      results[result] +=1

main()
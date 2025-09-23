board = [" " for _ in range(9)]
current_player = "X"
game_is_running = True
winner = None

def display_board():
    print("\nTIC TAC TOE ")
    print("* * * * * * * *")
    print("* " + board[0] + "  | " + board[1] + " | " + board[2] + "  *")
    print("* ---+---+--- *")
    print("* " + board[3] + "  | " + board[4] + " | " + board[5] + "  *")
    print("* ---+---+--- *")
    print("* " + board[6] + "  | " + board[7] + " | " + board[8] + "  *")
    print("* * * * * * * *")

def player_input():
    global current_player
    
    valid_move = False
    while not valid_move:
        try:
            print(f"\nPlayer {current_player}'s turn...")
            row = int(input(f"\nEnter row : "))
            col = int(input(f"Enter column : "))
            
            if 1 <= row <= 3 and 1 <= col <= 3:
                position = (row - 1) * 3 + (col - 1)
                
                if board[position] == " ":
                    board[position] = current_player
                    valid_move = True
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input. Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_win():
    global winner
    if (board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " " or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "):
        winner = current_player
        return True
    return False

def check_tie():
    global game_is_running
    if " " not in board:
        game_is_running = False
        return True
    return False

def play():
    global game_is_running
    print("Welcome to Tic-Tac-Toe!")
    display_board()
    
    while game_is_running:
        player_input()
        display_board()
        
        if check_win():
            print(f"Congratulations! Player {winner} wins!")
            game_is_running = False
        elif check_tie():
            print("The game is a tie!")
            game_is_running = False
        else:
            switch_player()

if __name__ == "__main__":
    play()
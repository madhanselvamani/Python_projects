import random

game_board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
        ]

player = input("Choose your symbol 'X' or 'O': ").upper() 


def display_board(game_board):
        for row in game_board:
            print(" | ".join([cell if cell else " " for cell in row]))
            print("-" * 10)

def choose_symbol():

    if player == "X":
        print("You choose 'X' \nBot is 'O'")
        return "O"
    elif player == "O":
        print("You choose 'O' \nBot is 'X'")
        return "X"
    else:
        print("Choose the appropriate icon")

def start_game():
    while True:
        # display_board(game_board)
        row = int(input("Where would you like to place your symbol in the play board (0, 1 or 2)? "))
        cell = int(input(f"where would you like to place your symbol in {row} row:  "))

        if game_board[row][cell] is not None:
            print("That place is already filled, Choose anothor")
        else:
            game_board[row][cell] = player
            break     
        
def bot(bot):
    while True:
        row = random.randrange(3)
        cell = random.randrange(3)

        if game_board[row][cell] is  None:
            game_board[row][cell] = bot
            break

            

def check_win():
    
    for row in game_board:
        if all(cell == player for cell in row):
            return True
          
    for coll in range(3):
        if all(game_board[row][coll] == player for row in range(3)):
            return True
        
    if all(game_board[i][i] == player for i in range(3)) or \
       all(game_board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_bot_win(bot):
    
    for row in game_board:
        if all(cell == bot for cell in row):
            return True
          
    for coll in range(3):
        if all(game_board[row][coll] == bot for row in range(3)):
            return True
        
    if all(game_board[i][i] == bot for i in range(3)) or \
       all(game_board[i][2-i] == bot for i in range(3)):
        return True

    return False

def is_board_full():
    for row in game_board:
        for cells in row:
            if cells is None:
                return False
    return True

def main():
    bot_move = choose_symbol() 
    while True:
        start_game()
        bot(bot_move)
        if check_win():
            display_board(game_board)
            print("Congratulations! You win")
            break
        
        if check_bot_win(bot_move):
            display_board(game_board)
            print("sorry, You lose")
            break

        if is_board_full():
            display_board(game_board)
            print("The game ends in a draw")
            break

        display_board(game_board)

main()
    
    
    





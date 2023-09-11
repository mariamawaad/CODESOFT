
import os
import time
import random

tictac = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_game():
    print(" " + tictac[1] + " | " + tictac[2] + " | " + tictac[3] + "  ")
    print("---|---|---")
    print(" " + tictac[4] + " | " + tictac[5] + " | " + tictac[6] + "  ")
    print("---|---|---")
    print(" " + tictac[7] + " | " + tictac[8] + " | " + tictac[9] + "  ")
 
 
def is_win(tictac, player):
    if (tictac[1] == player and tictac[2] == player and tictac[3] == player) or \
            (tictac[4] == player and tictac[5] == player and tictac[6] == player) or \
            (tictac[7] == player and tictac[8] == player and tictac[9] == player) or \
            (tictac[1] == player and tictac[4] == player and tictac[7] == player) or \
            (tictac[2] == player and tictac[5] == player and tictac[8] == player) or \
            (tictac[3] == player and tictac[6] == player and tictac[9] == player) or \
            (tictac[1] == player and tictac[5] == player and tictac[9] == player) or \
            (tictac[3] == player and tictac[5] == player and tictac[7] == player):
        return True
    else:
        return False
 
 
def is_game_full(tictac):
    if " " in tictac:
        return False
    else:
        return True
 
 
def get_firstPlayer_move(tictac, player):
    if tictac[5] == " ":
        return 5
 
    while True:
        move = random.randint(1, 9)
        if tictac[move] == " ":
            return move
            break
 
    return 5
 
 
while True:
    os.system("cls")
    print_game()
 
    choice = input("Where to put ur move?. ")
    choice = int(choice)
 
    if tictac[choice] == " ":
        tictac[choice] = "X"
    else:
        print("NOT EMPTY")
        time.sleep(1)
 
    if is_win(tictac, "X"):
        os.system("cls")
      
        print_game()
        print("First Player wins FLAWLESS VICTORY")
        break
 

    if is_game_full(tictac):
        print("DRAW")
        break
 

    choice = get_firstPlayer_move(tictac, "O")
 

    if tictac[choice] == " ":
        tictac[choice] = "O"
    else:
        print
        ("NOT EMPTY")
        time.sleep(1)
 

    if is_win(tictac, "O"):
        os.system("cls")
    
        print_game()
        print("Second Player wins FLAWLESS VICTORY")
        break

    if is_game_full(tictac):
        print("DRAW")
        break

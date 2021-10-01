import time
import random

Names = ["name", "test", "admin"]

Signs = ["x", "o"]

def Print(text):
    for i in range(len(text)):
        time.sleep(.025)
        print(text[i], end="")

def Authenticate():
    valid = False
    while valid == False:
        player1 = input("Player 1: ")
        player2 = input("Player 2: ")
        
        if player1.lower() in Names and player2.lower() in Names: valid = True
        else:
            print("Retry.\n")
            continue    

def ChangeCurrentStatus(CurrentTurn: str, Player1, Player2) -> str:
    if CurrentTurn == Player1:
        return Player2
    else:
        return Player1
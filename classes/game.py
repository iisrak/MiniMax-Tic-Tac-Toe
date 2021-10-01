from classes.bot import *
from classes.helpers import *
from classes.gameHelpers import *
import random

Player1 = random.choice(Signs)
Signs.pop(Signs.index(Player1))
Player2 = Signs[0]

def PlayAIGame():
    CurrentTurn = "o"
    Slot = 0
    
    print("\nPlayer 1: " + Player1 + "\nMr. Bot: " + Player2 + "\n")

    DisplayTable()

    while CheckIfWon() == False:
        try:
            if CurrentTurn == Player1: 
                Slot = int(input("Player 1 turn: "))
                if Slot < 1 or Slot > 9 or IsOccupied(Slot): print("Invalid, try again! (1-9)\n"); continue
                AddChoice(Slot, CurrentTurn)

            else: BotChoice(Player2, Player1)

            CurrentTurn = ChangeCurrentStatus(CurrentTurn, Player1, Player2)

            DisplayTable()
        except: print("Invalid, try again! (1-9)\n")
    
        AnnounceWinner(Player1, Player2)

    return


def PlayGame():
    CurrentTurn = "o"
    Slot = 0
    
    print("\nPlayer 1: " + Player1 + "\nPlayer 2: " + Player2 + "\n")

    DisplayTable()

    while CheckIfWon() == False:
        try:
            if CurrentTurn == Player1: Slot = int(input("Player 1 turn: "))
            else: Slot = int(input("Player 2 turn: "))

            if Slot < 1 or Slot > 9 or IsOccupied(Slot): print("Invalid, try again! (1-9)\n"); continue

            AddChoice(Slot, CurrentTurn)
            CurrentTurn = ChangeCurrentStatus(CurrentTurn, Player1, Player2)

            DisplayTable()
        except: print("Invalid, try again! (1-9)\n")
    
    AnnounceWinner(Player1, Player2)

    return
# Imports
from classes.helpers import *
from classes.gameHelpers import *
from classes.game import *
import os

Authenticate()
print()

Print("Tic Tac Toe.\n\n1. Play against a friend.\n2. Play against a bot.\n\n")

decision = input("")
print()

if decision == "1": PlayGame() 
elif decision == "2": PlayAIGame()
else: print("Incorrect decision. Try again!")
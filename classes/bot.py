from classes.gameHelpers import *
import random
import math


def BotChoice(Bot: str, Player: str):
    if len(taken) == 0: AddChoice(random.choice(corners), Bot)
    elif len(taken) == 1 and taken[0] != 5: AddChoice(5, Bot)
    elif len(taken) == 1 and taken[0] == 5: AddChoice(random.choice(corners), Bot)
    else: AddChoice(MakeBestMove(Bot, Player), Bot)

def MiniMax(Depth: int, IsMax: bool, Bot: str, Player: str):
    Best = 0
    Score = CheckIfWon()

    if Score == Bot: return 10
    elif Score == Player: return -10
    elif Score == "Draw": return 0

    if (IsMax): Best = -math.inf
    else: Best = math.inf

    for Box in range(1, 10) :          
        if IsOccupied(Box) == False and IsMax == True:
            AddChoice(Box, Bot)
            Best = max(Best, MiniMax(Depth + 1, not IsMax, Bot, Player))
            RemoveChoice(Box, Bot)
        elif IsOccupied(Box) == False and IsMax == False:
            AddChoice(Box, Player)
            Best = min(Best, MiniMax(Depth + 1, not IsMax, Bot, Player))
            RemoveChoice(Box, Player)
    
    return Best

def MakeBestMove(Bot: str, Player: str):
    OptimalScore = -math.inf
    BestBox = 0

    for Box in range(1, 10):
        if IsOccupied(Box) == False:
            AddChoice(Box, Bot)
            Score = MiniMax(0, False, Bot, Player)
            RemoveChoice(Box, Bot)
            
            if Score > OptimalScore:
                OptimalScore = Score
                BestBox = Box

    return BestBox
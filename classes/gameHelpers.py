Grid = [
        ["1","2","3"],
        ["4","5","6"], 
        ["7","8","9"],
       ]

WinChoices = [
                [1,2,3],
                [1,5,9],
                [1,4,7],
                [4,5,6], 
                [7,8,9],
                [3,6,9],
                [3,5,7],
                [2,5,8]
             ]

corners = [1, 3, 7, 9]
sides = [2, 4, 6, 8]
nums = [1,2,3,4,5,6,7,8,9]
taken = []

def AddChoice(x: int, choice: str):
    taken.append(x)
    for row in Grid:
        for box in row:
            if box == str(x): row[row.index(box)] += choice;nums.pop(nums.index(x))

def RemoveChoice(x: int, choice: str):
    for row in Grid:
        for box in row:
            if str(x) in box: row[row.index(box)] = str(x);nums.append(x)

def DisplayTable():
    print()
    for row in Grid:
        for box in row:
            if "x" in box:print("x", end=" ")
            elif "o" in box:print("o", end=" ")
            else:print("-", end=" ")
        print()
    print()

def IsOccupied(x: int) -> bool:
    for row in Grid:
        for box in row:
            if str(x) + "x" in box or str(x) + "o" in box: return True
    return False

def GetOccupied(x: int):
	for row in Grid:
		for box in row:
			if box[0] == str(x) and IsOccupied(x) == True: return box[1]

def CheckIfWon():
	for Index in WinChoices:
		if (GetOccupied(Index[0]) == "x" and GetOccupied(Index[1]) == "x" and GetOccupied(Index[2])) == "x": return "x"
		elif (GetOccupied(Index[0]) == "o" and GetOccupied(Index[1]) == "o" and GetOccupied(Index[2])) == "o": return "o"
        
	for i in range(1, 10):
		if IsOccupied(i) == False: return False
	return "Draw"    

def AnnounceWinner(Player1: str, Player2: str):
    if CheckIfWon() == Player1: print("Player 1 has won the game!") 
    elif CheckIfWon() == Player2: print("Player 2 has won the game!")
    elif CheckIfWon() == "Draw": print("Draw! Nobody has won the game!")
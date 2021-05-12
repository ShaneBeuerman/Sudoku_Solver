#Sudoku solver


def printBoard(arr):
    for i in range(9):
        print(arr[i])

def solveSudoku(arr):
    #To do
    print("To do soon")

board = [0 for i in range(9)]
f = open("sudokuboard.txt", "r")
lineCount = 0
while(True):
    line = f.readline()
    if not line:
        break
    if lineCount > 9:
        break
    line = line.strip("\n")
    line = list(line.split(" "))
    board[lineCount] = line
    lineCount += 1
printBoard(board)
#Sudoku solver

def printBoard(array):
    for i in range(9):
        print(array[i])

def printSolutions():
    global solutions
    for solution in solutions:
        for i in range(9):
            print(solution[i])

def horizontalVerify(x, n):
    global arr
    for i in range(9):
        if arr[x][i] == n:
            return False
    return True

def verticalVerify(y, n):
    global arr
    for i in range(9):
        if arr[i][y] == n:
            return False
    return True

def boxVerify(x, y, n):
    global arr
    xBox = (x//3) * 3
    yBox = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if arr[xBox+i][yBox+i] == n:
                return False
    return True

def solveSudoku():
    global arr
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                for n in range(1,10):
                    if horizontalVerify(i, n) and verticalVerify(j, n) and boxVerify(i, j, n):
                        arr[i][j] = n
                        solveSudoku()
                        arr[i][j] = 0
                return
    t = tuple(map(tuple, arr))
    solutions.add(t)
                
arr = [ 0 for i in range(9)]
solutions = set()
f = open("unsolved.txt", 'r')
lineCount = 0
while(True):
    line = f.readline()
    if not line:
        break
    if lineCount > 9:
        break
    line = line.strip("\n")
    line = list(map(int, line.split(" ")))
    arr[lineCount] = line
    lineCount += 1
printBoard(arr)
solveSudoku()
print()
printSolutions()
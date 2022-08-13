board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    # Recursive backtracking algorithm
    find = findEmpty(bo)
    if not find:
        return True # We've found the solution!
    else:
        row, col = find
    
    for i in range(1, 10): # Loops through numbers 1-9 to see if it's a valid solution
        if valid(bo, i, (row, col)):
            bo[row][col] = i # If it is, add it to the baord

            if solve(bo): # Recursively try to finish the solution by calling solve on our new board
                return True

            bo[row][col] = 0

    return False 


def valid(bo, num, pos):
    # Checks row, column, and square we're in
    # Check row: first loop through every column in given row
    for i in range (len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # Checks through each column (element) in the row, and see if it's equal to number added in
            return False # If it is checking the position we just inserted, we ignore that position 
    
    # Check column
    for i in range (len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i: # Checks if current x value (col value) is 
            return False

    # Check box
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    for i in range (box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos: 
                return False
    
    return True

def printBoard(bo):
    for i in range (len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range (len(bo[0])): #gets length of the rows
            if j % 3 == 0 and j != 0: #makes sure line isn't printed on left side immediately
                print(" | ", end = "")

            if j == 8: # are we at last position?
                print (bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")

def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col;

    return None

printBoard(board)
print()
solve(board)
print()
printBoard(board)
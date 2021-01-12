# solver.py

def solve(board):
    #base case is filled board
    find = find_empty(board)
    if find==None:
        return True
    else:
        row, column = find
    
    for i in range(1,10):
        if valid(board,(row,column),i):
            board[row][column]=i
            
            if solve(board):
                return True
            
            board[row][column] = 0
            
    return False
            

def valid(board, pos, num):
    
    #check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1]!=i:
            return False
        
    #check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0]!=i:
            return False
            
    #check 3x3 square
    square_x = pos[1]//3
    square_y = pos[0]//3
    
    for i in range(square_y*3,square_y*3 + 3):
        for j in range(square_x*3,square_x*3 + 3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    
    return True
    

def find_empty(board):
    # Parameter board = Unfinished Board
    # Searches for nearest empty space 
    # Returns (row, column) co-ordinate of empty space

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) #pos
    return None


def print_board(board):
    # Print the formatted board
    
    for i in range(9):
        if i % 3 == 0:
            print("-----------------------")
        for j in range(9):
            if j % 3 == 0 and j!=0:
                print(" | ",end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")
    print("-----------------------")

board = [
        [4, 0, 0, 1, 0, 0, 0, 0, 0],
        [9, 0, 6, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 7],
        [7, 0, 9, 0, 0, 0, 1, 0, 0],
        [3, 0, 0, 8, 0, 1, 0, 0, 5],
        [0, 0, 5, 0, 0, 0, 9, 0, 6],
        [8, 0, 0, 0, 0, 4, 5, 0, 0],
        [0, 0, 0, 9, 0, 0, 3, 0, 1],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        
    ]


print_board(board)
solve(board)
print('\n')
print_board(board)

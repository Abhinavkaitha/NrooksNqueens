#!/usr/bin/env python3
# ao.py : Solve the N-Rooks and nQueens problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
# Updated by Abhinav Reddy Kaitha, 2018
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# The N-queens problem is: Given an empty NxN chessboard, place N queens on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.
import sys


# Count # of pieces in given row
#I have added 99 in place of X initially and then replaced it with X. So inorder to exclude
#it from the count I wrote if board[row][col]!=99:
def count_on_row(board, row):
    sum = 0
    for col in range(0, len(board[0])):
        if board[row][col]!=99:
            sum += board[row][col]

    return sum

# Count # of pieces in given column
def count_on_col(board, col):
    sum = 0
    for row in range(0, len(board)):
        if board[row][col] != 99:
            sum += board[row][col]

    return sum


#http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
#I got this count_diagonal idea from the above code
def count_on_diag1(board,r,c):
    row=r
    col=c
    sum=0
    while row>=0 and col<N:
        sum=sum+board[row][col]
        row=row-1
        col=col+1
    row=r
    col=c
    while row<N and col>=0:
        sum=sum+board[row][col]
        row=row+1
        col=col-1
    return sum
def count_on_diag2(board,r,c):
    row = r
    col = c
    sum = 0
    while row >=0 and col >= 0:
        sum = sum + board[row][col]
        row = row - 1
        col = col - 1
    row = r
    col = c
    while row < N and col < N:
        sum = sum + board[row][col]
        row = row + 1
        col = col + 1
    return sum
# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

#I did this inorder to exclude the loop from printable_board
#When I wrote this loop inside the Printable_board, the size of board incresed, since the number #of interations increased
def add_block(board):
    for i in range(0,len(l1)):
        board[l1[i]][l2[i]]=99
    return board

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    board=add_block(board)
    str = ""
    if type == "nrook":
        coin = "R"
    if type=="nqueen":
        coin = "Q"

    for row in range(0, N):
        list = []
        for col in range(0, N):
                if board[row][col]==99:
                    list.append("X")
                elif board[row][col] == 0:
                    list.append("_")
                else:
                    list.append(coin)
        str = str + " ".join(list) + "\n"
    return str



# Add a piece to the board at the given position, and return a new board 
#(doesn't change original)
#It checks whether there is a coin in the row and column. 
#It also checks whether the r and c are matching with the r and c of X. In that case, it will #not add the coin
#The same case with queen
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

def successors(board):
    a=[]
    if type=="nrook":
        if count_pieces(board)<N:
            for r in range(0,N):
                for c in range(0,N):
                    if r not in l1 or c not in l2:
                        if count_on_row(board, r) < 1 and count_on_col(board, c) < 1:
                            a = a + [add_piece(board,r,c)]
        return a
    elif type=="nqueen":
        if count_pieces(board) < N:
            for r in range(0, N):
                for c in range(0, N):
                    if r not in l1 or c not in l2:
                        if count_on_row(board, r) < 1 and count_on_col(board, c) < 1 and count_on_diag1(board,r,c)<1 \
                            and count_on_diag2(board, r, c) < 1: \
                                a = a + [add_piece(board, r, c)]
        return a
# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors(fringe.pop()):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False
#Arguments to accept input
type = str(sys.argv[1])
N = int(sys.argv[2])
b = int(sys.argv[3])
l = []
# I have stored the input in the form of a list
for i in range(0,2*b):
    l.append(int(sys.argv[4+i])-1)

l1 = []
l2 = []
# Am segregating the the x and y co-ordinates into l1 and l2 which is further used to place X
for i in range(0,len(l),2):
    l1.append(l[i])

for i in range(1,len(l),2):
    l2.append(l[i])

# Used two conditions, one for rooks and the other for queens. Queens doesn't have solution for N<=3, so I have excluded them.
initial_board = [[0]*N]*N

solution = solve(initial_board)
print(printable_board(solution) if solution else "Sorry, no solution found. :(")

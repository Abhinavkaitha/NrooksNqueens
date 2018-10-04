#!/usr/bin/env python3
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
# Updated by Abhinav Reddy Kaitha, 2018
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.


# In[15]:
import sys

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] )


# In[16]:


# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )


# In[17]:


# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )


# In[18]:


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
   # print("\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board]))
    #return "\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board])
    str=""
    for row in board:
        for square in row:
            if square==0:
                str+="_ "
            else:
                str+="R "
        str+="\n"
    return str


# In[19]:


# Add a piece to the board at the given position, and return a new board 
#(doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]  


# In[20]:


def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]


# In[57]:


#With the condition count_pieces<N, the N+1 problem is eliminated 
#By checking whether a coin is already present or not(if board[r][c]!=1), some states with already a coin, can be skipped
def successors2(board):
    a=[]
    if count_pieces(board)<N:
        for c in range(0,N):
            for r in range(0,N):  
                if board[r][c]!=1:
                    a=a+[add_piece(board,r,c)] 
    return a


# In[66]:


# with this successor function, if there is a coin in any row or column, it goes to the next one. 
# Instead of going to the ith column, if i coins are present on board, this program checks each and every column for a coin.
def successors3(board):
    a=[]
    if count_pieces(board)<N:
        for c in range(0,N):
            if count_on_col(board,c)>=1:continue
            else:
                for r in range(0,N):  
                    if count_on_row(board,r)>=1: continue
                    else:
                        a=a+[add_piece(board,r,c)] 
    return a


# In[67]:


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and          all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and          all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )


# In[68]:


# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors3( fringe.pop() ):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False


# In[71]:


N = int(sys.argv[1])
initial_board = [[0]*N]*N


# In[72]:


initial_board = [[0]*N]*N

solution = solve(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")


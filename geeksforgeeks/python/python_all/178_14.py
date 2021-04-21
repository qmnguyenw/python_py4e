Python implementation of automatic Tic Tac Toe game using random number



Tic-tac-toe is a very popular game, so let’s implement an automatic Tic-tac-
toe game using Python.

The game is automatically played by the program and hence, no user input is
needed. Still, developing a automatic game will be lots of fun. Let’s see how
to do this.

numpy and random Python libraries are used to build this game. Instead of
asking the user to put a mark on the board, code randomly chooses a place on
the board and put the mark. It will display the board after each turn unless a
player wins. If the game gets draw, then it returns -1.

 **Explanation :**  
play_game() is the main function, which performs following tasks :

  * Calls create_board() to create a 9×9 board and initializes with 0.
  * For each player (1 or 2), calls the random_place() function to randomly choose a location on board and mark that location with the player number, alternatively.
  * Print the board after each move.
  * Evaluate the board after each move to check whether a row or column or a diagonal has the same player number. If so, displays the winner name. If after 9 moves, there are no winner then displays -1.

Below is the code for the above game :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Tic-Tac-Toe Program using

# random number in Python

 

# importing all necessary libraries

import numpy as np

import random

from time import sleep

 

# Creates an empty board

def create_board():

 return(np.array([[0, 0, 0],

 [0, 0, 0],

 [0, 0, 0]]))

 

# Check for empty places on board

def possibilities(board):

 l = []

 

 for i in range(len(board)):

 for j in range(len(board)):

 

 if board[i][j] == 0:

 l.append((i, j))

 return(l)

 

# Select a random place for the player

def random_place(board, player):

 selection = possibilities(board)

 current_loc = random.choice(selection)

 board[current_loc] = player

 return(board)

 

# Checks whether the player has three 

# of their marks in a horizontal row

def row_win(board, player):

 for x in range(len(board)):

 win = True

 

 for y in range(len(board)):

 if board[x, y] != player:

 win = False

 continue

 

 if win == True:

 return(win)

 return(win)

 

# Checks whether the player has three

# of their marks in a vertical row

def col_win(board, player):

 for x in range(len(board)):

 win = True

 

 for y in range(len(board)):

 if board[y][x] != player:

 win = False

 continue

 

 if win == True:

 return(win)

 return(win)

 

# Checks whether the player has three

# of their marks in a diagonal row

def diag_win(board, player):

 win = True

 y = 0

 for x in range(len(board)):

 if board[x, x] != player:

 win = False

 if win:

 return win

 win = True

 if win:

 for x in range(len(board)):

 y = len(board) - 1 - x

 if board[x, y] != player:

 win = False

 return win

 

# Evaluates whether there is

# a winner or a tie 

def evaluate(board):

 winner = 0

 

 for player in [1, 2]:

 if (row_win(board, player) or

 col_win(board,player) or

 diag_win(board,player)):

 

 winner = player

 

 if np.all(board != 0) and winner == 0:

 winner = -1

 return winner

 

# Main function to start the game

def play_game():

 board, winner, counter = create_board(), 0, 1

 print(board)

 sleep(2)

 

 while winner == 0:

 for player in [1, 2]:

 board = random_place(board, player)

 print("Board after " + str(counter) + " move")

 print(board)

 sleep(2)

 counter += 1

 winner = evaluate(board)

 if winner != 0:

 break

 return(winner)

 

# Driver Code

print("Winner is: " + str(play_game()))  
  
---  
  
 __

 __

 **Output :**

    
    
    [[0 0 0]
     [0 0 0]
     [0 0 0]]
    Board after 1 move
    [[0 0 0]
     [0 0 0]
     [1 0 0]]
    Board after 2 move
    [[0 0 0]
     [0 2 0]
     [1 0 0]]
    Board after 3 move
    [[0 1 0]
     [0 2 0]
     [1 0 0]]
    Board after 4 move
    [[0 1 0]
     [2 2 0]
     [1 0 0]]
    Board after 5 move
    [[1 1 0]
     [2 2 0]
     [1 0 0]]
    Board after 6 move
    [[1 1 0]
     [2 2 0]
     [1 2 0]]
    Board after 7 move
    [[1 1 0]
     [2 2 0]
     [1 2 1]]
    Board after 8 move
    [[1 1 0]
     [2 2 2]
     [1 2 1]]
    Winner is: 2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


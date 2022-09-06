'''Problem:
In the 1983 movie "War Game" the computer is finally overturn by asking it to play a game of tic-tac-toe.
In this task, create a program called tic_tac_toe.py that implements this game for two players taking turn in selecting where in a 3x3 grid to put their markers.
In turn, ask each player which row and column they want to play. Make sure that the program checks if that row/column combination is empty. When a player has won,
end the game. When the whole board is full and there is no winner, announce a draw.
As the program will be fairly large, you should divide it into suitable functions that do subset of the problem, but it up to you to decide what functions to use.
See below for an example execution of the game:
'''
'''Desired output:
  1 2 3
1 - - - 
2 - - - 
3 - - - 
Player X, which row do you play? 2
Player X, which column do you play? 2
  1 2 3
1 - - - 
2 - X - 
3 - - - 
Player O, which row do you play? 1
Player O, which column do you play? 1
  1 2 3
1 O - - 
2 - X - 
3 - - - 
Player X, which row do you play? 2
Player X, which column do you play? 3
  1 2 3
1 O - - 
2 - X X 
3 - - - 
Player O, which row do you play? 3
Player O, which column do you play? 3
  1 2 3
1 O - - 
2 - X X 
3 - - O 
Player X, which row do you play? 2
Player X, which column do you play? 1
  1 2 3
1 O - - 
2 X X X 
3 - - O 
Player X won!
'''

# tic_tac_toe.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

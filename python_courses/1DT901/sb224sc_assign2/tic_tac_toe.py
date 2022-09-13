# tic_tac_toe.py
#
# Author: Samuel Berg
# Date: 12-Sep-2022
def winner(b):
    for i in range(len(b)):
        if b[i][0] is not None and b[i][0] == b[i][0] == b[i][0]:   # Fix
            return True
        else:
            return False


def getRowCol(board, col, row):
    if board[col][row] is None:
        board[col][row] = turn
    else:
        return True


def display_board(board):
    print('  1 2 3')
    for i, row in enumerate(board):
        print(i + 1, get_attribute(row[0]), get_attribute(
            row[1]), get_attribute(row[2]))
    return board


def get_attribute(b):
    if b is None:
        return '-'
    elif b is False:
        return 'X'
    else:
        return 'O'


def move(board, row, col, turn):
    board[col - 1][row - 1] = turn


'''
Board:
  1 2 3
1 - - -
2 - - -
3 - - -
None = -
False = X
True = O
'''
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]]

turn = False
while True:
    display_board(board)
    row = int(input(f'Player {get_attribute(turn)}, which row do you play? '))
    col = int(
        input(f'Player {get_attribute(turn)}, which column do you play? '))
    move(board, row, col, turn)
    if winner(board):
        display_board(board)
        print(f'{get_attribute(turn)} Won!')
        exit()
    turn = not turn

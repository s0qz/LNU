# tic_tac_toe.py
#
# Author: Samuel Berg
# Date: 12-Sep-2022
def winner(b):
    for i in range(0, 3):
        for j in range(0, 3):   # Goes out of range ??
            print(i, j)  # Debugging
            if b[i][j] is not None and b[i][j] == b[i + 1][j] == b[i + 2][j]:
                return True  # I think this checks all column solutions
            elif b[j][i] is not None and b[j][i] == b[j + 1][i] == b[j + 2][i]:
                return True  # I think this checks all row solutions

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


def move(board, col, row, turn):
    if board[row - 1][col - 1] is None:
        board[row - 1][col - 1] = turn
    else:
        print('Select an empty spot on the board.')
        row = int(
            input(f'Player {get_attribute(turn)}, which row do you play? '))
        col = int(
            input(f'Player {get_attribute(turn)}, which column do you play? '))
        move(board, row, col, turn)


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
    move(board, col, row, turn)
    if winner(board):
        display_board(board)
        print(f'{get_attribute(turn)} Won!')
        exit()
    turn = not turn

# CMPT 145: Assignment 3
# Cordell Blanchard
# chb344, 11236660
# 04, L06
# Helper script
#  randomly creates Connect 4 boards of different sizes
#  These random boards are not realistic, and the algorithm is
#  very naive:
#    Create an empty board
#    Choose a random column, and 'drop' a token ('X' or 'O')
#      if the column is full, choose another random column
#
#  A board is represented as a list of columns.
#  Because Connect-4 works using "gravity", dropping a token
#  is implemented by putting the new token at the end of a list.  
#  We're dropping a token "on top" of all the other tokens already 
#  in the column.  So the top of the column is the end of the list.

import random as rand


def random_filled(height, width):
    """
    Create a random board with given dimensions.
    A board is represented as a list of columns.
    """

    board = [[]] * width

    # Choose a random number of moves
    # - at least 8
    # - no more than 80% of the board is full
    plays = rand.randint(8,int(0.8*height*width))

    player = 'X'
    for i in range(plays):
        valid_col = False
        while not valid_col:
            col_choice = rand.randrange(0, width)
            col = board[col_choice]
            if len(board[col_choice]) < height:
                valid_col = True
                board[col_choice] = col + [player]

        player = swap_players(player)

    for c in board:
        while len(c) < height:
            c.append('.')

    return board


def swap_players(player):
    """
    Change player from X to O and vice versa
    return: the swapped value for player
    """
    if player == 'X':
        player = 'O'
        return player
    else:
        player = 'X'
        return player


def display_board(board):
    """
    Display the board to the console.
    The "front" of each column is "down".
    """
    print(height, width)
    for i in range(-1, -height-1, -1):
        for j in range(width):
            print(board[j][i], end='')
        print()

# generate a bunch
examples = 25

print(examples)
for i in range(examples):
    height = rand.randint(5,7)
    width = rand.randint(6,9)
    bd = random_filled(height, width)
    display_board(bd)
    print()

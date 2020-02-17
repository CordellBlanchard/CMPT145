# CMPT 145: Assignment 3
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import randomc4 as rand
print ("*** Test cases for swap_players ***")
# test for swap_players #1
if rand.swap_players('X') == 'O':  # checks if player is swapped for X
    print("Test case 1 works")
else:
    print("Test case 1 does not work. Expected output: 'O'")

# test for swap_players #2
if rand.swap_players('O') == 'X':  # checks if player is swapped for O
    print("Test case 2 works")
else:
    print("Test case 2 does not work. Expected output: 'X'")
print()

print("*** Test cases for random_filled ***")
# test 1 for random_filled
checks = ['X','O','.']
board = rand.random_filled(5, 7)
not_full = 0
for x in checks:  # checks if the board is full with all values it should have
    for i in range(7):
        for j in range(5):
            if board[i][j] !='X' and board[i][j] !='O' and board[i][j] != '.':
                not_full = 1
if not_full == 1:
    print("Test case 1 did not work, board contains objects other then X, O, .")
else:
    print("Test case 1 works")

# test 2 for random_filled
width = 7
height = 5
count = 0
board1 = rand.random_filled(height, width)
# checks the height and width of board
if len(board1) == width:
    for i in range(width):
        if len(board1[i]) != height:
            count = +1
    if count == 0:
        print("Test case 2 works")
    else:
        print("Test case 2 does not work", count, "columns do not have correct height")
else:
    print("Test case 2 board does not have correct width")
    print("Test case 2 does not work.")
print()
print("*** Visual test for display function ***")
print("To test display function run main file and check if your width and height are correct,"
      "\nand also check if dots in the boards column are vertical.")

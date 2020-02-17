# CMPT 145: Assignment 3
# Cordell Blanchard
# chb344, 11236660
# 04, L06
# Connect-4 referee script
# determines if a given Connect-4 board is one of the following:
#   - Win for X
#   - Win for O
#   - No decision
#   - Too small (for extreme examples)
#
#  The job is too big to solve all at once, so the task is
#  divided into checking rows and columns and diagonals separately


def check_4x1(cols):
    """
    Check a board consisting of 4 columns each of height 1
    """
    cols = [row[0] for row in cols]
    return check_1x4(cols)

def check_1x4(col4):
    """
    Check a board consisting of 1 column of height 4
    """
    col4 = ''.join(col4)
    if col4 == 'XXXX':
        return 'X'
    elif col4 == 'OOOO':
        return 'O'
    else:
        return 'No decision'

def check_4diags(square):
    """
    Pre Condition:
    square: a 4x4 list of lists
    Check a board consisting of 4 columns of height 4.
    Just check the diagonals up and down
    """
    diagup = [square[i][i] for i in range(4)]
    result = check_1x4(diagup)
    if result == 'No decision':
        diagdn = [square[3-j][j] for j in range(4)]
        return check_1x4(diagdn)
    else:
        return result


def extract_4_from_column(board, i, j):
    """
    Grab 4 tokens from column i in row j
    """
    return board[i][0+j:4+j]


def extract_4_from_row(board, j, i):
    """
    Grab 4 tokens from row j in column i
    """
    return [col[j] for col in board[0+i:4+i]]


def extract_4x4(board, i,j):
    """
    Grab a 4x4 region from the board starting at i, j
    """
    return [col[0+j:4+j] for col in board[0+i:4+i]]

def check_board(height, width, board):
    """
    Check the board assuming the given size.
    Checks rows, columns, and diagonals
    """
    if height < 4 and width < 4:
        return 'Too small'

    # check columns
    for i in range(width):
        for j in range(height-3):
            # extract 4 consecutive values from column i and check it
            consec = extract_4_from_column(board, i, j)
            result = check_1x4(consec)
            if result != 'No decision':
                return result

    # check rows
    for j in range(height):
        for i in range(width-3):
            # extract 4 consecutive values from row j and check it
            consec = extract_4_from_row(board, j, i)
            result = check_4x1(consec)
            if result != 'No decision' :
                return result

    # check diagonals
    for j in range(height-3):
        for i in range(width-3):
            square = extract_4x4(board, i, j)
            result = check_4diags(square)
            if result != 'No decision':
                return result

    # if no decision has been made earlier...
    return 'No decision'


# open file
file = open('examples.txt')

# read board

# first initialize the variables
board = []
square = []

# first line has the number of examples only
line = file.readline()
line = line.rstrip().split()
n_examples = int(line[0])

for i in range(n_examples):
    print('Example', i, end=' ')
    # read the size
    line = file.readline()
    line = line.rstrip().split()
    height = int(line[0])
    width = int(line[1])

    # read the board
    board = [[]] * width
    for j in range(height):
        line = file.readline().rstrip()
        for v in range(width):
            board[v] = board[v] + [line[v]]

    # read a single blank line after the board
    file.readline()
    print(check_board(height, width, board))

# CMPT 145: Assignment 3
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import check4 as check
print("*** Testing cases for check_1x4 ***")
# checks if outputs is X when needed
test_1 = ['X', 'X', 'X', 'X']
test_1_1 = check.check_1x4(test_1)
if test_1_1 == 'X':
    print("test case 1 works")
else:
    print("test case 1 does not work, expected 'X'")

# checks if output is O when needed
test_2 = ['O', 'O', 'O', 'O']
test_2_2 = check.check_1x4(test_2)
if test_2_2 == 'O':
    print("test case 2 works")
else:
    print("test case 2 does not work, expected 'O'")

# checks if output is No Decision when needed
test_2 = ['O', 'O', 'O', 'X']
test_3_3 = check.check_1x4(test_2)
if test_3_3 == 'No decision':
    print("test case 3 works")
else:
    print("test case 3 does not work, expected 'No decision'")
print()


print("*** Test cases for check_4x1 ***")
# checks if outputs is X when needed
test_1 = [['X'], ['X'], ['X'], ['X']]
test_1_1 = check.check_4x1(test_1)
if test_1_1 == 'X':
    print("test case 1 works")
else:
    print("test case 1 does not work, expected 'X'")

# checks if output is O when needed
test_2 = [['O'], ['O'], ['O'], ['O']]
test_2_2 = check.check_4x1(test_2)
if test_2_2 == 'O':
    print("test case 2 works")
else:
    print("test case 2 does not work, expected 'O'")

# checks if output is No Decision when needed
test_2 = [['O'], ['O'], ['O'], ['X']]
test_3_3 = check.check_4x1(test_2)
if test_3_3 == 'No decision':
    print("test case 3 works")
else:
    print("test case 3 does not work, expected 'No decision'")
print()


print("*** Test cases for check_4diags ***")
# checks if outputs 'X' for up diagonal
test_1 = [ ['X', '.', '.', '.'],
           ['.', 'X', '.', '.'],
           ['.', '.', 'X', '.'],
           ['.', '.', '.', 'X']]
test_1_1 = check.check_4diags(test_1)
if test_1_1 == 'X':
    print("test case 1 works")
else:
    print("test case 1 does not work, expected 'X'")


# checks if outputs 'X' for down diagonal
test_2 = [ ['.', '.', '.', 'X'],
           ['.', '.', 'X', '.'],
           ['.', 'X', '.', '.'],
           ['X', '.', '.', '.']]
test_2_2 = check.check_4diags(test_1)
if test_2_2 == 'X':
    print("test case 2 works")
else:
    print("test case 2 does not work, expected 'X'")

# checks if outputs 'O' for up diagonal
test_3 = [ ['O', '.', '.', '.'],
           ['.', 'O', '.', '.'],
           ['.', '.', 'O', '.'],
           ['.', '.', '.', 'O']]
test_3_3 = check.check_4diags(test_3)
if test_3_3 == 'O':
    print("test case 3 works")
else:
    print("test case 3 does not work, expected 'O'")

# checks if outputs 'O' for down diagonal
test_4 = [ ['.', '.', '.', 'O'],
           ['.', '.', 'O', '.'],
           ['.', 'O', '.', '.'],
           ['O', '.', '.', '.']]
test_4_4 = check.check_4diags(test_4)
if test_4_4 == 'O':
    print("test case 4 works")
else:
    print("test case 4 does not work, expected 'O'")

# checks if outputs 'No decision' for up diagonal
test_5 = [ ['O', '.', '.', '.'],
           ['.', 'X', '.', '.'],
           ['.', '.', 'O', '.'],
           ['.', '.', '.', 'O']]
test_5_5 = check.check_4diags(test_5)
if test_5_5 == 'No decision':
    print("test case 5 works")
else:
    print("test case 5 does not work, expected 'No decision'")

# checks if outputs 'No decision' for down diagonal
test_6 = [ ['.', '.', '.', 'O'],
           ['.', '.', 'X', '.'],
           ['.', 'O', '.', '.'],
           ['O', '.', '.', '.']]
test_6_6 = check.check_4diags(test_6)
if test_6_6 == 'No decision':
    print("test case 6 works")
else:
    print("test case 6 does not work, expected 'No decision'")
print()

print("*** Test cases for extract functions ***")
# to clear confusion for the list what appears to be columns are the rows and vice versa
test =   [['X', 'X', 'O', 'X', 'O', '.', '.'],
          ['X', 'O', 'O', 'O', '.', '.', '.'],
          ['O', '.', '.', '.', '.', '.', '.'],
          ['X', 'O', 'O', '.', '.', '.', '.'],
          ['O', 'O', 'X', 'X', 'X', 'O', 'X'],
          ['O', 'X', 'O', 'X', 'O', 'X', 'X'],
          ['O', 'X', 'O', '.', '.', '.', '.'],
          ['O', 'X', 'O', 'O', 'X', 'O', '.']]

# tests if extracts column of 4 from row 0 column 0
test_1_1 = check.extract_4_from_column(test, 0, 0)
if test_1_1 == ['X', 'X', 'O', 'X']:
    print("test case 1 works for extract_4_from_column")
else:
    print("test case 1 does not work for extract_4_from_column, expected ['X', 'X', 'O', 'X']")

# tests if extracts column of 4 from row 2 column 1
test_2_1 = check.extract_4_from_column(test, 1, 2)
if test_2_1 == ['O', 'O', '.', '.']:
    print("test case 2 works for extract_4_from_column")
else:
    print("test case 2 does not work for extract_4_from_column, expected ['O', 'O', '', '.']")

# tests if extracts row of 4 from row 2 column 1
test_1_2 = check.extract_4_from_row(test, 2, 1)
if test_1_2 == ['O', '.', 'O', 'X']:
    print("test case 1 works for extract_4_from_row")
else:
    print("test case 1 does not work for extract_4_from_row, expected ['O', '.', 'O', 'X']")

# tests if extracts row of 4 from row 3 column 2
test_2_2 = check.extract_4_from_row(test, 3, 2)
if test_2_2 == ['.', '.', 'X', 'X']:
    print("test case 2 works for extract_4_from_row")
else:
    print("test case 2 does not work for extract_4_from_row, expected ['.', '.', 'X', 'X']")

# tests if extracts 4x4 list starting at 2 (column) 2 (row)
test_1_3 = check.extract_4x4(test, 2, 2)
if test_1_3 == [['.', '.', '.', '.'], ['O', '.', '.', '.'], ['X', 'X', 'X', 'O'], ['O', 'X', 'O', 'X']]:
    print("test case 1 works for extract_4x4")
else:
    print("test case 1 does not work for extract_4x4, expected [['.', '.', '.', '.'], ['O', '.', '.', '.'], ['X', 'X', "
          "'X', 'O'], ['O', 'X', 'O', 'X']]")

# tests if extracts 4x4 list starting at 1 (column) 1 (row)
test_2_3 = check.extract_4x4(test, 1, 1)
if test_2_3 == [['O', 'O', 'O', '.'], ['.', '.', '.', '.'], ['O', 'O', '.', '.'], ['O', 'X', 'X', 'X']]:
    print("test case 2 works for extract_4x4")
else:
    print("test case 2 does not work for extract_4x4, expected [['O', 'O', 'O', '.'], ['.', '.', '.', '.'], "
          "['O', 'O', '.', '.'], ['O', 'X', 'X', 'X']]")
print()


print("*** Test cases for check_board ***")
test1 =  [['X', 'X', 'O', 'X', 'O', '.', '.'],
          ['X', 'O', 'O', 'O', '.', '.', '.'],
          ['O', '.', '.', '.', '.', '.', '.'],
          ['X', 'O', 'O', '.', '.', '.', '.'],
          ['O', 'O', 'X', 'X', 'X', 'O', 'X'],
          ['O', 'X', 'O', 'X', 'O', 'X', 'X'],
          ['O', 'X', 'O', '.', '.', '.', '.'],
          ['O', 'X', 'O', 'O', 'X', 'O', '.']]
test_1_1 = check.check_board(7, 8, test)
# checks for column with O as winner
if test_1_1 == "O":
    print("test case 1 works")
else:
    print("test case 1 does not work, expected 'O'")

test2 =  [['X', 'X', 'O', 'X', 'O', '.', '.'],
          ['X', 'O', 'O', 'O', '.', '.', '.'],
          ['O', '.', '.', '.', '.', '.', '.'],
          ['X', 'O', 'O', '.', '.', '.', '.'],
          ['X', 'X', 'X', 'O', 'X', 'O', 'X'],
          ['O', 'O', 'X', 'X', 'O', 'X', 'X'],
          ['O', 'X', 'O', 'X', '.', '.', '.'],
          ['O', 'X', 'O', 'O', 'X', 'O', '.']]
# checks for diagonal with X as winner
test_2_2 = check.check_board(7, 8, test2)
if test_2_2 == 'X':
    print("test case 2 works")
else:
    print("test case 2 does not work, expected 'X'")

test3 =  [['X', 'X', 'O', 'X', 'O', '.', '.'],
          ['X', 'O', 'O', 'O', '.', '.', '.'],
          ['O', '.', '.', '.', '.', '.', '.'],
          ['X', 'O', 'O', '.', '.', '.', '.'],
          ['X', 'X', 'X', 'O', 'X', 'O', 'X'],
          ['O', 'O', 'X', 'O', 'O', 'X', 'X'],
          ['O', 'X', 'O', '.', '.', '.', '.'],
          ['O', 'X', 'O', 'O', 'X', 'O', '.']]
# checks for no winner
test_3_3 = check.check_board(7, 8, test3)
if test_3_3 == 'No decision':
    print("test case 3 works")
else:
    print("test case 3 does not work, expected 'No decision'")



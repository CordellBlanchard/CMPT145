# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06

from a4q1 import *

# Tests for read_file()
# Not many tests are needed for read_file() if it works for 1
# correct file it should work for all
# Test 1 for read_file
N, square = read_file("no_3.3.txt")
if N != 3 and square != [[2, 3, 1], [3, 1, 1], [1, 2, 3]]:
    print("error in test 1 for read_file() expected N = 3 and square = [[2, 3, 1], [3, 1, 1], [1, 2, 3]] ")
# Test 2 for read_file
N, square = read_file("yes_5.1.txt")
if N != 5 and square != [[3, 4, 1, 5, 2], [2, 5, 4, 3, 1], [1, 3, 2, 4, 5], [4, 2, 5, 1, 3], [5, 1, 3, 2, 4]]:
    print("error in test 2 for read_file() expected N = 5 and square = [[3, 4, 1, 5, 2], [2, 5, 4, 3, 1], "
          "[1, 3, 2, 4, 5], [4, 2, 5, 1, 3], [5, 1, 3, 2, 4]] ")
# Tests for check_columns()
# Test 1 for check_columns()
square, N = [[1, 3, 2, 4], [2, 2, 1, 2], [3, 1, 3, 1], [4, 4, 4, 3]], 4
test = check_columns(square, N)
if not test:
    print("error in test 1 for check_columns(), expected True")
# Test 2 for check_columns()
square, N = [[1, 3, 2], [2, 4, 3], [3, 5, 1]], 3
test = check_columns(square, N)
if test:
    print("error in test 2 for check_columns(), expected False because second column "
          "does not contain values 1 through 3")
# Test 3 for check_columns()
square, N = [[1, 1, 1], [1, 2, 2], [3, 3, 3]], 3
test = check_columns(square, N)
if test:
    print("error in test 3 for check_columns(), expected False because first column "
          "does not contain values 1 through 3 exactly once")
# Test 4 for check_columns()
square, N = [[1, 2, 3], [1, 2, -10], [1, 2, 3]], 3
test = check_columns(square, N)
if test:
    print("error in test 4 for check_columns(), expected False because third column "
          "does not contain values 1 through 3 exactly once")
# Tests for check_rows()
# Test 1 for check_rows()
square, N = [[1, 3, 2, 4], [3, 2, 1, 4], [1, 2, 3, 4], [4, 3, 2, 1]], 4
test = check_rows(square, N)
if not test:
    print("error in test 1 for check_columns(), expected True")
# Test 2 for check_rows()
square, N = [[1, 1, 1], [1, 2, 3], [3, 2, 1]], 3
test = check_rows(square, N)
if test:
    print("error in test 2 for check_columns(), expected False because first row "
          "does not contain values 1 through 3 exactly once")
# Test 3 for check_columns()
square, N = [[1, 2, 3], [-10, 2, 2], [3, 2, 1]], 3
test = check_rows(square, N)
if test:
    print("error in test 3 for check_columns(), expected False because second row "
          "does not contain values 1 through 3 exactly once")
# Test 4 for check_columns()
square, N = [[1, 2, 3], [2, 3, 1], [-10, 100, 3]], 3
test = check_rows(square, N)
if test:
    print("error in test 4 for check_columns(), expected False because second column "
          "does not contain values 1 through 3")

# Tests for check_square()
# Test 1 for check_square()
square, N = [[1, 3, 2], [3, 2, 1], [2, 1, 3]], 3
test = check_square(square, N)
if not test:
    print("error in test 1 for check_square(), expected True")
# Test 2 for check_square()
square, N = [[1, 2, 3], [1, 2, 3], [1, 2, 3]], 3
test = check_square(square, N)
if test:
    print("error in test 2 for check_square(), expected False because columns are not"
          "valid")
# Test 3 for check_square()
square, N = [[1, 1, 1], [2, 2, 2], [3, 3, 3]], 3
test = check_square(square, N)
if test:
    print("error in test 3 for check_square(), expected False because rows are not valid")
# Test 4 (white box test) for check_square()
square, N = [[-10, 2, 10], [100, 2, 3], [4, 5, 3]], 3
test = check_square(square, N)
if test:
    print("error in test 4 for check_square(), expected False because square contains values"
          "out of range from 1...N")
# Test 5 for check_square()
square, N = [[3, 4 , 1, 5, 2], [2, 5, 4, 3, 1], [1, 3, 2, 4, 5], [4, 2, 5, 1, 3], [5, 1, 3, 2, 4]], 5
test = check_square(square, N)
if not test:
    print("error in test 5 for check_square(), expected True")

print("**** TEST SCRIPT COMPLETE ****")

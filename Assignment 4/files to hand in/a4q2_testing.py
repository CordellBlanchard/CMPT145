# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06

from a4q2 import *
import TStack as s

# These are visual tests and the answers are shown on a4q2_output.txt

# Tests cases for read_file_lines
# Test 1
test = reverse('months.txt')
if test != 'December November October, September\nAugust. July June, May\nApril March February January,\n':
    print('error did not print file in correct order')

# Test 2
test = reverse(1)
if test != 1:
    print('expected function to return 1 when not inputting a string')
print()

# Test 3
test = reverse('test2.txt')
if test != '20 19 18\n17 16 15 14 13\n12 11 10 9 8 7\n6 5 4 3 2 1\n':
    print('error did not print in correct order')


# Test 4
test = reverse('test3.txt')
if test != 'Hello this message\nis displayed backwards\nisnt that fun\nI think so\n':
    print('error did not print in correct order')

# Test 5
test = reverse('test4.txt')
if test != "cares' who5 but.\nwords42 the to attatched4\n'things? weird. with test\n":
    print('error did not print in correct order')
print('*** Test script completed ***')

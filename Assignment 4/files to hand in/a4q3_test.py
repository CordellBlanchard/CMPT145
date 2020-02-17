# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import a4q3 as a

# Test 1 for '+' operator
test = a.math_processing('( 1 + 5 )')
if test != 6:
    print('error in test 1 expected 6')

# Test 2 for '-' operator
test = a.math_processing('( 4 - 9 )')
if test != -5:
    print('error in test 2 expected -5')

# Test 3 for '*' operator
test = a.math_processing('( 100 * 10 )')
if test != 1000:
    print('error in test 3 expected 1000')

# Test 4 for '/' operator
test = a.math_processing('( 10 / 2 )')
if test != 5:
    print('error in test 4 expected 5')

# Test 5 for complex expression
test = a.math_processing('( ( ( 10 + 2 ) * 14 ) + ( 5 * 3 ) )')
if test != 183:
    print('error in test 5 expected 63')

# Test 6 for complex expression
test = a.math_processing('( ( ( -100 * 8 ) + 900 ) / ( ( ( 7 * 10 ) + 10 ) - 10 ) )')
if test != 10/7:
    print('error in test 6 expected 10/7')

# Test 7 for complex expression
test = a.math_processing('( ( 10 / 2 ) * 20 )')
if test != 100:
    print('error in test 7 expected 100')

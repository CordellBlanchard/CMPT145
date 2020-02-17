# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import a4q3 as a

# intro
print("Welcome to Calculator! Input your expressions.")
while True:
    expression = input('> ')

    # allows user to exit program
    if expression == 'quit':
        print('Thanks for using Calculator!')
        break

    evaluation = a.math_processing(expression)
    print(evaluation)

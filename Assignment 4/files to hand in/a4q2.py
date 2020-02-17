# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import TStack as s


def reverse(filename):
    """
    Purpose: to reverse file lines and words
    Pre-Conditions:
    filename: string that is name of file to be reversed
    Post-Conditions: prints the reversed filed
    Return: None
    """
    if isinstance(filename, str) is not True:
        print("Error: file name input must be of the type string")
        return 1

    stack = s.create()
    file = open(filename)
    test_string = ''  # initializing string for testing purposes
    # iterates through each line in file and splits the words
    for line in file:
        WordList = line.split()
        # iterates through each word
        for word in WordList:
            # for printing reasons adds new line to every first word at the beginning of a line
            if word == WordList[0]:
                word = word + '\n'
                s.push(stack, word)
            # for printing reasons for every other word adds a space to each word
            else:
                word = word + ' '
                s.push(stack, word)

    # prints the reversed file
    for i in range(s.size(stack)):
        test_string += str(s.pop(stack))
    print(test_string)
    file.close()
    return test_string

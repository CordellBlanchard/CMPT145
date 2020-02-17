# Cordell Blanchard, chb344, 11236660, CMPT145 Section 04, L06
def obtain_file():
    """
    This function opens a file and returns the date inside word by word as a list
    """
    print("Insert name of file")
    data1 = open(input(), 'r')
    data2 = []
    for line in data1:  # iterates through each line of text file
        for word in line.split():  # iterates through each word of each line in file and appends data to list
            data2.append(word)
    data1.close()
    return data2

    # all blocks for all the rotation functions are similar and are swapping the values of the corresponding row/column
    # to "rotate them" in the direction specified
def rotate_left(torus, operation):
    """
    torus: a list containing each integer from the torus square
    operation: a value containing the info of what row is to be rotated
    return: a torus square (integer by integer) that has a specific row rotated to the left corresponding to
    inputted operation
    """
    if operation is 0:
        temp = torus[0]
        torus[0] = torus[1]
        torus[1] = torus[2]
        torus[2] = temp
    elif operation is 1:
        temp = torus[3]
        torus[3] = torus[4]
        torus[4] = torus[5]
        torus[5] = temp
    elif operation is 2:
        temp = torus[6]
        torus[6] = torus[7]
        torus[7] = torus[8]
        torus[8] = temp
    return torus


def rotate_right(torus, operation):
    """
    torus: a list containing each integer from the torus square
    operation: a value containing the info of what row is to be rotated
    return: a torus square (integer by integer) that has a specific row rotated to the right corresponding to
    inputted operation
    """
    if operation is 0:
        temp = torus[2]
        torus[2] = torus[1]
        torus[1] = torus[0]
        torus[0] = temp
    elif operation is 1:
        temp = torus[5]
        torus[5] = torus[4]
        torus[4] = torus[3]
        torus[3] = temp
    elif operation is 2:
        temp = torus[8]
        torus[8] = torus[7]
        torus[7] = torus[6]
        torus[6] = temp
    return torus


def rotate_up(torus, operation):
    """
    torus: a list containing each integer from the torus square
    operation: a value containing the info of what column is to be rotated
    return: a torus square (integer by integer) that has a specific column rotated up corresponding to
    inputted operation
    """
    if operation is 0:
        temp = torus[0]
        torus[0] = torus[3]
        torus[3] = torus[6]
        torus[6] = temp
    elif operation is 1:
        temp = torus[1]
        torus[1] = torus[4]
        torus[4] = torus[7]
        torus[7] = temp
    elif operation is 2:
        temp = torus[2]
        torus[2] = torus[5]
        torus[5] = torus[8]
        torus[8] = temp
    return torus


def rotate_down(torus, operation):
    """
    torus: a list containing each integer from the torus square
    operation: a value containing the info of what column is to be rotated
    return: a torus square (integer by integer) that has a specific column rotated down corresponding to
    inputted operation
    """
    if operation is 0:
        temp = torus[6]
        torus[6] = torus[3]
        torus[3] = torus[0]
        torus[0] = temp
    elif operation is 1:
        temp = torus[7]
        torus[7] = torus[4]
        torus[4] = torus[1]
        torus[1] = temp
    elif operation is 2:
        temp = torus[8]
        torus[8] = torus[5]
        torus[5] = torus[2]
        torus[2] = temp
    return torus


def main():
    """
    input a file from the a1q3 examples folder and the square after all rotations are done will be printed
    """
    data = obtain_file()
    torus = [int(x) for x in data[0:9]]  # gathers the torus square from data as integers
    number_of_operations = int(data[9])
    operations = data[10:11 + number_of_operations*2]  # gathers the operations word by word in a list

    # iterates through the letters to determine which direction the rotation is in
    for i in range(0, number_of_operations*2, 2):
        if operations[i] == 'D':
            rotate_down(torus, int(operations[i+1]))
        elif operations[i] == 'U':
            rotate_up(torus, int(operations[i+1]))
        elif operations[i] == 'L':
            rotate_left(torus, int(operations[i+1]))
        elif operations[i] == 'R':
            rotate_right(torus, int(operations[i+1]))
    # prints the rotated torus square
    for i in range(0, 9, 3):
        print(torus[i], torus[i+1], torus[i+2])

    return 0


main()

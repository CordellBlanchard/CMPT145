# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06


def read_file(filename):
    """
    Purpose:
        To convert the text file into useful information to check the NxN square
    Pre Conditions:
        filename: a string containing name of file to be read
    PostConditions: None
    Return:
         N: A positive integer containing The order of the square N,
        square: a NxN list of integers containing values specified in file
    """

    file = open(filename)
    N = int(file.readline())
    square = []  # initialize list square

    # iterates through file and makes a NxN list from the numbers in file
    for i in range(N):
        line = file.readline().split()
        square.append([])   # adds N rows to each list
        for j in line:  # add corresponding int values from the file to square
            square[i].append(int(j))
    file.close()
    return N, square


def check_columns(square, N):
    """
    Purpose:
        To check if every column in square is correct for a Latin square
    Pre Conditions:
        square: NxN list of integers
        N: Positive integer representing order of square
    PostConditions: None
    Return:
       True if all columns in square contain 1 through N exactly once, False otherwise
    """
    count = 0
    # iterates through each column
    for i in range(N):
        seen = [False]*N  # re-initializes seen after each column iteration
        for j in range(N):
            value = square[j][i]
            if 1 <= value <= N:  # accounts for values out of range
                if seen[value - 1]:  # accounts for if values repeat
                    count += (N+1)
                else:
                    seen[value-1] = True
        if all(seen):  # adds 1 if all values are present in a column
            count += 1
    if count == N:
        return True
    else:
        return False


def check_rows(square, N):
    """
    Purpose:
        To check if every row in square is correct for a Latin square
    Pre Conditions:
        square: NxN list of integers
        N: Positive integer representing order of square
    PostConditions: None
    Return:
       True if all rows in square contain 1 through N exactly once, False otherwise
    """
    count = 0
    # iterates through each row
    for i in range(N):
        seen = [False]*N  # re-initializes seen after each row iteration
        for j in range(N):
            value = square[i][j]
            if 1 <= value <= N:  # accounts for values out of range
                if seen[value - 1]:  # accounts for if values repeat
                    count += (N+1)
                else:
                    seen[value-1] = True
        if all(seen):  # adds 1 if all values are present in a column
            count += 1
    if count == N:
        return True
    else:
        return False


def check_square(square, N):
    """
    Purpose:
        To check if NxN square is Latin
    Pre Conditions:
        square: NxN list of integers
    N: Positive integer representing order of square
        PostConditions: None
    Return:
        True if square is Latin, False otherwise
    """

    columns = check_columns(square, N)
    rows = check_rows(square, N)
    if rows and columns:
        return True
    else:
        return False

def main():
    """
    Purpose:
    To ask a user for a file name, read the file, and check if there is a latin square
    Post Conditions:
    Prints "YES" if square is Latin, "NO" otherwise
    """
    filename = input("Please input the name of the file: ")
    N, square = read_file(filename)
    check = check_square(square, N)

    if check:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()

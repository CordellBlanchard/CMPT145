# CMPT 145 Assignment 2
# Name : Cordell Blanchard
# ID: 11236660
# NSID : chb344
# Lab : 06
# Lecture : 04


def print_image(image):
    """
    Purpose:
        Display the ascii image to the console.
    Pre-conditions:
        image: a list of lists
    Post-Conditions:
        None
    Return:
        a new list with the rows in reverse order
    """
    for row in image:
        for char in row:
            print(char, end='')
        print()


def flip_updown(image):
    """
    Purpose:
        Flip the image upside down
    Preconditions:
        image: a list of lists containing single-character strings
    Post-Conditions:
        the same list (image) with the rows in reverse order
    Return:
        None
    """
    image.reverse()
    return None


def flip_leftright(image):
    """
    Purpose:
        Flip the image left to right
    Preconditions:
        image: a list of lists containing single-character strings
    Post-Conditions:
        the same list (image) with the columns in reverse order
    Return:
        None
    """
    i = 0
    for row in image:
        new_row = []
        for char in row:
            new_row = [char] + new_row
            image[i] = new_row
        i += 1
    return None


def read_image(filename):
    """
    Decode the named file, producing a list of lists.
    image: a list of lists
    """

    # the file is opened
    file = open(filename)

    # the file has 2 lines;
    # the header has the number of rows and the number of columns
    header = file.readline()
    header = header.rstrip().split(' ')
    rows = int(header[0])
    cols = int(header[1])

    # the second line is the data, a runlength-encoded image
    data = file.readline()

    # tidy up by closing the file immediately
    file.close()

    decoded = decode_image(data)
    image = decompress(decoded, rows, cols)
    return image


def decode_image(data):
    """
    Decode the data, by parsing the run-length encoding
    """
    # the data consists of information about characters, e.g.
    # 5:a, 16:b, 1:c
    # this means 5 'a' followed by 16 'b' followed by 1 'c'
    # This function produces the list [(5, 'a'), (16, 'b'), (1, 'c')]

    data = data.rstrip('\n').split(':')  # adjusted this line according to professors instructions

    # the tricky part is that this data is jammed together like this:
    # 5:a16:b1:c
    # splitting on ':' gives us ['5', 'a16', 'b1', 'c']
    # We can use slicing to separate the single character from the integer.

    # Even trickier, the character could be ':', e.g. 16::  which means 16 ':'.
    # Splitting 5:a16::1:c gives us ['5', 'a16', '', '1', 'c']
    # To handle this, we use a flag that indicates a ':' was inferred from a ''

    # set up two lists to store the items
    counts = []
    chars = []

    # the split produces a number as the first element, no character
    counts.append(int(data[0]))

    colon = False
    for code in data[1:-1]:
        if code == '':
            # infer ':' from a '', and set the flag
            chars.append(':')
            colon = True
        elif colon:
            # if the previous char was ':' then the current code is just a number
            counts.append(int(code))
            # reset the flag
            colon = False
        else:
            # the normal case cN, where c is a single character, and N is an integer
            chars.append(code[0])
            counts.append(int(code[1:]))

    # the very last item is just a character
    chars.append(data[-1])

    # return the list of all tuples (N, c)
    return zip(counts, chars)


def decompress(decodedimage, rows, cols):
    """
    Decompress the decoded data.

    decodedimage: a list of tuples (N, c)
    rows: the number of rows for the image
    cols: the number of columns for the image
    :return: a list of lists
    """
    # the raw image is just a sequence of single characters
    rawimage = []
    for N, c in decodedimage:
        rawimage.extend([c] * N)

    # here we produce the right number of rows and columns
    img = []
    for i in range(rows):
        img.append(rawimage[i * cols:(i + 1) * cols])
    return img


def print_title(astring):
    """
    Print a string with some title like formatting
    """
    print('\n')
    print('-+' * 40)
    print(astring, end='\n\n')


# Main script

img = read_image('a1q2-square.txt')

print_title("The Image")
print_image(img)

print_title("The Image, Upside Down")
flip_updown(img)
print_image(img)

print_title("The Image, Mirrored")
flip_updown(img)
flip_leftright(img)
print_image(img)

print_title("The Image, Upside Down and Mirrored")
flip_updown(img)
print_image(img)

# done

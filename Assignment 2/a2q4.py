# CMPT 145 Assignment 2
# Name : Cordell Blanchard
# ID: 11236660
# NSID : chb344
# Lab : 04
# Lecture : 06
#
# Synopsis :
# This script is a game, showing all outputs.
# the following lines are used to create the dungeon according to instructions from a file.
# They are also to play the game corresponding to directions inputted by a user.
# The goal of the game is to find the prize (G) and escape the NxN dungeon through
# exploring. Players lose if they enter a room with a monster (W) or trap (P), and can only travel N, E, W,or S.


import a2q4_dialog as flavour


def create_room():
    """
    Purpose: Creates an empty room in the dungeon
    Pre-conditions: None
    Post-conditions: None
    Return: A dictionary named room that contains info of room, and of the rooms
        around (N,E,S,W)
    """
    room = {}
    room['contents'] = None
    room['N'] = None
    room['E'] = None
    room['S'] = None
    room['W'] = None
    return room


def connect(room1, axis, room2):
    """
    Purpose: Connects adjacent rooms
    Pre-conditions:
        room1: A dictionary containing info of room and rooms around it, must be
        a room that is below or to the left of room 2 by 1 block
        room2: A dictionary containing info of room and rooms around it, must be
        a room that is above or to the right of room 1 by 1 block
        axis: A string the represents the common axis the two rooms are on (ex. if room 1 and room 2 are both in the same
        row then axis would be 'row')
    Post-conditions: Modifies lists room1 and room2's keys so that the 2 rooms are connected
    Return: None
    """
    if axis == 'row':
        room1['N'] = room2
        room2['S'] = room1
    else:
        room1['E'] = room2
        room2['W'] = room1


def create_dungeon(size, items):
    """
    Purpose: Creates a NxN grid dungeon
    Pre-conditions:
        size: integer value describing the size N of the grid dungeon
        items: a list of tuples containing room contents: goal, traps, and monsters along with
        locations of their corresponding rooms on the grid
    Post-conditions: None
    Return: the dictionary room where the player starts which is connected to all rooms in the dungeon
    """
    dungeon = []
    for r in range(size):
        row = []
        for c in range(size):
            row.append(create_room())
        dungeon.append(row)

    for row in range(size):
        for col in range(size - 1):
            connect(dungeon[row][col], 'row', dungeon[row][col + 1])

    for col in range(size):
        for row in range(size - 1):
            connect(dungeon[row][col], 'col', dungeon[row + 1][col])

    for item, r, c in items:
        dungeon[r][c]['contents'] = item

    return dungeon[0][0]


def terminal(room):
    """
    Purpose: Detects if someone hits a trap or monster
    Pre-conditions: the dictionary room which player is in
    Post-conditions: None
    Return: true if contents in room are 'W' or 'P' False otherwise
    """
    c = room['contents']
    return c in ['W', 'P']


def describe_room(room):
    """
    Purpose: Describes room player is currently in and detects contents of adjacent rooms
    Pre-conditions:
        room: a dictionary containing info about whats inside and near by
    Post-conditions: prints a corresponding message if contents of room are a trap, monster, or goal
        if none are present then prints a message detecting if a monster or trap is in an adjacent room
    Return: None
    """

    if room['contents'] == 'W':
        print(flavour.content['W'])
        return
    if room['contents'] == 'P':
        print(flavour.content['P'])
        return
    if room['contents'] == 'G':
        print(flavour.content['G'])

    close_by = []
    for n in 'NSEW':
        if room[n] is not None:
            close_by.append(room[n]['contents'])

    if 'W' not in close_by and 'P' not in close_by:
        print(flavour.closeby['E'])
    if 'W' in close_by:
        print(flavour.closeby['W'])
    if 'P' in close_by:
        print(flavour.closeby['P'])


def read_play(filename):
    """
    Purpose: reads the file containing info on game setup
    Pre-conditions:
        filename: name of text file containing info needed to play the game
    Post-conditions: None
    Return: a dictionary containing the locations of the goal, monsters, and traps on the grid
        and the size of the dungeon
    """
    file = open(filename)
    size = int(file.readline().rstrip())
    locations = []
    for i in range(4):
        line = file.readline().rstrip().split()
        locations.append((line[0], int(line[1]), int(line[2])))
    file.close()
    return {'size': size,
            'locations': locations}


def play(size, locations):
    """
    Purpose: plays the game
    Pre-conditions:
        size: size of the dungeon
        locations: locations of the goal, monsters, and traps
    Post-conditions: if player hits trap/monster sends message that game is over,
        if goal is hit and player returns to starting position sends message for winning,
        if no goal or monster/trap is hit and player returns to start position prints
        message for exiting dungeon
    Return: int numbers: 1000 - steps taken for winning (score for winning), size of dungeon - steps taken (score for
    getting out of dungeon alive), -1000 (score for losing)
    """
    start = create_dungeon(size, locations)
    gotG = False
    loc = start
    describe_room(loc)
    PrevRoom = ''
    steps = 0
    while loc == loc or loc == PrevRoom:
        steps +=1
        s = input("Input direction you wish to travel (N, S, W, or E): ")
        if (s != "N") and (s != 'S') and (s != 'W') and (s != 'E'):  # makes sure user in inputting correct directions
            print("Must input a correct direction (N, S, W, or E)")
        else:
            PrevRoom = loc
            loc = loc[s]
            if loc == start:  # breaks from loop if player returns to start without goal
                describe_room(loc)
                break
            if loc is None:  # does not let player go out of bounds
                print("You have hit a wall go in a different direction.")
                loc = PrevRoom
            describe_room(loc)
            if terminal(loc):  # breaks from loop if player hits trap/monster
                break
            if loc['contents'] == 'G':
                gotG = True
                loc['contents'] = None
            if loc is start and gotG is True:  # breaks from loop if player returns to start after collecting goal
                break

    if loc is start and gotG:
        print(flavour.final['W'], 'Final Score:', 1000-steps)
        return 1000 - steps
    elif loc is start:
        print(flavour.final['F'], "Final score:", (size**2 - steps)*steps)
        return (size**2 - steps)*steps
    else:
        print(flavour.final['L'], "Final score:", -1000)
        return -1000


game = read_play('wumpus4_0.txt')
play(game['size'], game['locations'])

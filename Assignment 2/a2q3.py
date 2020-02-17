# CMPT 145 Assignment 2
# Name : Cordell Blanchard
# ID: 11236660
# NSID : chb344
# Lab : 04
# Lecture : 06
#
# Synopsis :
# This script simulates a game, showing all outputs that players will see.
# the following lines are used to create the dungeon, and replay the game corresponding
# to instructions on how the game will be run. The goal of the game is to find the
# prize (G) and escape the NxN dungeon through exploring. Players lose if they enter a room
# with a monster (W) or trap (P), and can only travel N, E, W,or S.


import flavourSW as flavour


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


def read_replay(filename):
    """
    Purpose: reads the file containing info on game instructions
    Pre-conditions:
        filename: name of text file containing info needed to replay the game
    Post-conditions: None
    Return: a dictionary containing the locations of the goal, monsters, and traps on the grid,
        the size of the dungeon, and the directions the player moved in the game (in trip)
    """
    file = open(filename)
    size = int(file.readline().rstrip())
    locations = []
    for i in range(4):
        line = file.readline().rstrip().split()
        locations.append((line[0], int(line[1]), int(line[2])))
    trip = file.readline().rstrip()
    file.close()
    return {'size': size,
            'locations': locations,
            'trip': trip}


def replay(size, locations, trip):
    """
    Purpose: replays the game
    Pre-conditions:
        size: size of the dungeon
        locations: locations of the goal, monsters, and traps
        trip: directions that the player moved (ex. 'NEWS')
    Post-conditions: if player hits trap/monster sends message that game is over,
        if goal is hit and player returns to starting position sends message for winning,
        if no goal or monster/trap is hit and player returns to start position prints
        message for exiting dungeon
    Return: int number 1000, 0 , -1000 corresponding to score received at end of game
    """
    start = create_dungeon(size, locations)
    gotG = False
    loc = start

    describe_room(loc)
    for s in trip:
        loc = loc[s]
        describe_room(loc)
        if terminal(loc):
            break
        if loc['contents'] == 'G':
            gotG = True
            loc['contents'] = None

    if loc is start and gotG:
        print(flavour.final['W'])
        return 1000
    elif loc is start:
        print(flavour.final['F'])
        return 0
    else:
        print(flavour.final['L'])
        return -1000


game = read_replay('wumpus4_5.txt')
replay(game['size'], game['locations'], game['trip'])

# CMPT 145: Linear ADTs
# Cordell Blanchard
# chb344, 11236660
# 04, L06

# Implements a finite capacity Queue
#
# A queue (also called a FIFO queue) is a compound data 
# structure in which the data values are ordered according to 
# the FIFO (first-in first-out) protocol.
#
# This style of queue has a fixed capacity, defined 
# when the queue is created.  Enqueue operations 
# will add the given data to the queue, as long as 
# the number of values in the queue is less than the 
# capacity.  If the length of the queue is equal to the
# capacity, the value cannot be added.  

# TO-DO complete the implementations


def create(cap):
    """
    Purpose
        creates an empty queue, with a given capacity 
    Return
        an empty queue
    """
    b = dict()
    b['storage'] = list()  # data goes here
    b['capacity'] = cap    # remember the capacity
    return b



def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return len(queue['storage']) == 0


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    return len(queue['storage'])


def enqueue(queue, value):
    """
    Purpose
        adds the given data value to the given queue
    Pre-conditions:
        queue: a queue created by create()
        value: data to be added
    Post-condition:
        if the capacity is not exceeded, the value 
        is added to the queue.
    Return:
        (none)
    """
    if len(queue['storage']) != queue['capacity']:
        queue['storage'].append(value)


def dequeue(queue):
    """
    Purpose
        removes and returns a data value from the given queue
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        the first value is removed from the queue
    Return:
        the first value in the queue
    """
    return queue['storage'].pop(0)

def peek(queue):
    """
    Purpose
        returns the value from the front of given queue
        without removing it
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        None
    Return:
        the value at the front of the queue
    """
    return queue['storage'][0]

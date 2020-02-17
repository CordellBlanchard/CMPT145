# CMPT 145 Assignment 5
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import TStack as Stack


def create():
    """
    Purpose
        creates an empty queue
    Return
        an empty queue
    """
    return Stack.create()


def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return Stack.is_empty(queue)


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    return Stack.size(queue)


def enqueue(queue, value):
    """
    Purpose
        adds the given data value to the given queue
    Pre-conditions:
        queue: a queue created by create()
        value: data to be added
    Post-condition:
        the value is added to the queue
    Return:
        (none)
    """
    return Stack.push(queue, value)

   
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
    TempStack = Stack.create()  # Temporary stack to aid in the process of removing and returning first in queue

    # inputs all all values from queue in reverse order into TempStack
    # and pops all values out of queue
    for j in range(Stack.size(queue)):
        val = Stack.pop(queue)
        Stack.push(TempStack, val)

    first = Stack.pop(TempStack)  # first value of queue

    # pushes all values back into queue in correct order with first value removed
    for i in range(Stack.size(TempStack)):
        val = Stack.pop(TempStack)
        Stack.push(queue, val)

    return first



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
    TempStack = Stack.create()  # Temporary stack to aid in the process of removing and returning first in queue

    # inputs all all values from queue in reverse order into TempStack
    # and pops all values out of queue
    for j in range(Stack.size(queue)):
        val = Stack.pop(queue)
        Stack.push(TempStack, val)

    first = Stack.pop(TempStack)  # first value of queue
    Stack.push(TempStack, first)  # puts value back

    # pushes all values back into queue in correct order with first value removed
    for i in range(Stack.size(TempStack)):
        val = Stack.pop(TempStack)
        Stack.push(queue, val)

    return first

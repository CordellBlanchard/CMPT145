# CMPT 145 Assignment 5
# Cordell Blanchard
# chb344, 11236660
# 04, L06


import TQueue as Queue


def create():
    """
    Purpose
        creates an empty stack (whcih is actually a queue)
    Return
        an empty Queue
    """
    return Queue.create()


def is_empty(stack):
    """
    Purpose
        checks if the given stack has no data in it
    Pre-conditions:
        stack is a stack created by create()
    Return:
        True if the stack has no data, or false otherwise
    """
    return Queue.is_empty(stack)


def size(stack):
    """
    Purpose
        returns the number of data values in the given stack
    Pre-conditions:
        stack: a stack created by create()
    Return:
        The number of data values in the queue
    """
    return Queue.size(stack)

def push(stack, value):
    """
    Purpose
        adds the given data value to the given stack
    Pre-conditions:
        stack: a stack created by create()
        value: data to be added
    Post-condition:
        the value is added to the stack
    Return:
        (none)
    """
    Queue.enqueue(stack, value)

def pop(stack):
    """
    Purpose
        removes and returns a data value from the given stack
    Pre-conditions:
        stack: a stack created by create()
    Post-condition:
        the top value is removed from the stack
    Return:
        returns the value at the top of the stack
    """
    TempQueue = Queue.create()  # Temporary stack to aid in the process of removing and returning top in stack

    # inputs all all values from stack into TempQueue
    # and dequeues all values out of stack except for top stack value
    for j in range(Queue.size(stack)-1):
        val = Queue.dequeue(stack)
        Queue.enqueue(TempQueue, val)

    top = Queue.dequeue(stack)  # top value of stack

    # enqueues all values back into stack in correct order with top value removed
    for i in range(Queue.size(TempQueue)):
        val = Queue.dequeue(TempQueue)
        Queue.enqueue(stack, val)

    return top

def peek(stack):
    """
    Purpose
        returns the value from the front of given stack
        without removing it
    Pre-conditions:
        stack: a stack created by create()
    Post-condition:
        None
    Return:
        the value at the front of the stack
    """
    TempQueue = Queue.create()  # Temporary stack to aid in the process of removing and returning top in stack

    # inputs all all values from stack into TempQueue
    # and dequeues all values out of stack except for top stack value
    for j in range(Queue.size(stack)-1):
        val = Queue.dequeue(stack)
        Queue.enqueue(TempQueue, val)

    top = Queue.dequeue(stack)  # top value of stack

    # enqueues all values back into stack in correct order with top value removed
    for i in range(Queue.size(TempQueue)):
        val = Queue.dequeue(TempQueue)
        Queue.enqueue(stack, val)

    Queue.enqueue(stack, top)  # returns top value to stack

    return top


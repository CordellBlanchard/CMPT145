# CMPT 145: Assignment 5 Question 3
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import node as node
import to_string_checker as t


def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """
    # check if node chain is empty
    if node_chain is None:
        return 0
    else:
        anode = node_chain
        count = 1  # not 0 since there will be at least one node if not empty
        # goes through node chain counting how many nodes there are
        while node.get_next(anode) is not None:
            count += 1
            anode = node.get_next(anode)
        return count



def contains_duplicates(node_chain):
    """
    Purpose:
        Returns whether or not the given node_chain contains one
        or more duplicate data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Return:
        :return: True if duplicate data value(s) were found,
        False otherwise
    """
    walker = node_chain
    # checks for empty node_chain
    if walker is None:
        return False
    # walker walks along node chain
    while node.get_next(walker) is not None:
        checker = walker
        # checker starts to walk from walker to end of chain
        while node.get_next(checker) is not None:
            checker = node.get_next(checker)
            if node.get_data(checker) == node.get_data(walker):
                return True
        walker = node.get_next(walker)

    return False



def insert_at(node_chain, value, index):
    """
        Purpose:
            Insert the given value into the node-chain so that
            it appears at the the given index.
        Pre-conditions:
            :param node_chain: a node-chain, possibly empty
            :param value: a value to be inserted
            :param index: the index where the new value should appear
            Assumption:  0 <= index <= n
                         where n is the number of nodes in the chain
    Post-condition:
            The node-chain is modified to include a new node at the
            given index with the given value as data.
    Return
            :return: the node-chain with the new value in it
    """
    anode = node_chain
    prev = None
    # if node_chain is empty creates a new one with value in it
    if anode is None:
        node_chain = node.create(value)
        return node_chain
    else:
        # iterate to index desired in node
        for i in range(index):
            prev = anode
            anode = node.get_next(anode)
        if prev is not None:
            node.set_next(prev, node.create(value, anode))
        else:
            node_chain = node.create(value, anode)
        return node_chain




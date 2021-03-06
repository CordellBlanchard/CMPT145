"""
CMPT 145 Computing with Python Lists, References
"""

def copy1(data):
    """
    Returns a copy of the given list of data
    Preconditions:
        :param data: a list
    Return:
        a copy of the given data
    """
    copied = data
    return copied


def copy2(data):
    """
    Returns a copy of the given list of data
    Preconditions:
        :param data: a list
    Return:
        a copy of the given data
    """
    copied = []
    for d in data:
        copied.append(d)
    return copied


def copy3(data, copy):
    """
    Copies the given list of data.
    Preconditions:
        :param data: a list
        :param copy: a list with the same contents as data
    :return: None
    """
    for d in data:
        copy.append(d)
        data.remove(d)


def copy4(data, copy):
    """
    Copies the given list of data.
    Preconditions:
        :param data: a list
        :param copy: an empty list 
    Post-conditions:
        copy has the same contents as data
    :return: None
    """
    for d in data:
        copy.append(d)


def copy5(data):
    """
    Returns a copy of the given list of data
    Preconditions:
        :param data: a list
    Return:
        a copy of the given data
    """
    copied = []
    for d in data:
        copied += [d]
    return copied


def selection_sort(unsorted):
    """
    Returns a list with the same values as unsorted,
    but reorganized to be in increasing order.
    :param unsorted: a list of comparable data values
    :return:  a sorted list of the data values
    """

    result = list()

    # TODO use one of the copy() functions here
    acopy = copy5(unsorted)
    while len(acopy) > 0:
        out = min(acopy)
        acopy.remove(out)
        result.append(out)


    return result

print(selection_sort([3,5,4,1,2]))
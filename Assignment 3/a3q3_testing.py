# Assignment 3: ADTs and Testing
# CMPT 145: Assignment 3
# Cordell Blanchard
# chb344, 11236660
# 04, L06
# This script is a starter file for testing the Statistics ADT

import Statistics as Stat

#####################################################################
# test Statistics.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],
     'outputs':[0, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # we'll open the data structure in these tests
    # check the initial count
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the initial ave
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs':[1, 0], # [count, avg]
     'reason' : 'No change to avg'},
    { 'inputs' : [0.0],
      'outputs': [1, 0],
      'reason' : 'Floating point values used'
    },
    {
        'inputs' :[3],
        'outputs':[1, 3],
        'reason' : 'None zero int'
    },
    {
        'inputs' :[3.0000],
        'outputs': [1,3],
        'reason' : 'larger floating point used'
    },
    {
        'inputs' : [-10],
        'outputs': [1,-10],
        'reason' : 'Negative integer'
    },
    {
        'inputs': [1.0+1.0],
        'outputs': [1, 2],
        'reason' : 'Using different kinds of floating point arithmetic'
    },
    {
        'inputs': [3.67],
        'outputs': [1, 3.67],
        'reason' : 'rational floating point value'
    }


]

for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # now call add()
    Stat.add(thing, args_in[0])

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[5, 0],          #[count, avg]
     'reason' : 'All zeroes'},
    {
        'inputs' : [10, -10, 5, -5],
        'outputs': [4, 0],
        'reason': 'inputs cancel'
    },
    {
       'inputs': [1.0, 1.0, 1.0],
       'outputs': [3, 1],
       'reason': 'arithmetic on floating point values'
    },
    {
        'inputs': [1.0-1.0, 2.0-1.0, 2-1],
        'outputs': [3, 2/3],
        'reason': 'arithmetic on floating point values'
    },
    {
        'inputs': [1, 2, 3],
        'outputs': [3, 2],
        'reason' : 'multiple int values'
    },
    {
        'inputs' : [100, 345, 15210, -12030, 10100002],
        'outputs': [5, 2020725.4],
        'reason': 'large values used'
    }


]

for t in test_mean:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call mean()
    result = Stat.mean(thing)

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

    # check the result of mean()
    if result != expected[1]:
        print('Error in mean(): expected avg', expected[1],
              ' but found ', result, '--', t['reason'])

print('*** Test script completed ***')
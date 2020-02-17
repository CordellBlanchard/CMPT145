# CMPT 145: Assignment 4
# Cordell Blanchard
# chb344, 11236660
# 04, L06

import TStack as s
import TQueue as q
import isfloat as i

def math_processing(input):
    """
    Purpose: To preform mathematical operations based on a given mathematical expression
    Pre-Conditions:
    input: string that contains mathematical expression with normal notation
    Return: the final value of the expression as an integer
    """
    # initialize data structures
    expression = q.create()
    numeric = s.create()
    operator = s.create()

    expr = input.split()

    # inputting all values of the expression intro a queue
    for j in expr:
        q.enqueue(expression, j)

    while not q.is_empty(expression):
        op = q.dequeue(expression)
        # if the symbol can be converted to float pushes to numeric stack
        if i.isfloat(op):
            op = float(op)
            s.push(numeric, op)
        # if symbol contains a operator pushes it onto operator stack
        elif op == '+' or op == '-' or op == '*' or op == '/':
            s.push(operator, op)
        # if symbol is ')' evaluates correct operation and pushes evaluation onto numeric stack
        elif op == ')':
            oper = s.pop(operator)
            v1 = s.pop(numeric)
            v2 = s.pop(numeric)
            if oper == '+':
                s.push(numeric, v1 + v2)
            elif oper == '-':
                s.push(numeric, v2 - v1)
            elif oper == '*':
                s.push(numeric, v1 * v2)
            elif oper == '/':
                s.push(numeric, v2 / v1)
    return s.pop(numeric)











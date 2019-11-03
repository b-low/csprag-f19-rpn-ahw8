#!/usr/bin/env python3

import operator
import readline
import sys


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()
            
def calculate_single(calculation):
    print("Result: ", calculate(calculation))

def calculate_forever():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        calculate_single(" ".join(sys.argv[1:]))
    else:
        calculate_forever()

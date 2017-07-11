#!/usr/bin/python3

from sys import argv

program, a, b = argv

def larger(x, y):
    '''THERE IS NO HELP'''
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print('x=y')

print(larger(a,b))

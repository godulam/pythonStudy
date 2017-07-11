#!/usr/bin/python3

import random

def coinFlipCount(c):
    h=0
    t=0
    for i in range(0,c):
        flip = random.randrange(0,2)
        if (flip==0):
            h+=1
        if (flip==1):
            t+=1
    print(h, ' heads')
    print(t, 'tails')

coinFlipCount(100)

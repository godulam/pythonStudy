#!/usr/bin/python3

a = input('type first value: ')
b = input('type second value: ')

def add():
    return float(a)+float(b)

def sub():
    return float(a)-float(b)

def multi():
    return float(a)*float(b)

def div():
    return float(a)/float(b)

def opers = {
    '+': add(),
    '-': sub(),
    '/': div(),
    '*': multi()
}

while True:
    action = input('what kind of operation you\'d like to perform?\n \
(+ - / * %[modulo] **[exponent] //[floor division]): ')
    if action

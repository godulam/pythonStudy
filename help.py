#!/usr/bin/python3

from sys import argv
program, command = argv

def getHelp(comm):
    print(help(comm))

getHelp(command)

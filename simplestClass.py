#!/bin/python3

class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi! My name is ", self.name)

p=Person('Kokos')

p.say_hi()
#!/usr/bin/python3

from sys import argv
program, a, action, b = argv

"""
a = input('type first value: ')
action = input('what kind of operation you\'d like to perform?\n \
(+ - / * %[modulo] **[exponent] //[floor division]): ')
b = input('type second value: ')
"""

# sum
if (action=='+' and a.isnumeric() and b.isnumeric()):
    print('The sum is ',float(a)+float(b))
# sub
elif (action=='-' and a.isnumeric() and b.isnumeric()):
    print('The sub is ',float(a)-float(b))
# multikulti
elif (action=='*' and a.isnumeric() and b.isnumeric()):
    print('The multi is ',float(a)*float(b))
# div
elif (action=='/' and a.isnumeric() and b.isnumeric()):
    print('The div is ',float(a)/float(b))
# modulo
elif (action=='%' and a.isnumeric() and b.isnumeric()):
    print('The modulo is ',float(a)%float(b))
# exponent
elif (action=='**' and a.isnumeric() and b.isnumeric()):
    print('The exponent is ',float(a)**float(b))
# floor division
elif (action=='//' and a.isnumeric() and b.isnumeric()):
    print('The floor div is ',float(a)//float(b))
# if the input is wrong, below message is printed out
else:
    print('wrong input')




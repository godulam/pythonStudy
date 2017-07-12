#!/usr/bin/python3

"""
from sys import argv
program, a, action, b = argv
"""

a = input('type first value: ')
action = input('what kind of operation you\'d like to perform?\n \
(+ - / * %[modulo] **[exponent] //[floor division]): ')
b = input('type second value: ')


def calculator():
    '''
    IT IS A SIMPLE CALCULATOR AND I'M A CAPS FAN.
    THIS IS TEXT.
    '''
    # sum
    if (action == '+' and a.isnumeric() and b.isnumeric()):
        print('The sum is ', float(a) + float(b))
    # sub
    elif (action == '-' and a.isnumeric() and b.isnumeric()):
        print('The sub is ', float(a) - float(b))
    # multikulti
    elif (action == '*' and a.isnumeric() and b.isnumeric()):
        if (int(b) == 2):
            print('The multi is ', int(a) << 1)
        if (int(b) == 4):
            print('The multi is ', int(a) << 2)
        if (int(b) == 8):
            print('The multi is ', int(a) << 3)
        if (int(b) == 16):
            print('The multi is ', int(a) << 4)
        else:
            print('The multi is ', float(a) * float(b))
    # div
    elif (action == '/' and a.isnumeric() and b.isnumeric()):
        print('The div is ', float(a) / float(b))
    # modulo
    elif (action == '%' and a.isnumeric() and b.isnumeric()):
        print('The modulo is ', float(a) % float(b))
    # exponent
    elif (action == '**' and a.isnumeric() and b.isnumeric()):
        print('The exponent is ', float(a) ** float(b))
    # floor division
    elif (action == '//' and a.isnumeric() and b.isnumeric()):
        print('The floor div is ', float(a) // float(b))
    # if the input is wrong, below message is printed out
    else:
        print('wrong input')


calculator()
# below line prints out comment in ''' ''' from the start of the function
print(calculator.__doc__)

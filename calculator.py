#!/usr/bin/python3

a = input('type first value: ')
action = input('what kind of operation you\'d like to perform? (+ - \
/ *): ')
b = input('type second value: ')

if (action=='+' and a.isnumeric() and b.isnumeric()):
    print('The sum is ',float(a)+float(b))
elif (action=='-' and a.isnumeric() and b.isnumeric()):
    print('The sub is ',float(a)-float(b))
elif (action=='*' and a.isnumeric() and b.isnumeric()):
    print('The multi is ',float(a)*float(b))
elif (action=='/' and a.isnumeric() and b.isnumeric()):
    print('The div is ',float(a)/float(b))
else:
    print('wrong input')




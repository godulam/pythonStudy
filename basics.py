# use format method to convert
# age variable to string

age = 20
name = "Zbigniew"

print("{0} is {1}".format(name, age))

# or it can be done that way
age += 5
print(name + " is " + str(age))

# numbers in {} brackets are optional
age -= 14
print("{} is {}".format(name, age))

# by default print ends with \n new line
# use below code to write in one line

print('\n', end='')
print('a', end=';')
print('b', end='@')
print('c')

import math
# decimal (.) precision of 3 for float '0.333'
pi = math.pi
print('\n{0:.3f}'.format(pi))

# fill with underscores (_) with the text centered
# (^) to 22 width '___hello___'
print('{0:_^22}'.format('hello'))

# keyword-based 'Zbigniew wrote "Necronicon"'
print('{name} wrote {book}'.format(name='Zbigniew', book='Necronicon'))

# escape characters
print('\tjan\tmaria\trokita\n\tjan\tzbigniew\twodecki')
print('This is not really long string \
but I will still separate it.')

# raw string (no escape characters)
print(r'Des \n pa \n cito')

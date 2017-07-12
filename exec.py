#!/usr/bin/python3

import re
import modules

# can be executed from command line
print('russia')

modules.randomStuff()
print()
print('name:\t\t', modules.__name__)
print('version:\t', modules.__version__)
print('file:\t\t', modules.__file__,'\n')

print('vars(modules): ')
for i in (vars(modules)):
    if not(re.search(r'__', i)):
        print(i)
        print('oooooooooooooooooo')

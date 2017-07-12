import sys

__name__ = 'klops'
__version__ = '0.1'

def randomStuff():


    print('CLA: ')
    for i in sys.argv:
        print(i)

    print('________________________________________________')

    for j in sys.path:
        print(j)

    print('________________________________________________')

    if __name__ == '__klops__':
        print('chuck itself')
    else:
        print('chuck imported')

    print('________________________________________________')


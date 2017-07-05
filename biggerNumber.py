x = input('give the value of variable x: ')
y = input('give the value of variable y: ')
if (x > y):
    print ('x = {}'.format(x))
    z = input('give the value of variable z: ')
    if (x > z):
        print ('x = {}'.format(x))
    else:
        print ('z = {}'.format(z))
else:
    print ('y = {}'.format(y))
    z = input('give the value of variable z: ')
    if (y > z):
        print ('y = {}'.format(y))
    else:
        print ('z = {}'.format(z))

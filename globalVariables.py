# input section
# fixed x, m and c typed by the user
x = 66
m = int(input('what is the multiplier? '))
c = input('do you want to multiply?\ntype \'1\' if you want a program \
to run or \'0\' if you don\'t ')

# function multiplier prints multiplication of 2 inputs
# global variable x is used inside of a function multiplier
# there is a additional argument named condition set by default as
# true to specify if you'd like to run a function or not
def multiplier(multi, condition=1):
    if (int(condition)==True):
        global x
        print (x * multi)
    else:
        print('that\'s too bad...')
multiplier(m,c)

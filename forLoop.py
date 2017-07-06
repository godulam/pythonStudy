# creates for loop for range of 1 to 20 with step of 4
for i in range(1, 20, 4):
    print(i)
else:
    print('The for loop is over')

print()

# used list for range
for i in list(range(5)):
    print(i)
    if (i==3):
        print('BREAK')
        break
else:
    print('The for loop is over')

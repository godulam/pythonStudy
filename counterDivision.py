k = 0
for i in range (4,8):
    for j in range (3,9):
        print ('{} / {} = {}'.format(i, j, i/j))
        k += (i/j)
    print()
print ('Sum of all divisions is: {}'.format(k))

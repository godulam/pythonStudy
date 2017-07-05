# look for typed number in given array
myArray = [1,53,322,64,23,65,32,14,66,74,325,600,9000]
j = len(myArray)
searchVal = input('What do you want to find? ')
for i in range (0, j):
    if (myArray[i]==int(searchVal)):
            print('found on position {}'.format(i+1))

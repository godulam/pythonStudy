# binary search array
myArray = [1,53,322,64,23,65,32,14,66,74,325,600,9000]
myArray = sorted(myArray)

arrLen = len(myArray)
halfLen = arrLen // 2

print (myArray)

searchVal = input('What do you want to find? ')

if (int(searchVal) < myArray[halfLen]):
    for i in range (0, halfLen):
        if (myArray[i]==int(searchVal)):
            print('found on position {}'.format(i))
elif (int(searchVal) > myArray[halfLen]):
    for j in range (halfLen, arrLen):
        if (myArray[j]==int(searchVal)):
            print('found on position {}'.format(j))
else:
    print('found on position {}'.format(halfLen))

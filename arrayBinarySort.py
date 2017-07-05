# binary search array
myArray = [1,53,322,64,23,65,32,14,66,74,325,600,9000]
myArray = sorted(myArray)

arrLen = len(myArray)
halfLen = arrLen // 2
print (halfLen)

searchVal = input('What do you want to find? ')
if (int(searchVal) < myArray[halfLen]):
    for i in range (0, halfLen):
        if (myArray[i]==int(searchVal)):
            print('found on position {}'.format(i+1))
# else:
#     for j in range (halfLen+1, arrLen):
#         if (myArray[j]==int(searchVal))
#             print('found on position {}'.format(j+1))
#

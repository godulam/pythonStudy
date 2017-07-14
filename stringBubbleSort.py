import time

wordString=input('string: ')
wordListB=[]
wordListQ=[]
charCount=len(wordString)

for i in wordString:
    wordListB.append(i.lower())
    wordListQ.append(i.lower())

def bubbleSorter():
    for j in range (0,charCount-1):
        for i in range (0,charCount-1):
            if ord(wordListB[i])>ord(wordListB[i+1]):
                x=wordListB[i]
                wordListB[i]=wordListB[i+1]
                wordListB[i+1]=x
    print (wordListB)

start_time = time.time()
bubbleSorter()
print("--- %s seconds ---" % (time.time() - start_time))

def quickSorter():
    wordListQ.sort()
    print(wordListQ)

start_time = time.time()
quickSorter()
print("--- %s seconds ---" % (time.time() - start_time))

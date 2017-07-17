import random

statsSkeleton=[]
statsTable={}
k=0

for i in range (10):
    statsSkeleton.append(i)

statsTable = statsTable.fromkeys(statsSkeleton,0)

for i in range (0,100):
    k=random.randint(0,9)
    statsTable[k] += 1

print(statsTable)

most=max(statsTable.values())
mostitem=[]

for i in range(10):
    if (statsTable[i]==most):
        mostitem.append(i)

print('the number(s) %r appears most often: %d' %(mostitem, most))

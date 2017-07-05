x=1
y=1

matrix = {}

for y in range (1,11):
    for x in range (1,11):
        matrix[y,x] = x * y
        print(x*y, end=' ')
    print('')
    x += 1

print ()
print (matrix[5,6])
print(matrix[1,10])


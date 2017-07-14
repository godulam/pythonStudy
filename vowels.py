# variables section
word=input('please provide string: ')
count=0
vowels=['a','e','i','o','u','y']

# check & count
for i in word.lower():
    if i in vowels:
        count+=1

# output
print('vowels count: ', count)

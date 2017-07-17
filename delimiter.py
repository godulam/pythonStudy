import string

msg=input('please provide elements separated by coma:\n')
words = msg.split(',')
lysta=[]

for i in words:
    lysta.append(i)

lysta=sorted(list(set(lysta)))

print(lysta)

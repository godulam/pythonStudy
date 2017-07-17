import string
import random

# lists containing all letters, digits and symbols
lettersL=(tuple(string.ascii_lowercase))
lettersU=(tuple(string.ascii_uppercase))
digits=(tuple(string.digits))
symbols=(tuple(string.punctuation))

# input
passwordLength=int(input('number of digits of a password(more than or equal 4): '))
password=[]
digitx=[]


# random password generator loop
# creates additional list named digitx and appends
# element from each of the following tuples:
# lettersL, lettersU, digits, symbols
# then it append random value from newly created digitx list
# into password list
for i in range (0,passwordLength-4):
    digitx.append(random.choice(lettersL))
    digitx.append(random.choice(lettersU))
    digitx.append(random.choice(digits))
    digitx.append(random.choice(symbols))
    password.append(random.choice(digitx))
    digitx=[]

# part to make sure that password is STRONK
# adds character from each tuple at the end
# and the shuffles whole password to make sure it's stronk
password.append(random.choice(lettersL))
password.append(random.choice(lettersU))
password.append(random.choice(digits))
password.append(random.choice(symbols))
random.shuffle(password)

#output
print(''.join(password))

person={}
nameInput=0
ageInput=0
iqInput=0

while True:

    nameInput=input('name: ')
    if nameInput=='q':
        break
    ageInput=input('age :')
    iqInput=input('iq: ')

    for i in range(0,2):
        person={'name':nameInput,'age':ageInput,'iq':iqInput}

    print('\n',person['name'],'\n',person['age'],'\n',person['iq'],'\n')

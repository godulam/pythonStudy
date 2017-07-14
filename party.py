david=input('david? (y, n): ')
bruno=input('bruno? (y, n): ')
carlo=input('carlo? (y, n): ')

if david=='y':
    if bruno=='n' and carlo=='n':
        print('Angelo comes!')
    else:
        print('Angelo stays home and plays nintendo')
else:
    print('Angelo stays home and plays nintendo')

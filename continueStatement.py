while True:
    s = input('Enter something (type \'quit\' to quit) : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    print('I don\'t want this text to be prtinted if the length is too small')

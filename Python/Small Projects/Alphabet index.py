'''
while True:
    letter = input('Letter: ')     # Output: 1 (ord() - 64)

    if letter == 'exit':
        exit()

    elif letter >= 'A' and letter <= 'Z':
        print(ord(letter) - 64)
        print('--------------------')

    else:
        print('invalid')
        print('--------------------')

'''


for i in range(32,55204):
    print(str(i) + ':' + chr(i))
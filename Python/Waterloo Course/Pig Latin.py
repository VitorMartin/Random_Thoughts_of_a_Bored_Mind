# Input string for output primeira letra no final, mais 'ay'

while True:

    S = input('Input word for translation to Pi Latin ')

    block = S[1:len(S)]     # onkey
    first = S[0:1]          # m

    print(block+first+"ay")
    print('--------------------')

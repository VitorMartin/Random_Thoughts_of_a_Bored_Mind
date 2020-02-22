# Input several periods for output periods centered in the middle
width = int(input('Length of period: '))

while True:
    line = input('Input line: ')
    L = len(line)

    if line == 'END':
        break

    # Qtde de '.':
    Rperiods = (width - L) // 2
    Lperiods = width - (Rperiods + L)

    print('.' * int(Lperiods) + line + '.' * int(Rperiods))

def check(string):

    # Creating string and list variables
    string = string + ' '
    string_test = string

    # Checking lenght of input
    if len(string) < 20:
        return 'Input too short'
    elif len(string) > 20:
        return 'Input too long'

    # Checking numbers and spaces
    else:
        for i in range(0, 4):
            try:
                int(string_test[0:3])
            except ValueError:
                return print('Input is not all numbers at the', str(i+1)+'º', 'group')
            if string_test[4] != ' ':
                return print('Input is missing a space at the', str(i+1)+'º', 'group')

            string_test = string_test[5:len(string_test)]

    # Checking sum
    lista = []
    for i in range(0, len(string)):
        lista.append(string[i])
    for i in range(0, 4):
        lista.remove(' ')

    soma = 0
    for i in range(0, len(lista)):
        soma += int(lista[i])
    if soma % 10 != 0:
        return 'invalid credit card number'
    else:
        return True

while True:
    inp = input('Input credit card number as #### #### #### #### or "end" to terminate: ')
    #      0123456789012345678
    if inp == 'end':
        break
    print(check(inp))

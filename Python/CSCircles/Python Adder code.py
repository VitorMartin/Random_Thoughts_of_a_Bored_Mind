# Python Adder code

while True:
    # Inputs:
    inp = input('Input sum as a+b ')

    for position in range(0, len(inp)):
        character = inp[position:position + 1]

        if character in '+':
            a = int(inp[0:position])
            b = int(inp[position+1:len(inp)])

            print(a+b)
            print('--------------------')
            break

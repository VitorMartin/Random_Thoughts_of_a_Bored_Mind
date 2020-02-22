while True:

    # Input
    inp = input('Coordenates (x1, y1, x2, y2): ')     # inp = '10, 12, 32, 22'
    comma1 = 0
    comma2 = 0
    comma3 = 0

    # Position of comma1, comma2, comma3
    for i in range(0, len(inp)):
        if inp[i] == ',':
            comma1 = i
            break

    for i in range(comma1 + 1, len(inp)):
        if inp[i] == ',':
            comma2 = i
            break

    for i in range(comma2 + 1, len(inp)):
        if inp[i] == ',':
            comma3 = i
            break

    # Extracting x1, y1, x2, y2:
    x1 = int(inp[0:comma1])
    y1 = int(inp[comma1 + 1:comma2])
    x2 = int(inp[comma2 + 1:comma3])
    y2 = int(inp[comma3 + 1:len(inp) + 1])


    # Calculate distance
    def distance(x1, y1, x2, y2):
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = (a**2 + b**2)**(1/2)
        return c


    # Output
    dist = distance(x1, y1, x2, y2)
    print(dist)
    print('--------------------')
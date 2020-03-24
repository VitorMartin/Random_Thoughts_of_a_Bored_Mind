# Input time and period for output final time: 12:30 + 00:30 = 13:00

while True:
    # Inputs:
    H = input('Initial time: ')
    m = input('Wait for (min): ')

    # Calculation:
    m = (int(H[3:5]) + int(m)) / 60
    H = int(H[0:2]) + m
    m = int(round((H - int(H)) * 60, 0))
    H = int(H)

    # Adding spare 0s and 24 clock:
    if int(H) >= 24:
        H = str(H % 24)

    if int(H) < 10:
        H = '0' + str(H)

    if int(m) < 10:
        m = '0' + str(m)

    # Print:
    print(str(H) + ':' + str(m))
    print('--------------------')

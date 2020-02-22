# FUNCTIONS
def converttodecimal(time):            # 1:9 -> 1.15
    dotposition = 0

    for i in range(0, len(time)):
        if time[i] == ':':
            dotposition = i

    H = int(time[0:dotposition])
    m = int(time[dotposition + 1:len(time)]) / 60
    time = H + m
    return round(time, 10)


def converttoclock(time):              # 1.15 -> 01:09
    H = int(time)
    m = round((time - H) * 60)

    # #Validate the following for 00h00 format
    # if H < 10:
    #     H = '0' + str(H)
    # else:
    #     H = str(H)
    #
    # if m < 10:
    #     m = '0' + str(m)
    # else:
    #     m = str(m)
    # time = H + ':' + m

    # Validate the following for 0h
    if H == 0:
        time = str(m) + 'min'
    elif m == 0:
        time = str(H) + 'h'
    else:
        time = str(H) + 'h' + str(m)

    return time


while True:
    # INPUTS
    inicialT = input('Initial time (##:##): ')
    finalT = input('Final time (##:##): ')

    # Convert inputs to DECIMAL
    inicialT = converttodecimal(inicialT)
    finalT = converttodecimal(finalT)

    # Calculation
    deltaT = finalT - inicialT

    # Convert delta to CLOCK
    deltaT = converttoclock(deltaT)

    # Outputs
    print('Waiting time: ', deltaT)
    print('--------------------')

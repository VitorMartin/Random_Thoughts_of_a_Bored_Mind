while True:
    # Variables:
    eggs = int(input('How many eggs? '))
    carton = int(input('Size of the carton? '))
    crt = eggs // carton
    left = eggs % carton

    # Print:
    if left == 0:          # No eggs left

        if crt > 1:
            print(crt, 'cartons left')

        else:
            print(crt, 'carton left')

    elif crt > 1:          # With eggs left

        if left > 1:
            print(crt, 'cartons and', left, 'eggs remaining')
            print('--------------------')

        else:
            print(crt, 'cartons and', left, 'egg remaining')
            print('--------------------')

    else:

        if left > 1:
            print(crt, 'carton and', left, 'eggs remaining')
            print('--------------------')

        else:
            print(crt, 'carton and', left, 'egg remaining')
            print('--------------------')

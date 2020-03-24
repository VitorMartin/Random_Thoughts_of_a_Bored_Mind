from time import clock
infinite = 2
prime = 1
counter = 0

while True:

    for j in range(1, infinite):
        prime += 1
        infinite += 1
        factors = 0

        for i in range(1, prime + 1):

            if prime % i == 0:
                factors = factors + 1

        if factors <= 2:
            counter += 1
            print(prime, '(' + str(counter) + ' / ' + str(clock()) + ')')

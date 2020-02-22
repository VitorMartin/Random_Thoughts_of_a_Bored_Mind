# Input integer for output numero de fatores e se e primo ou nao

# INPUT
while True:
    n = int(input('Input integer for factorization: '))
    inp = n
    n = abs(n)
    counter = 0


    def factorization():

        global counter
        for a in range(1, n+1):                     # Fatorizacao

            if n % a == 0:

                if inp < 0:
                    print(-a, 'x', int(n / a), '=', -a)
                    counter = counter + 1

                if inp >= 0:
                    print(a, 'x', int(n/a), '=', n)
                    counter = counter + 1

    factorization()

    # RELATORIO
    print('Factors found:', counter)

    if inp > 1:

        if counter == 2:
            print(n, 'is prime')

        elif counter == 1:
            print(n, 'is prime')

    print('--------------------')

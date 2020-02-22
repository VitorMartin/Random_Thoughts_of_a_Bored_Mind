def digito(inp):
    lista = []
    soma = 0
    for i in range(0,3):
        lista.append(inp[i])

    for i in range(0,3):
        soma += int(lista[i])*(i+1)

    print(str(soma)[-1])


inp = input('numero: ')
digito(inp)

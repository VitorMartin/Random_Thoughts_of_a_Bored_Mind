def prod(L):
    number = 1

    for l in L:
        product = number * l
        number = product

    return product


L = [2,3,4]
print(prod(L))
from time import time_ns

def get_list(number):
    '''
    Converts a number into a list of its integers: 123 => [1,2,3]
    '''
    number = str(number)
    lista = []
    for n in number:
        lista.append(int(n))
    return lista
    

def rand():
    '''
    Generates a random integer between 0 and 10: ]0;1)
    '''
    tempo = time_ns()
    lista_tempo = get_list(tempo)
    
    soma = sum(lista_tempo)
    while soma > 10:
        lista_soma = get_list(soma)
        soma = sum(lista_soma)
    
    
    return soma


for i in range(100):
    print(rand())
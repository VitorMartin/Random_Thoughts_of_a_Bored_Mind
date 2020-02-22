from math import *

'''
# 1. 3.8) ––––––––––

inp = input('Numeros (x,y): ')
inp = inp.replace(' ','')
print(inp)

n1 = float(inp[:inp.find(',')])
n2 = float(inp[inp.rfind(',')+1:])

if n1 > n2:
    print(n1, 'é maior')
else:
    print(n2, 'é maior')

'''
'''
# 1. 3.38) ––––––––––

d = float(input('D: '))
q = float(input('Q: '))

if d > 100:
    n = 2
elif d < 50:
    n = 6
else:
    n = 4

s = (4 * q) / (pi * d ** 2)

print('S =', s)

'''
'''
# 1. 3.43) ––––––––––

lista = list()
a = float(input('A: '))
lista.append(a)
b = float(input('B: '))
lista.append(b)
c = float(input('C: '))
lista.append(c)


maior = max(a, b, c)
lista.remove(maior)
menor = min(a, b, c)
lista.remove(menor)
medio = lista.pop()

print(
    str(menor)+'\n'+
    str(medio)+'\n'+
    str(maior)
     )

'''
'''
# 2. ––––––––––––––––

def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 != 0:
            return True
        else:
            if ano % 400 == 0:
                return True
            else:
                return False
    else:
        return False

mes = int(input('Mes: '))
ano = int(input('Ano: '))

if bissexto(ano):
    if mes == 2:
        print('%02d/%04d possui 29 dias' %(mes, ano))
    elif mes == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        print('%02d/%04d possui 31 dias' % (mes, ano))
    else:
        print('%02d/%04d possui 30 dias' % (mes, ano))


else:
    if mes == 2:
        print('%02d/%04d possui 28 dias' % (mes, ano))
    elif mes == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        print('%02d/%04d possui 31 dias' % (mes, ano))
    else:
        print('%02d/%04d possui 30 dias' % (mes, ano))

'''
'''
# 3. ––––––––––––––––

def delta(a, b, c):
    d = b**2-4*a*c
    return d

a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))
d = delta(a, b, c)

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(
        'x1 = %f\n'
        'x2 = %f'
        % (x1, x2)
         )
elif d == 0:
    x = -b / (2 * a)
    print('x = %f' % x)
else:
    print('Delta < 0: nao ha raizes')

'''
'''
# 4. ––––––––––––––––

mm = float(input('Altura da coluna d\'agua: '))
h  = float(input('Duracao media: '))

indice = mm/h

if indice < 3:
    print('Indice normal')
elif 3 <= indice < 8:
    print('Indice critico')
else:
    print('Indice alarmante!')

'''
'''
# 5. ––––––––––––––––

a = float(input('lado 1: '))
b = float(input('lado 2: '))
c = float(input('lado 3: '))

if abs(b-c)< a <b+c and abs(a-c)< b <a+c and abs(a-b)< c <a+b:
    if a==b==c:
        print('Triangulo equilatero')
    elif a==b!=c or a==c!=b or b==c!=a:
        print('Triangulo isoceles')
    elif a!=b!=c:
        print('Triangulo escaleno')
    else:
        print('ERRO: triangulo nao encontrado')
else:
    print('Esse triangulo nao existe')
    
'''
'''
# 6. ––––––––––––––––

a = float(input('lado 1: '))
b = float(input('lado 2: '))
c = float(input('lado 3: '))

if abs(b-c)< a <b+c and abs(a-c)< b <a+c and abs(a-b)< c <a+b:
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        if a == b != c or a == c != b or b == c != a:
            print('Triangulo retangulo isoceles')
        elif a != b != c:
            print('Triangulo retangulo escaleno')
        else:
            print('ERRO: triangulo nao encontrado')
else:
    print('Esse triangulo nao e reto')
    
'''
'''
# 7. ––––––––––––––––
def operacao(a, b, c):
    if c == '+':
        return a + b

    elif c == '-':
        return a - b

    elif c == 'x':
        return a * b

    elif c == '/':
        if b != 0:
            return a / b
        else:
            return 'Divisao por zero'

    else:
        return 'Operador invalido'


a = float(input('Valor 1: '))
b = float(input('Valor 2: '))
c = input('Operacao (+ - x /): ')

print(operacao(a, b, c))

'''
























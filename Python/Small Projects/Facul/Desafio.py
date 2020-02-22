# Lista Desafio

from math import *
from random import randrange

'''
# 1. ––––––––––––––––––––

def area(l, n):
    soma = 0
    for i in range(1, n+1):
        soma += (4/9)**(i-1)

    area = (l**2*sqrt(3)/4) * ( 1 + (soma/3) )

    return area

l = float(input('l: '))
n = int(input('n: '))

print('Area total: %f' % area(l, n))

'''
'''
# 2. –––––––––––––––––––

n = int(input('n: '))

if n < 0:
    exit('n deve ser >= 0')

elif n == 0:
    print('p = -99')

else:
    p = -1/2
    for i in range(2, n+1):
        p += 1 / (2 * i)

    print('p =', p)

'''
'''
# 3. –––––––––––––––––––

def primo(n):

    if n < 0:
        return ('O numero deve ser >= 0')

    limite = ceil(sqrt(n))

    if n == 0 or n == 1:
        return False

    elif n == 2:
        return True

    for i in range(2, limite+1):
        if n % i == 0:
            return False

    return True

n = int(input('Numero: '))
print(primo(n))


'''
'''
# 4. –––––––––––––––––––

a = input('Palavra 1: ')
b = input('Palavra 2: ')
c = input('Palavra 3: ')

if a < b and a < c:
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)

if b < a and b < c:
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)

if c < a and c < b:
    print(c)
    if a < b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

'''
'''
# 5. –––––––––––––––––––

def ContarVogais(s):
    s = s.replace('á', 'a')
    s = s.replace('é', 'e')
    s = s.replace('í', 'i')
    s = s.replace('ó', 'o')
    s = s.replace('ú', 'u')
    s = s.replace('ã', 'a')
    s = s.replace('õ', 'o')
    s = s.replace('à', 'a')
    s = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    return s


s = input('Texto: ')
s = s.lower()
print(ContarVogais(s))

'''
'''
# 6. –––––––––––––––––––

s = 'Ola meu nome é Vitor'
s = s.split()
print(s, type(s))

maior = s[0]

for i in range(len(s)):
    if len(s[i]) > len(maior):
        maior = s[i]

print(maior, '–>', len(maior))

'''
'''
# 7. –––––––––––––––––––

n = int(input('Numero de competidores: '))
PMC = float(input('Padrao Maua de Competitividade: '))
tempo = list()
naopassou = list()
passou = list()
soma = 0

for i in range(1, n+1):
    t = float(input('Tempo do competidor %d: ' % i))
    tempo.append(t)


for i in range(n):
    if tempo[i] >= PMC:
        naopassou.append(tempo[i])
    else:
        passou.append(tempo[i])

for i in range(len(passou)):
    soma += passou[i]

media = soma/len(passou)

print('––––––––––––––––––––––––\n'
      'Media: %.2f\n'
      'Desclassificados: %d\n'
      '––––––––––––––––––––––––'
      % (media, len(naopassou))
     )

'''
'''
# 8. –––––––––––––––––––

def VerificarAnagrama(palavra1, palavra2):
    palavra1 = palavra1.lower()
    print(palavra1)
    lista1 = list()
    for i in range(len(palavra1)):
        lista1.append(palavra1[i])
    lista1.sort()

    palavra2 = palavra2.lower()
    lista2 = list()
    for i in range(len(palavra2)):
        lista2.append(palavra2[i])
    lista2.sort()

    if lista1 == lista2 :
        return True
    else:
        return False


palavra1 = input('Primeira palavra: ')
palavra2 = input('Segunda palavra: ')

print(VerificarAnagrama(palavra1, palavra2))

'''
'''
# 9. –––––––––––––––––––

def categoria(pas, pad):
    if pas < 130 and pad < 85:
        cat = 'Pressao Normal'

    elif pas >= 140 or pad >= 90:
        cat = 'Hipertensao'

    elif 130 <= pas < 139 or 85 <= pad < 89:
        cat = 'Pressao Limitrofe'

    else:
        cat = 'Categoria nao encontrada'

    return cat


N = int(input('Numero de pacientes: '))
aux = []
pacientes = []

for i in range(N):
    PAS = float(input('PAS: '))
    aux.append(PAS)
    PAD = float(input('PAD: '))
    aux.append(PAD)
    pacientes.append(aux)
    aux = []

for i in range(N):
    paciente = pacientes[i]
    PAS = paciente[0]
    PAD = paciente[1]
    print('Categoria: %s' % categoria(PAS, PAD))

'''
'''
# 10. ––––––––––––––––––

text1 = input('Texto 1: ')
text1 = text1.replace(' ', '').lower()
text2 = input('Texto 2: ')
text2 = text2.replace(' ', '').lower()
letras = []

while len(text1) > 0:
    letra = text2.find(text1[0])
    if letra != -1:
        letra = text2[letra]
        letras.append(letra)
        text2 = text2.replace(text1[0], '')
    text1 = text1.replace(text1[0], '')

    print(letras)

'''
'''
# 11. ––––––––––––––––––

def Direito(atraso):
    if atraso <= 60:
        direito = 'Nenhum direito'

    elif 61 <= atraso <= 120:
        direito = 'Facilidade de comunicacao'

    elif 121 <= atraso <= 240:
        direito = 'Alimentacao adequada'

    elif atraso >= 241:
        direito = 'Transporte e hospedagem'

    else:
        direito = 'Tempo de atraso nao reconhecido'

    return direito


def HoraSaida(hora, minutos, atraso):
    minutos /= 60
    hora += minutos
    atraso /= 60
    HoraSaida = hora+atraso

    i = 0
    while HoraSaida >= 24:
        HoraSaida -= 24
        i += 1

    hora = int(HoraSaida)
    minutos = round((HoraSaida - hora) * 60)
    HoraSaida = str(hora) + ':' + str(minutos)

    if i > 0:
        return HoraSaida + ' +' + str(i)

    else:
       return HoraSaida




atraso = int(input('Atraso em minutos: '))
direito = Direito(atraso)
hora = int(input('Hora de saida: '))
minutos = int(input('Minutos de saida: '))
print(HoraSaida(hora, minutos, atraso))

'''

# import random
# n = random.randint(3, 8)          # INPUT tamanho da linha
#
# for i in range(0, n):             # Gera a QTDE de linhas
#     x = 0
#
#     for j in range(n+i, 2*n):     # Gera a linha (1111111)
#         x = (x * 10) + 1
#     print(x)
#



# n = 16
# counter = 1
#
# while counter**2 < n:
#     print(counter**2)
#     counter = counter + 1
#



    # PROGRAMACAO MAIS LEVE ABAIXO. Esta demanda muita MEMORIA!!!
# n = 12
# b = 1
#
# for a in range(1, n+1):
#
#     if a * b == n:
#         print(a, 'x', b, '=', n)
#         continue
#
#     for b in range(1, n+1):
#
#         if a * b == n:
#             print(a, 'x', b, '=', n)
#



    # PROGRAMACAO MAIS LEVE AQUI:
# # Input integer for output numero de fatores e se e primo ou nao
#
# # INPUT
# while True:
#     n = int(input('Input integer for factorization: '))
#     inp = n
#     n = abs(n)
#     counter = 0
#
#
#     def factorization():
#
#         global counter
#         for a in range(1, n+1):                     # Fatorizacao
#
#             if n % a == 0:
#
#                 if inp < 0:
#                     print(-a, 'x', int(n / a), '=', -a)
#                     counter = counter + 1
#
#                 if inp >= 0:
#                     print(a, 'x', int(n/a), '=', n)
#                     counter = counter + 1
#
#     factorization()
#
#     # RELATORIO
#     print('Factors found:', counter)
#
#     if inp >= 0:
#
#         if counter == 2:
#             print(n, 'is prime')
#
#         elif counter == 1:
#             print(n, 'is prime')
#
#     print('......................')
#
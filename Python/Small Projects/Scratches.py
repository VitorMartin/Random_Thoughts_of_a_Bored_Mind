# # Input number of bit to return number of entries and range
#
# while True:
#     bits = int(input('How many bits? '))
#
#     entries = 2**bits
#     negrange = int(-entries/2)
#     posrange = int((entries/2) - 1)
#
#     print(bits, 'bits accept', entries, 'entries, from', negrange, 'to', posrange)
#     print(-negrange == 9223372036854775808)
#     print('--------------------')
#
#
#
#
# # Loop for input seconds
# import time
#
# inp = float(input('Sleep for how many seconds? '))
#
# while time.clock() < inp:
#         t = time.clock()
#         print(t)
#
# print(inp)
#
#
#
#
# for counter in range(10, 15):
#         print("counter is", counter)
# print(counter)
#
#
# for t in range(3,33,3):
#     print(t, end=',')
# print()
#
# from math import pi
#
# print(pi)
#
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# def ExtractAlphanumeric(InputString):
#     from string import ascii_letters, digits
#     return "".join([ch for ch in InputString if ch in (ascii_letters + digits + ' ')])
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

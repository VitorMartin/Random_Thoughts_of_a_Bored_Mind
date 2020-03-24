# Em 10h, v1 -     544.979
#         v2 -   2.166.179 (4*v1)
#         v3 - 246.376.633 (456*v1 114xv2)
from time import clock


def is_n_prime(n):
    limit = n ** (1 / 2)
    if limit - int(limit) == 0:  # n possui raiz
        return False

    else:
        limit = int(limit) + 1
        for i in range(2, limit):
            if n % i == 0:
                return False

        return True


counter = 1
print(2, '(' + str(counter) + ' / ' + str(clock()) + ')')
counter += 1
print(3, '(' + str(counter) + ' / ' + str(clock()) + ')')
counter += 1
print(5, '(' + str(counter) + ' / ' + str(clock()) + ')')
counter += 1
print(7, '(' + str(counter) + ' / ' + str(clock()) + ')')

number = 11
while True:
    if is_n_prime(number) is True:
        counter += 1
        print(number, '(' + str(counter) + ' / ' + str(clock()) + ')')
    number += 2

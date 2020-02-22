# RULES:    1) number is always odd: (1+2n)
#           2) 1 < divisor < number
#           3) Code will divide number by every divisor between 3 and (number-2)
#           4) If no divisor is found, NUMBER IS PRIME

from time import clock

number, counter = 7, 1

print(2, '(' + str(counter) + ' / ' + str(clock()) + ')')
counter += 1
print(3, '(' + str(counter) + ' / ' + str(clock()) + ')')
counter += 1
print(5, '(' + str(counter) + ' / ' + str(clock()) + ')')
counter += 1
divisor = 3

while True:
    if number % divisor != 0:
        divisor = divisor + 2
        if divisor >= number:
            print(number, '(' + str(counter) + ' / ' + str(clock()) + ')')
            counter += 1
            number = number + 2
            divisor = 3
            continue

    else:
        number = number + 2
        divisor = 3

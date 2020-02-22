# list.append(X) adds X to the end of the list
# list.insert(i, X) adds X at position i
# list.extend(L) adds a list L of items to the end
# list.remove(X) removes the first occurence of X
# list.pop(i) deletes & returns item list[i], while list.pop() deletes & returns the last item
# del list[i] deletes the ith item of list (Note this is a "del statement", not a method)
# list.reverse() reverses the list
# list.sort() sorts the list
# Letter case: capitalize, lower, upper, islower, isupper
# Characters: isalpha, isdigit
# Padding: center, ljust, rjust; strip will erase padding
# Substrings: endswith, startswith, find, replace
# Parsing: split, splitlines


# # Changes x for y in a list
# L = [3, 1, 4, 1, 5, 9]
#
# def replace(list, x, y):
#     while list.count(x) > 0:
#         list.insert(list.index(x), y)
#         list.remove(x)
#
#     return list
#
# print('L =', L)
# print(replace(L, 1, 7))


# L = '  3d3  L3  T'
#
# def postalValidate(code):
#     code = code.replace(' ', '') # Apaga os espacos em branco
#
#     if len(code) != 6: # Falso se codigo nao tiver 6 letras
#         return False
#
#     letters = code[0:len(code):2]
#     numbers = code[1:len(code):2]
#     x = letters.isalpha()
#     y = numbers.isdigit()
#
#     if x == False or y == False: # Falso se nao for 'L#L#L#'
#         return False
#
#     # A partir daqui, ja chequei comprimento e forma 'L#L#L#'
#     return code.upper()
#
#
# print(postalValidate(L))



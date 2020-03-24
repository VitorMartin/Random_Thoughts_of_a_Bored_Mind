inp = input('Input as ##.#X: ')
print(inp)

temp = float(inp[0:len(inp)-1])
CF = str.lower(inp[len(inp)-1])

if CF == 'f':
   c = round((temp - 32) * 5/9, 1)
   print(str(c)+'C')

elif CF == 'c':
   f = round((temp * 9/5) + 32, 1)
   print(str(f)+'F')

else:
    print('Incorrect input')
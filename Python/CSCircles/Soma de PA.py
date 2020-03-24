# Write a function naturalNumbers which takes a positive integer n as input,
# and returns a list [1, 2, ...] consisting of the first n natural numbers.

def naturalNumbers(n):
    return list(range(1, n+1))

L = naturalNumbers(int(input('Numero da contagem? ')))
print(L)
print((L[0]+L[len(L)-1])*(L[len(L)-1]/2))

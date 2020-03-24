# As mentioned in lesson 7A, a substring is any consecutive
# sequence of characters inside another string.
# The same substring may occur several times inside the same string:
# for example "assesses" has the substring "sses" 2 times,
# and "trans-Panamanian banana" has the substring "an" 6 times.
# Write a program that takes two lines of input, we call the first needle
# and the second haystack.
#
# Print the number of times that needle occurs as a substring of haystack.

# Variables:
haystack = str(input('Haystack? '))
needle = str(input('Needle? '))
lenhaystack = len(haystack)  # len = 6
counter = 0

for i in range(0, lenhaystack + 1):  # de 0 ate 7
    searchhaystack = haystack[i:i + len(needle)]

    if searchhaystack == needle:
        counter = counter + 1

print('Number of needles in haystack:', counter)

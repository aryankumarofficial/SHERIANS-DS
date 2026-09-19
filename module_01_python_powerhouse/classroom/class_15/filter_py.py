"""
Filter in Python
syntax - filter(fn.,iterable)
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 00]
print(l)

evens = set(filter(lambda x: x % 2 == 0, l))

print(evens)

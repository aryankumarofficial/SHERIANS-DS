"""
Set comprehensions
"""

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 16, 18, 20, 21}

threes = {i for i in s if i % 3 == 0}
print(threes)

# Set
# unique
# only hashable values - can't list and set but tuple
# unordered nature
# s = {10, 20, 30, 40}

# s[1] = 20 # can't do that

# print(s)
# print(hash((1, 2, 3)))

# print(hash(s))


# l = [65, 1, 2, 2, 4, 55, 72, 75, 55, 65]
# s = set(l)
# print(s)

# traversing
# for i in s:
#     print(i)

# s.add(70)

# print(s)

s = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# print(s2 - s)  # s.difference(s2) # Set Difference

# print(s & s2)  # intersection
s2.discard(50)
s2.discard(60)

print(s2.issubset(s))

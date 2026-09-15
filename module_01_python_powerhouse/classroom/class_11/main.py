# List
# Mutable Duplicate Store Everything
# a = [10, True, "Aryan"]
# b = [1, 1, 1, 2, 2, 2, 3]
# c = [1, 2, 3, 4.5, 6]
# print(a)

# l = [10, 20, 30, 40, 50]

# print(l[-1], l[0]) # accessing by idx
# print(l[:3])  # slicing

# l[3] = 41
# print(l)

# reference copy
# a = [10, 20, 30, 40]
# b = a
# b[0] = 90
# print(a, b)

# shallow copy
# a = [10, 20, 30, 40]
# b = a.copy()
# b[0] = 80
# print(a, b)

# import copy
#
# a = [10, 20, 30, 40]
#
# b = copy.deepcopy(a)
# b[0] = 100
#
# print(a, b)

a = [10, 20, 30, 40]

# traversing
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

print(a)
a.append(50)  # adds to the end of the list
# a.clear()
print(a.count(10))
print(a.index(20))

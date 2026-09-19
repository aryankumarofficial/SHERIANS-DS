"""
Dictionary Comprehensions
"""
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# dt = {i: i ** 2 for i in l if i % 2 == 0}
# print(dt)

l1 = ["Aryan", "Kush", "Anish"]
l2 = [22, 24, 26]
mp = dict(zip(l1, l2))

result = {
    i: mp[i]
    for i in mp
    if i[0] == "A"
}
print(mp)
print(result)

# print unique elements in a array
arr = [10, 20, 30, 10, 15, 20, 30, 15, 45, 50, 45, 75, 55, 50, 75]

mp = {}
for i in arr:
    if i in mp.keys():
        mp[i] += 1
    else:
        mp.update([(i, 1)])


print(list(mp.keys()))
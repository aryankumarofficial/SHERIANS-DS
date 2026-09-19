# count frequency of array Elements

arr = [10, 20, 20, 10, 45, 30, 50, 75, 95, 45, 75, 55, 50]

hash_map = {}
for i in arr:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map.update([(i, 1)])

print(hash_map)

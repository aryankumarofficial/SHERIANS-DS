"""
Jewels and Stones
 - count how many stones are also jewels based on given string
"""


# using set
# def num_jewels_in_stones(jewels: str, stones: str) -> int:
#     jewels_set = set()
#     count = 0
#     for jewel in jewels:
#         jewels_set.add(jewel)
#
#     for stone in stones:
#         if stone in jewels_set:
#             count += 1
#     return count
# using hashmap
def num_jewels_in_stones(jewels: str, stones: str) -> int:
    count = 0
    hash_map = dict()
    for stone in stones:
        if stone in hash_map.keys():
            hash_map[stone] += 1
        else:
            hash_map[stone] = 1

    for jewel in jewels:
        if jewel in hash_map.keys():
            count += hash_map[jewel]

    return count


print(num_jewels_in_stones("aA", "aAAbbbb"))

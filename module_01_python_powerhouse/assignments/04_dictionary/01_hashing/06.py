"""
Sum of unique elements
"""


def sum_of_unique_elements(nums: list) -> int:
    mp = {}
    total = 0
    for item in nums:
        if item in mp.keys():
            mp[item] += 1
        else:
            mp[item] = 1

    for item in mp.keys():
        if mp.get(item) == 1:
            total += item
    return total


print(sum_of_unique_elements([1, 2, 3, 2]))
print(sum_of_unique_elements([1, 1, 1, 1, 1]))
print(sum_of_unique_elements([1, 2, 3, 4, 5]))

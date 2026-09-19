"""
Most Frequent Even Elements
"""
from typing import List


def most_freq_even_elements(nums: List[int]) -> int:
    mp = {}
    for i in nums:
        if i % 2 == 0:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
    if not mp:
        return -1

    max_freq = max(mp.values())
    cand = [num for num, freq in mp.items() if freq == max_freq]
    return min(cand)


# result = most_freq_even_elements([0, 1, 2, 2, 4, 4, 1])
# result = most_freq_even_elements([4, 4, 4, 9, 2, 4])
result = most_freq_even_elements([29, 47, 21, 41, 13, 37, 25, 7])
print(result)

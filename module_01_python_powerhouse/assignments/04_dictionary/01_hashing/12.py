"""
Intersection or two arrays
"""
from typing import List


def interset_array(l1: List[int], l2: List[int]) -> list[int]:
    mp = {}
    result = []
    for i in l1:
        if i in mp.keys():
            mp[i] += 1
        else:
            mp[i] = 1
    for i in mp.keys():
        if i in l2:
            result.append(i)

    return result


l1 = [1, 2, 2, 1]
l2 = [2, 2]

print(interset_array(l1, l2))

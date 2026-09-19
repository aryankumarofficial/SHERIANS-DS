"""
Find Duplicate in array using hashSet
    Detect and print the elements which appear more than one in array
"""
from typing import List


def detect_duplicate(nums: List[int]):
    mp = {}
    for i in nums:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    for i in mp:
        if mp[i] > 1:
            print(i)
    else:
        print("No Duplicate Elements found")


detect_duplicate([1, 2, 3, 4, 5, 6])
detect_duplicate([1, 1, 3, 3, 5, 5, 5, 6, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

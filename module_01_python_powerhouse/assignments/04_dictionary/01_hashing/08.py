"""
Check if two strings have same frequency
    compare character frequencies of two strings and check if they match
"""


def string_match_by_freq(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    mp = {}

    for i in str1:
        if i in mp.keys():
            mp[i] += 1
        else:
            mp[i] = 1

    for i in str2:
        if i in mp:
            mp[i] -= 1

    for i in mp:
        if mp[i] != 0:
            return False

    return True


result = string_match_by_freq("aabbcc", "baccab")
print(result)

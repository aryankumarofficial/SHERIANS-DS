"""
Check if Number Has Equal Digit Count and Digit Value 2283
"""


def is_num_equal_freq_index(num: str) -> bool:
    mp = {}
    for i in num:
        if i in mp.keys():
            mp[i] += 1
        else:
            mp[i] = 1
    for i in range(len(num)):
        if mp.get(str(i), 0) == int(num[i]):
            continue
        else:
            return False
    return True


result = is_num_equal_freq_index("1210")
print(result)

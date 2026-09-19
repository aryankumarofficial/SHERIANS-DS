"""
First Letter to appear Twice
    - find the first character that appears twice in a string
"""


def repeated_character(sentence: str) -> str:
    str_hash = {}
    for ch in sentence:
        if ch in str_hash.keys():
            return ch
        else:
            str_hash[ch] = 1

    print(str_hash)
    return None


print(repeated_character("abccbaacz"))
print(repeated_character("abcdd"))

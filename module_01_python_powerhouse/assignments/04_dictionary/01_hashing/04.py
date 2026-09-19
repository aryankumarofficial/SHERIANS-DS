"""
Pangram Check
    verify if a sentence contains every letter of english alphabets at least once
"""


def is_pangram(sentence: str) -> bool:
    sentence_hash = {}
    for char in sentence:
        if char in sentence_hash:
            sentence_hash[char] += 1
        else:
            sentence_hash[char] = 1

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabets:
        if not ch in sentence_hash:
            return False

    return True


print(is_pangram("thequickbrownfoxjumpsoverthelazydog"))
print(is_pangram("leetcode"))

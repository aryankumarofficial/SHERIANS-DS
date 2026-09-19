from typing import List


def merge_list_of_dicts(dict_list: List[dict[str, int]]):
    result = {}
    print(dict_list)
    for d in dict_list:
        result.update(d)
    print(result)


merge_list_of_dicts([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

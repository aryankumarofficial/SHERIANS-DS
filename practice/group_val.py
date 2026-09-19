def group_values_by_key(dict_list):
    result: dict[str, list[int]] = {}
    for d in dict_list:
        for i in d:
            if not i in result:
                result[i] = [d[i]]
            else:
                result[i].append(d[i])
    print(result)


group_values_by_key([{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}])

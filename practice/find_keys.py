def find_keys_recursive(data):
    keys = list()
    for key, value in data.items():
        keys.append(key)
        if isinstance(value, dict):
            keys.extend(find_keys_recursive(value))

    return list(keys)


re = find_keys_recursive({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}})
print(re)

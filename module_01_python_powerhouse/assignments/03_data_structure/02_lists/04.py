# selection sort

def selection_sort(l: list) -> list:
    for i in range(len(l) - 1):
        j = i + 1
        min_idx = i
        for k in range(j, len(l)):
            if l[k] < l[min_idx]:
                min_idx = k

        l[i], l[min_idx] = l[min_idx], l[i]
    return l


my_list = [34, 26, 89, 123, 16, 112, 11]

print(selection_sort(my_list))

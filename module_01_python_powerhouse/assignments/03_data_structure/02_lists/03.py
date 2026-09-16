# Bubble sort

def bubble_sort(l: list) -> list:
    for j in range(len(l) - 1):
        for i in range(len(l) - 1 - j):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l


my_list = [34, 26, 89, 123, 16, 12, 11]

print(bubble_sort(my_list))

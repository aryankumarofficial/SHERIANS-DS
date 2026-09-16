# reverse a list in place

def reverse_list(l: list) -> list:
    n = len(l)
    for i in range(n // 2):
        l[i], l[n - i - 1] = l[n - i - 1], l[i]
    return l


my_list = [10, 20, 30, 40, 50]

print(reverse_list(my_list))

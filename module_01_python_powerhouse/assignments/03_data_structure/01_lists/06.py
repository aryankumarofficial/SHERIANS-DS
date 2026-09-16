# left rotation by K

def rotate_list_left_by_k(l: list, k: int = 1) -> list:
    for i in range(k % len(l)):
        for item in range(len(l) - 1):
            l[item], l[item + 1] = l[item + 1], l[item]

    return l


def rotate_list_right_by_k(l: list, k: int = 1) -> list:
    for i in range(k % len(l)):
        for item in range(len(l) - 1, 0, -1):
            l[item], l[item - 1] = l[item - 1], l[item]

    return l


my_list = [10, 20, 30, 40]

print(rotate_list_right_by_k(l=my_list, k=1))

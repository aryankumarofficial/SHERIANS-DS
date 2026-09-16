# Binary Search

def binary_search_recursive(l: list, target: int, offset: int = 0):
    if not l:
        return
    mid = len(l) // 2
    if l[mid] == target:
        print(f"{target} found at index {mid + offset}")
        return

    elif l[mid] > target:
        binary_search_recursive(l[:mid], target, offset)
    else:
        binary_search_recursive(l[mid + 1:], target, offset + mid + 1)


def binary_search(l: list, target: int):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2

        if l[mid] == target:
            print(f"{target} found at {mid}")
            return
        elif l[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    print("No such element found")


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# binary_search_recursive(my_list, 10)
binary_search(my_list, 10)

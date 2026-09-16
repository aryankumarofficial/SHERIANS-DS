# linear search

def linear_search(l: list, target: int):
    for i in range(len(l)):
        if target == l[i]:
            print(f"{target} found in the List at index {i}")
            break
    else:
        print(f"{target} doesn't exist in the list")


my_list = [10, 95, 20, 15, 65, 1, 45, 77]

linear_search(my_list, 1)
linear_search(my_list, 100)

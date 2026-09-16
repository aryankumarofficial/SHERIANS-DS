# Check if list is sorted (ASC)

def is_list_sorted(input_list: list) -> bool:
    for i in range(len(input_list) - 1):
        if not (input_list[i] < input_list[i + 1]):
            return False
    return True


my_list = [10, 20, 30, 40, 50]
my_list_02 = [10, 20, 30, 40, 50, 15]
my_list_03 = [10, 45, 15, 20, 30, 40, 50]

print(f"The given list is {"sorted" if is_list_sorted(my_list) else "Not sorted"}")
print(f"The given list is {"sorted" if is_list_sorted(my_list_02) else "Not sorted"}")
print(f"The given list is {"sorted" if is_list_sorted(my_list_03) else "Not sorted"}")

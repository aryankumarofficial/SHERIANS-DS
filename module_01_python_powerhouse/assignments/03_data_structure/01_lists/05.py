# Q. Rotate by 1

def rotate_list_left_by_one(input_list: list) -> list:
    for item in range(len(input_list) - 1):
        input_list[item], input_list[item + 1] = input_list[item + 1], input_list[item]
    return input_list


def rotate_list_right_by_one(input_list: list) -> list:
    for item in range(len(input_list) - 1, 0, -1):
        input_list[item], input_list[item - 1] = input_list[item - 1], input_list[item]
    return input_list


my_list = [10, 20, 30, 40]
print(rotate_list_right_by_one(my_list))

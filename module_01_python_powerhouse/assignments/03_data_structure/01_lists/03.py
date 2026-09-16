# Second-Greatest Element

my_list = [50, 10, 20, 455, 95, 30, 36]

largest_num = 0
second_largest_num = 0

for item in my_list:
    if item > largest_num:
        second_largest_num = largest_num
        largest_num = item

    if largest_num > item > second_largest_num:
        second_largest_num = item

print(f"Second Largest Number in the list is {second_largest_num}")

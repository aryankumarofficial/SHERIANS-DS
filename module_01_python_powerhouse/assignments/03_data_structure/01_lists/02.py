# Largest Element with Index

my_list = [10, 20, 4, 40, 90, 110, 85, 15, 75, 36, 95]

largest_num = 0
largest_num_idx = 0

for i in range(len(my_list)):
    if my_list[i] > largest_num:
        largest_num = my_list[i]
        largest_num_idx = i

print(f"The largest number in the list is {largest_num} at index {largest_num_idx}")

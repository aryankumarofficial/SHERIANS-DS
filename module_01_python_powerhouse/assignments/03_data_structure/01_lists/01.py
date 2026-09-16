# Q. Sum and average of list

my_list = [10, 20, 30, 11, 25, 75, 80, 110, 95]

my_list_sum = 0

for item in my_list:
    my_list_sum += item

my_list_avg = my_list_sum // len(my_list)

print(f"Sum of the elements in the list is {my_list_sum}")
print(f"Average of the elements in the list is {my_list_avg}")

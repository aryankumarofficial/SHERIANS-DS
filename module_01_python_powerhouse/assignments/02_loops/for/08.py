# sum up all factors of number

num = int(input("Enter a number:-"))

total = 0
for i in range(1, num + 1):
    if num % i == 0:
        total += i
    else:
        continue

print(f"Sum of the factorials of {num} is {total}")

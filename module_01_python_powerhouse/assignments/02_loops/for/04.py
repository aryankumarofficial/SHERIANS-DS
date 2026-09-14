# total of natural numbers 1 to n

n = int(input("Enter n:-"))
total = 0
for i in range(n + 1):
    total += i

print(f"Sum of first {n} natural numbers is {total}")

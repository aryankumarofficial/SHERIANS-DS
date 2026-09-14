# sum of even and odd in range

n = int(input("Enter n:-"))

odd = 0
even = 0
for i in range(1, n + 1, 2):
    odd += i

print(f"Sum of odd numbers from 1 to {n} is {odd}")

for i in range(0, n + 1, 2):
    even += i

print(f"Sum of even numbers from 1 to {n} is {even}")

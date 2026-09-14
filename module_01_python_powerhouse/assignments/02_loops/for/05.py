# factorial of a number

n = int(input("Enter a number:-"))
fact = 1

for i in range(n, 0, -1):
    fact *= i

print(f"Factorial of {n} is {fact}")

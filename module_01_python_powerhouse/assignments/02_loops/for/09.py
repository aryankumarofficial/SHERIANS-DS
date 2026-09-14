# power calculation (a^b)

base = int(input("Enter base:-"))
exponent = int(input("Enter exponent:-"))

prod = 1
for i in range(exponent):
    prod *= base

print(prod)
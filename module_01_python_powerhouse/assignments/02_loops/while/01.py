# print digits reverse

num = int(input("Enter a number:-"))

while num > 0:
    rem = num % 10
    print(rem)
    num //= 10

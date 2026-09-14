# Automorphic Number

num = int(input("Enter a number:-"))
num_square = num ** 2

while num > 0:
    num_square_digit = num_square % 10
    num_digit = num % 10
    if num_digit != num_square_digit:
        print("Not Automorphic Number")
        break
    num //= 10
    num_square //= 10
else:
    print("Automorphic Number")

# sum of digits

num = int(input("Enter a number:-"))

digits_sum = 0
while num > 0:
    digit = num % 10
    digits_sum += digit
    num //= 10

print(f"Digits sum is {digits_sum}")

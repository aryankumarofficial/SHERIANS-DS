# palindrome number check

num = int(input("Enter a number:-"))

original_num = num
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print("Palindrome" if reversed_num == original_num else "Not Palindrome")

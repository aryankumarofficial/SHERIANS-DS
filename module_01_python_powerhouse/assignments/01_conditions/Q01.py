# Q. compare two numbers - take two user input and determine which is greater - or they are equal

num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))

if num1 > num2:
    print(f"Number {num1} is greater")
elif num1 == num2:
    print(f"Both Number {num1} are equal")
else:
    print(f"Number {num2} is greater")

# Q. Greatest of three numbers - accept three numbers and find the largest among them using nested if else

num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
num3 = int(input("Enter third Number:"))

if num1 > num2:
    if num1 > num3:
        print("First Number is largest")
    else:
        print("Third Number is largest")

elif num1 > num3:
    if num1 > num2:
        print("First Number is largest")
    else:
        print("Second Number is largest")

else:
    if num2 > num3:
        print("Second Number is largest")
    else:
        print("Third Number is largest")

"""
Exception handling
"""
# a = int(input("num1"))
# b = int(input("num2"))
#
# try:
#     print(a / b)
#
# except ZeroDivisionError as err:
#     print("Can't divide by zero")
#
# except Exception as err:
#     print(f"An error occurred as {err}")
# else:
#     print("There was no Errors")
# finally:
#     print("Division completed")
#
# print(a + b)

try:
    age = int(input("enter your age:\t"))
    if age < 18:
        raise Exception("You must be 18")
    print("Access Granted")
except Exception as e:
    print(f"Error {e}")

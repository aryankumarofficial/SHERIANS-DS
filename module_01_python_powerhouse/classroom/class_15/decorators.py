"""
Decorators
"""


#
# def my_decorator(func):
#     def wrapper():
#         print("Hello I will print Before")
#         func()
#         print("Hello, I will print after")
#
#     return wrapper
#
#
# @my_decorator
# def greet():
#     print("Hello")
#
#
# greet()

def decorate(func):
    def wrapper(*args):
        print("your two numbers addition is :")
        func(*args)
        print("Thank you for choosing our service...")

    return wrapper


@decorate
def addition(a, b):
    print(a + b)


addition(10, 99)

# def greet():
#     # print("Hello Greetingş from GSPS")
#     return "Hello Greetingş from GSPS"
#
#
# print(greet())
#
# def addition(a, b):
#     print(a + b)
#
#
# #
# addition(b=12, a=2)  # keyword arguments
# addition(121, 32)
# addition(32, 154)


# def palindrome(num: int) -> bool:
#     reversed_num = 0
#     original_num = num
#     while num > 0:
#         reversed_num = reversed_num * 10 + num % 10
#         num //= 10
#
#     return reversed_num == original_num
#
#
# print(palindrome(121))


def addition(a, b, c):  # default args
    print(a + b + c)


addition(12, c=13, b=20)

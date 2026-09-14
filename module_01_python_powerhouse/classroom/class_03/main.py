from modulefinder import test

print("welcome to the string bootcamp!")

str = "ARYAN"

print(str)  # ARYAN
print(str[0])  # A
print(str[-1])  # N

print(str[-1], str[4])  # N N

str = "ARYAN JI"

print(str[5])  # whitespace
print(str[6])  # J

# slicing
print(str[0 : 4 + 1 : 1])  # ARYAN
print(str[::])  # ARYAN JI

testStr = "Hello I am Data Science Dev"

# only hello
print(testStr[: 4 + 1 :])

# only Data
print(testStr[11:15:])

# only science
print(testStr[16:23:])

age = 21
des = "DS Dev"
print("my age is", age)  # a whitespace is automatically created at the end of str
print(f"Hello my age is {age} and my designation is {des}")  # formated string


# escape sequence

print("Hello my name is Kush\b and my age is 24")  # escape sequence
print(rf"hello \n It's me {age}")  # row string no work of the the escape sequence

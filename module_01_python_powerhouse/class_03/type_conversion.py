a = 23
a = str(a)
print(type(a))

a = "hello"
# a = int(a)  # ValueError: invalid literal for int() with base 10: 'hello'

a = "23"
a = float(23)
print(a)

a = "hello"
a = bool(a)
print(a)

a = 23
a = bool(a)
print(a)

a = ""
a = bool(a)
print(a)

a = 0
a = bool(a)
print(a)


name = input("What is your name?")
print(f"The name is {name.upper()}")

age = int(input("what is your age?"))
print(type(age))
print(f"The age is {age}")

print("ARYAN".count("A"))

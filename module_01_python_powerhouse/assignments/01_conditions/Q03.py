# Q. Gender with case handling -  make the gender check case-insensitive (M, F, m, f all valid) if input invalid print Wrong Input

gender = input("Enter your gender (M, F, m, f)\n\n")

gender = gender.lower()

if gender == "m":
    print("Hello Sir")
elif gender == "f":
    print("Hello Ma'an")
else:
    print("Wrong Input")

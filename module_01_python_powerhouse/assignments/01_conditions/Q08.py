# Q. Leap Year checker - input a year and check weather if it's a leap year or not by using proper rule: divisible by 4; not by 100 unless divisible by 400

year = int(input("Enter a year to check leap year:"))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

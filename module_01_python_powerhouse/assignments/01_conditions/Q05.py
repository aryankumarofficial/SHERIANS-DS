# Q. Voting Eligibility - input name and age. if age>=18 print "Eligible to vote". if not print how many years are left to become eligible

age = int(input("Enter your age:\n\n"))

if age >= 18:
    print("Eligible to vote")
else:
    remaining = 18 - age
    print(f"You will be eligible in next {remaining} years to vote")

# Q. Vowel or consonant - Accept a single alphabet character and check if it's a vowel (a,e,i,o,u). Also Handle Invalid characters

char = input("Enter the alphabet:-")

if char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

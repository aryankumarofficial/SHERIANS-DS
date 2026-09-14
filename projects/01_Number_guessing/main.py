import random

num = random.randint(1, 100)

tries = 0

while True:
    guess = int(input("Guess The Number between 1 to 100:-\n"))
    tries += 1
    if num == guess:
        print(f"Hurray! You Guess the number in {tries} tries\n")
        break
    elif guess > num:
        print(f"Try harder your guess is larger than the number\n")
    else:
        print("Try harder Your Guess is smaller than the number\n")

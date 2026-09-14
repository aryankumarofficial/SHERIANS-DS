# prime number check

num = int(input("Enter a number:-"))

for i in range(2, int(num / 2)):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime ")

# isPrime = True
# count =0
# for i in range(num - 1, 1, -1):
#     if num % i == 0:
#         isPrime = False
#         break
#
# print("Prime" if isPrime else "Not Prime")

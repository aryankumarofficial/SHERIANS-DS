# Q. Shop Discount Calculator - Ask for purchase amount. Apply amount based on threshold eg: above 1K -> 10% above 1500 ->20% print final Bill.

bill = int(input("Enter your final amount:-"))

if 1000 <= bill < 5000:
    discounted = bill * 0.90  # 10% Discount
    print(f"You Got a discount of 10% and your final Bill is ₹{discounted}")
elif bill >= 5000:
    discounted = bill * 0.80  # 20% Discount
    print(f"You Got a discount of 20% and your final Bill is ₹{discounted}")
else:
    print(f"No Discount for you. Your final bill is ₹{bill}")

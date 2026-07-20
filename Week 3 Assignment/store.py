purchase = float(input("Enter total purchase amount: "))
is_loyalty = input("Are you a loyalty member? (yes/no): ")

if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 5
elif purchase < 15000:
    discount = 10
else:
    discount = 20

amountafter_discount = purchase - (purchase * discount / 100)

if is_loyalty == "yes":
    amountafter_discount = amountafter_discount - (amountafter_discount * 5 / 100)

print(f"Final payable amount: NPR {amountafter_discount}")
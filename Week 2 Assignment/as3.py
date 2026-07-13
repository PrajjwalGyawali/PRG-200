first_trekker_fee = float(input("Enter first trekker's fee amount: "))
second_trekker_fee = float(input("Enter second trekker's fee amount: "))
third_trekker_fee = float(input("Enter third trekker's fee amount: "))

total_expense = first_trekker_fee + second_trekker_fee + third_trekker_fee
share_per_person = total_expense / 3

print(f"Total Trip Expense: {total_expense}")
print(f"Each person has to contribute: {share_per_person}")
print(f"First trekker has contributed {first_trekker_fee - share_per_person}")
print(f"Second trekker has contributed {second_trekker_fee - share_per_person}")
print(f"Third trekker has contributed {third_trekker_fee - share_per_person}")
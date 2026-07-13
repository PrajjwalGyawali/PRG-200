basic_salary = float(input("Enter monthly basic salary: "))
income_deduction_percent = float(input("Enter income-related deduction percent: "))

dashain_bonus = basic_salary
income_deduction = dashain_bonus * income_deduction_percent / 100
final_bonus = dashain_bonus - income_deduction

print(f"Dashain Bonus: {dashain_bonus}")
print(f"Income-related Deduction: {income_deduction}")
print(f"Final Take-home Bonus: {final_bonus}")
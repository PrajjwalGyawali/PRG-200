cost_price = float(input("Enter cost price per plate: "))
selling_price = float(input("Enter selling price per plate: "))
plates_sold = int(input("Enter number of plates sold: "))

total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
total_profit = total_revenue - total_cost
profit_margin = total_profit / total_revenue * 100

print(f"Total Revenue: {total_revenue}")
print(f"Total Cost: {total_cost}")
print(f"Total Profit: {total_profit}")
print(f"Profit Margin: {profit_margin:.1f}%")
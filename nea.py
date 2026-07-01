current: float
current = 3000
previous: float
previous= 2000
units_consumed=current-previous
cost = 15* units_consumed
charge:float
charge=0.03 * cost
totalcost= cost + charge
print(totalcost)

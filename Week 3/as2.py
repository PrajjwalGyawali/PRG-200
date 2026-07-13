previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

units = current - previous
rate = 16          
service = 10       

bill = (units * rate) + service

print("Units consumed:", units)
print("Total Bill (NRs):", bill)
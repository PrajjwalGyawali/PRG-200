usd = float(input("Enter USD amount: "))
rate = 152
service = float(input("Enter service rate (%): "))

nrp = usd * rate
deduction = (service / 100) * nrp
net = nrp - deduction

print("NRP earning:", nrp)
print("Deduction:", deduction)
print("Net amount:", net)

print("Yearly deduction:", deduction * 12)
print("Yearly net:", net * 12)

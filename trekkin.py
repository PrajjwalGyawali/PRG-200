price_list = {"yubik":1000,"shirhir":100000,"krish":1000}
total = 0
for name,price in price_list.items():
    total+=price


print(total/len(price_list))

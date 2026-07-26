inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

def process_order(inventory, cart):
    grand_total = 0
    print("---- Bill ----")

    for item, qty in cart.items():
        if qty <= inventory[item]["stock"]:
            price = inventory[item]["price"]
            item_total = price * qty
            grand_total = grand_total + item_total
            inventory[item]["stock"] = inventory[item]["stock"] - qty
            print(f"{item} x{qty} = NPR {item_total}")
        else:
            print(f"Sorry, not enough stock for {item}")

    print("--------------")
    print(f"Grand Total: NPR {grand_total}")

    stock_summary = []
    for item in cart:
        stock_summary.append(f"{item}={inventory[item]['stock']}")
    print("Updated stock: " + ", ".join(stock_summary))

process_order(inventory, cart)
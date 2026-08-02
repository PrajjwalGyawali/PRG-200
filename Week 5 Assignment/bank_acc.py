class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount

    def get_balance(self):
        print(f"{self.name}: NPR {self.balance}")

accounts = [
    ("Ramesh Thapa",  "A001", 5000),
    ("Sunita Karki",  "A002", 0),
    ("Bikash Rai",    "A003", 12000),
]

acc1 = BankAccount(accounts[0][0], accounts[0][1], accounts[0][2])
acc2 = BankAccount(accounts[1][0], accounts[1][1], accounts[1][2])
acc3 = BankAccount(accounts[2][0], accounts[2][1], accounts[2][2])

acc2.deposit(3000)
acc3.withdraw(15000)
acc1.withdraw(2000)

acc1.get_balance()
acc2.get_balance()
acc3.get_balance()
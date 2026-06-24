# Creating an ATM programme 
# Functions : check balance , deposit money , withdraw money , exit.
class ATM:
    def __init__(self):
        self.balance = 0
    def check_balance(self):
        return f"Your current balance is {self.balance}"
    def deposit_money(self,deposit):
        self.balance += deposit
        return f"deposited : {deposit}, current balance: {self.balance}"
    def withdraw_money(self,withdraw):
        if withdraw > self.balance:
            return "insufficient balance"
        else:
            self.balance -= withdraw
            return f"withdrawn : {withdraw}, current balance: {self.balance}"
atm = ATM()
while True:
    print("-------ATM Machine--------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        print(atm.check_balance())
    elif choice == 2:
        amount = float(input("enter amount to deposit: "))
        print(atm.deposit_money(amount))
    elif choice == 3:
        amount = float(input("enter amount to withdraw:"))
        print(atm.withdraw_money(amount))
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else: 
        print("Invalid Choice")
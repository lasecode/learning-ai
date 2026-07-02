import json

class Account:
    def __init__(self, name, acc_number, acc_type):
        self.name = name
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = 0
        self.transaction = []

    def __str__(self):
        return f'{self.name}: {self.acc_number}|{self.acc_type}'

    def deposit(self, amount):
        if amount <= 0:
            print("Transaction is to low")
        else:
            self.balance += amount
            transact = {'name': self.name, 'acc_number': self.acc_number, 'amount': amount, 'balance': self.balance}
            self.transaction.append(transact)
            self.save_transactions()
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            transact = {'name': self.name, 'acc_number': self.acc_number, 'amount': amount, 'balance': self.balance}
            self.transaction.append(transact)
            self.save_transactions()

    def history(self):
        for index, item in enumerate(self.transaction):
            print(f'{index} - {item}')
    
    def save_transactions(self):
        filename = f"{self.acc_number}.json"
        with open(filename, 'w') as f:
            json.dump(self.transaction, f)

    def load_transaction(self):
        try:
            filename = f"{self.acc_number}.json"
            with open(filename, 'r') as f:
                transactions = json.load(f)
            self.transaction.extend(transactions)
            self.balance = self.transaction[-1]['balance']
        except FileNotFoundError:
            print("File not found")

class SavingsAccount(Account):
    def __init__(self, name, acc_number, acc_type, interest_rate):
        super().__init__(name, acc_number, acc_type)
        self.interest_rate = interest_rate 

    def add_interest(self):
        p = self.balance
        r = self.interest_rate
        t = 365
        daily_interest = (p * r)/t
        self.balance += daily_interest
        self.save_transactions()

class CurrentAccount(Account):
    def __init__(self, name, acc_number, acc_type, overdraft_limit):
        super().__init__(name, acc_number, acc_type)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print("Exceeded Overdraft Limit")
        else:
            self.balance -= amount
            transact = {'name': self.name, 'acc_number': self.acc_number, 'amount': amount, 'balance': self.balance}
            self.transaction.append(transact)
            self.save_transactions()

def main():
    print("=== Welcome to Python Bank ===")

    accounts = {}
    

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transaction History")
        print("6. Add_interest")
        print("7. Exit")

        option = input("\nWhat do you want to do: ")
        if option == '1':
            choice = input("\nSavings/Current: ")
            if choice.lower() == 'savings':
                name = input("Enter account holder's name: ")
                acc_number = input("Enter account number: ")
                accounts[acc_number] = SavingsAccount(name, acc_number, interest_rate=0.5, acc_type = 'SavingsAccount')
            elif choice.lower() == 'current':
                name = input("Enter account holder's name: ")
                acc_number = input("Enter account number: ")
                accounts[acc_number] = CurrentAccount(name, acc_number, overdraft_limit=1000, acc_type= 'CurrentAccount')
            else:
                print("Invalid option")
        elif option == '2':
            acc_number = input("Enter account number: ")
            if acc_number in accounts:
                accounts[acc_number].load_transaction()
                print(accounts[acc_number])
            else:
                print("Account doesn't exist")
        elif option == '3':
            try:
                acc_number = input("Enter account number: ")
                amount = int(input("Amount: "))

                if acc_number in accounts:
                    accounts[acc_number].deposit(amount)
                else:
                    print("account does not exist")
            except ValueError:
                print("Invalid Valuetype")
        elif option == "4":
            try: 
                acc_number = input("Enter account number: ")
                amount = int(input("Amount: "))

                if acc_number in accounts:
                    accounts[acc_number].withdraw(amount)
                else:
                    print("account does not exist")
            except ValueError:
                print("Invalid Valuetype")
        elif option == "5":
            acc_number = input("Enter account number: ")
            if acc_number in accounts:
                accounts[acc_number].history()
            else:
                print("account does not exist")
        elif option == "6":
            acc_number = input("Enter Account Number: ")
            if acc_number in accounts: 
                if isinstance(accounts[acc_number], SavingsAccount):
                    accounts[acc_number].add_interest()
                else:
                    print("Only savings accounts earn interest")
            else:
                print("Account Doesn't exist")
        elif option == "7":
            print("Thank you")
            break


    
            
        


                





    





          
        
        

    

    

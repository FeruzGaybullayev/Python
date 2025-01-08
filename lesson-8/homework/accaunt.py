import json
import os

class Account:
    def __init__(self, account_number, name, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        return len(self.accounts) + 1

    def create_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully! Account number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print(f"Successfully deposited {amount}. New balance: {account.balance}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > account.balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                account.balance -= amount
                self.save_to_file()
                print(f"Successfully withdrew {amount}. New balance: {account.balance}")
        else:
            print("Account not found.")

    def save_to_file(self):
        with open('accounts.txt', 'w') as file:
            json.dump({acc_number: acc.__dict__ for acc_number, acc in self.accounts.items()}, file)

    def load_from_file(self):
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as file:
                accounts_data = json.load(file)
                for acc_number, acc_info in accounts_data.items():
                    account = Account(**acc_info)
                    self.accounts[int(acc_number)] = account

def main():
    bank = Bank()
    
    while True:
        print("\n1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == '2':
            account_number = int(input("Enter account number: "))
            bank.view_account(account_number)

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
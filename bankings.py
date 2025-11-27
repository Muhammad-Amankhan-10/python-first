# -----------------------------
# Simple OOP Banking System (Fixed Create Account Logging)
# -----------------------------
import os

class BankAccount:
    accounts = {}   # {username: object}

    def __init__(self, username, password, balance=0):
        self.username = username
        self.__password = password
        self.balance = balance

    def check_password(self, password):
        return self.__password == password

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def show_account_type(self):
        print("This is a normal bank account.")


class SavingAccount(BankAccount):
    def show_account_type(self):
        print("This is a saving account.")


def save_terminal_message(text):
    # Append mode, current folder me file
    filepath = os.path.join(os.getcwd(), "termnal_log.txt")
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(text + "\n")


class BankSystem:
    def __init__(self):
        self.logged_in_user = None

    def create_account(self):
        print("\n--- Create Account ---")
        save_terminal_message("--- Create Account ---")

        username = input("Enter username: ")
        save_terminal_message(f"Enter username: {username}")

        password = input("Enter password: ")

        try:
            balance = int(input("Enter initial balance: "))
        except ValueError:
            print("Balance must be a number!")
            save_terminal_message("❌ Invalid balance input!")
            return

        save_terminal_message(f"Enter initial balance: {balance}")

        acc_type = input("Account type (normal/saving): ").lower()
        save_terminal_message(f"Account type: {acc_type}")

        if username in BankAccount.accounts:
            print("Username already exists!")
            save_terminal_message("❌ Username already exists!")
            return

        if acc_type == "saving":
            user = SavingAccount(username, password, balance)
        else:
            user = BankAccount(username, password, balance)

        BankAccount.accounts[username] = user
        print("Account created successfully!")
        save_terminal_message(f"✅ Account created successfully: {username}")


    def login(self):
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username not in BankAccount.accounts:
            print("User not found!")
            return

        user = BankAccount.accounts[username]

        if user.check_password(password):
            self.logged_in_user = user
            print(f"Logged in as {username}")
        else:
            print("Wrong password!")

    def logout(self):
        if self.logged_in_user:
            print(f"User {self.logged_in_user.username} logged out.")
            self.logged_in_user = None
        else:
            print("No user is logged in.")

    def show_account(self):
        if self.logged_in_user:
            print("\n--- ACCOUNT DETAILS ---")
            print("Username:", self.logged_in_user.username)
            print("Balance:", self.logged_in_user.balance)
            self.logged_in_user.show_account_type()
        else:
            print("Please login first.")

    def menu(self):
        while True:
            print("\n===== BANK MENU =====")
            print("1. Create Account")
            print("2. Login")
            print("3. Show Account")
            print("4. Deposit")
            print("5. Withdraw")
            print("6. Logout")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.show_account()
            elif choice == '4':
                if self.logged_in_user:
                    amt = int(input("Enter amount: "))
                    self.logged_in_user.deposit(amt)
                else:
                    print("Login required!")
            elif choice == '5':
                if self.logged_in_user:
                    amt = int(input("Enter amount: "))
                    self.logged_in_user.withdraw(amt)
                else:
                    print("Login required!")
            elif choice == '6':
                self.logout()
            elif choice == '7':
                print("Exiting system...")
                break
            else:
                print("Invalid choice.")


# -------------- RUN SYSTEM --------------
bank = BankSystem()
bank.menu()

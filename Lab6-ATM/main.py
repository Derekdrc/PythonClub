"""
name: Derek D'Arcy
Description: This program simulates an ATM 
"""

from bank_account import BankAccount
import os


def main():
    account = BankAccount()
    menu(account)


def menu(account):
    """Menu Displays the user's choices to use the ATM"""
    while True:
        os.system("cls")
        display_menu()
        user_choice = int(input("Please enter the number for your desired option (1 - 5): "))
        while user_choice not in range(1, 6):
            display_menu()
            user_choice = int(
                input("That was not an available choice. Please enter the number for your desired option (1 - 5): "))
        if user_choice == 1:
            balance_inquiry(account)
        elif user_choice == 2:
            deposit(account)
        elif user_choice == 3:
            withdraw(account)
        elif user_choice == 4:
            number_transactions(account)
        elif user_choice == 5:
            break
        input("Press any key to continue")


def display_menu():
    print("Please enter the number for your desired option")
    print("1. Balance Inquiry")
    print("2. Make a Deposit")
    print("3. Make a Withdrawl")
    print("4. Display Number of Transactions")
    print("5. Exit")
    print()


def balance_inquiry(account: BankAccount):
    print(f"The balance of the account is ${account.get_balance():.2f}")


def deposit(account: BankAccount):
    account.deposit()


def withdraw(account: BankAccount):
    account.withdraw()


def number_transactions(account: BankAccount):
    print(f"There has been {account.get_transaction_count()} transactions")


if __name__ == "__main__":
    main()

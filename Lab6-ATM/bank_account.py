"""
name: Derek D'Arcy
Description: This file is the class for the bank account
"""


class BankAccount:
    def __init__(self) -> None:
        self._balance = 1000
        self._transaction_count = 0

    def deposit(self):
        deposit_amount = int(input("Please enter how much you would like to deposit: $"))
        self._balance = self._balance + deposit_amount
        self._transaction_count += 1

    def withdraw(self):
        while True:
            withdraw_amount = int(input("Please enter how much you wish to withdrawl. Amount must be in denominations of $10 and less than account balance: "))
            if withdraw_amount % 10 != 0 or withdraw_amount > self._balance:
                print("The amount withhdrawn needs to be in denominations of 10 and less than the available balance. ")
                withdraw_amount = int(input("Please enter how much you wish to withdrawl. Amount must be in denominations of $10 and less than account balance: "))
            else:
                break
        self._balance = self._balance - withdraw_amount
        self._transaction_count += 1

    def get_balance(self):
        self._transaction_count += 1
        return self._balance

    def get_transaction_count(self):
        return self._transaction_count

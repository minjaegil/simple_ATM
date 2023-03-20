class Account:
    def __init__(self, account_name, balance):
        self._balance = balance
        self._accountName = account_name

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("ERROR: NOT ENOUGH BALANCE")
            return False
        self._balance -= amount
        return True

    def get_account_name(self):
        return self._accountName


class AccountsDatabase:
    def __init__(self):
        # [key]: Card object
        # [value]: List of Account object
        self._myAccounts = {}

    def add_account(self, card, account):
        if card not in self._myAccounts:
            self._myAccounts[card] = [account]
        else:
            self._myAccounts[card].append(account)

    # Returns list of Account objects of selected card
    def get_accounts(self, card):
        return self._myAccounts[card]

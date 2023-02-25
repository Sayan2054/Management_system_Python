class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.number] = account

    def get_account(self, number):
        return self.accounts.get(number)

class Account:
    def __init__(self, number, owner, balance=0):
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient balance')
        self.balance -= amount

# Test the classes
bank = Bank('MyBank')
account1 = Account('123', 'Alice')
account2 = Account('456', 'Bob', 1000)
bank.add_account(account1)
bank.add_account(account2)

print(f'{bank.name} account holders:')
for number, account in bank.accounts.items():
    print(f'{account.owner} ({number}): {account.balance}')
print()

account1.deposit(500)
account2.withdraw(200)
print(f'New balances:')
for number, account in bank.accounts.items():
    print(f'{account.owner} ({number}): {account.balance}')

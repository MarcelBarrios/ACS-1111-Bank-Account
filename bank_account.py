# import code to be able to create a random account number
import random
import string

# Create blueprint to create a new bank account
class BankAccount:

    # Create all of the following below
    def __init__(self, full_name, account_number, balance, type):
        # define the name of the owner of the accounr
        self.full_name = full_name
        # define the unique account number of the owner
        self.account_number = account_number if account_number else ''.join(random.choices(string.digits, k=8))
        # define the balance of money in the account, it should start with 0
        self.balance = balance if balance else 0
        # type of account
        self.type = type
        # routing number
        self.routing_number = 12341234


        # if type is equal to savings then add interest, else do nothing
        if self.type == "savings":
            self.balance += balance * 0.01
        else:
            pass

    # add money to the account
    def deposit(self, amount):
        # add amount to balance
        self.balance += amount
        # say amount deposited and new balance
        print(f"Amount deposited: ${amount:,.2f} new balance: ${self.balance:,.2f}")

    # withdraw money from the account
    def withdraw(self, amount):
        # substract ammount from account
        self.balance -= amount
        # if amount is more than balance say you have insufficient funds and charge $10 as overdraft fee
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
            # say new balance
            print(f"New balance: ${self.balance:,.2f}")
            return
        # say amount withdrawn and new balance
        print(f"Amount withdrawn: ${amount:,.2f} new balance: ${self.balance:,.2f}")

    # get balance
    def get_balance(self):
        # say balance
        print(f"Hello {self.full_name}, your balance is ${self.balance:,.2f}")
        # give balance
        return self.balance

    # add interest
    def add_interest(self):
        # add monthly interest to the balance
        self.balance += self.balance *  0.00083 
    
    # print statement
    def print_statement(self):
        # say name, acount number sensitized, routing number, balance in currency format
        account_number_sensitized = "*" * 4 + str(self.account_number)[4:]
        print(f"""{self.full_name}\nAccount No: {account_number_sensitized}
Routing No: {self.routing_number}\nBalance: ${self.balance:,.2f}""")
        
# create blueprint to create a bank
class Bank:
    # create a empty group for future bank accounts
    def __init__(self):
        self.bank_accounts = []

    # add bank account
    def create_account(self, full_name, account_number, balance, type):
        # add bank account to the the bank group
        self.bank_accounts.append(BankAccount(full_name, account_number, balance, type))

    # deposit to account
    def deposit(self, amount, account_number):
        # for every account in group of accounts
        for account in self.bank_accounts:
            # if account number match
            if account.account_number == account_number:
                # add amount to account
                account.balance += amount
            # else say account does not exist
            else:
                print("Sorry, that account does not exist.")

    # withdraw from account
    def withdraw(self, amount, account_number):
        # for each account in group of accounts
        for account in self.bank_accounts:
            # if account numbers match
            if account.account_number == account_number:
                # reduce balance of the account by amount
                account.balance -= amount

    # transfer money from an account to another account
    def transfer(self, amount, account_from, account_to):
        # for every account in group of accounts
        for account1 in self.bank_accounts:
            # if account numbers match
            if account1.account_number == account_from:
                # if balance of account is bigger than amount
                if account1.balance >= amount:
                    # for each account in group of accounts
                    for account2 in self.bank_accounts:
                        # if account number to deposit to match account number
                        if account2.account_number == account_to:
                            # reduce balance of the account deposit from by amount
                            account1.balance -= amount
                            # add amount to balance of the account to deposit
                            account2.balance += amount
                # else say insufficient funds
                else:
                    "Insufficient funds"

    # say statement of desired account
    def statement(self, account_number):
        # for each account in group of accounts
        for account in self.bank_accounts:
            # if account number matches
            if account.account_number == account_number:
                # say statement of desired account
                account.print_statement()
            # else if account doesn't exist
            else:
                # say account does not exist
                print("Account does not exist.")

# create first example acconout
marhia_account = BankAccount("Marhia Johns", 0, 1000, "savings")
# marhia_account.print_statement()
# print(marhia_account.account_number)

# create second example acconout
hans_account = BankAccount("Hans Lahm", 0, 500, "checking")
# hans_account.print_statement()
# print(hans_account.account_number)

# create third example acconout 
Sarah_account = BankAccount("Sarah Abdul", 0, 5000, "savings")
# Sarah_account.print_statement()
# print(Sarah_account.account_number)

# create another account. set his name to Mitchell, and his account number to 03141592
mitchell_account = BankAccount("Mitchell Hudson", f"{3141592:08}", 0, "checking" )

# deposit $400,000 to Mitchell account 
mitchell_account.deposit(400000)

# say his statement
mitchell_account.get_balance()

# add interest to his account
mitchell_account.add_interest()

# say his statement
mitchell_account.print_statement()

# make a withdrawl of $150 from Mitchell's account
mitchell_account.withdraw(150)

# say his statement
mitchell_account.print_statement()

# bank list
bank = [mitchell_account, Sarah_account, hans_account, marhia_account]

# go over all accounts in bank and add interest to each.
def add_interst_loop(bank):
    for account in bank:
        account.add_interest()

# executing code adding interest to each account
add_interst_loop(bank)

mitchell_account.print_statement()

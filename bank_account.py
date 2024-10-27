# import code to be able to create a random account number
import random
import string

# Create blueprint to create a new bank account
class BankAccount:

    # Create all of the following below
    def __init__(self, full_name, account_number, balance):
        # define the name of the owner of the accounr
        self.full_name = full_name
        # define the unique account number of the owner
        self.account_number = account_number if account_number else ''.join(random.choices(string.digits, k=8))
        # define the balance of money in the account, it should start with 0
        self.balance = balance

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
        routing_number = 12341234
        account_number_sensitized = "*" * 4 + str(self.account_number)[3:]
        print(f"""{self.full_name}\nAccount No: {account_number_sensitized}
Routing No: {routing_number}\nBalance: ${self.balance:,.2f}""")

# create first example acconout
marhia_account = BankAccount("Marhia Johns", 0, 1000)

# create second example acconout
hans_account = BankAccount("Hans Lahm", 0, 500)

# create third example acconout 
Sarah_account = BankAccount("Sarah Abdul", 0, 5000)


# create another account. set his name to Mitchell, and his account number to 03141592
mitchell_account = BankAccount("Mitchell Hudson", 3141592, 0 )

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

# import code to be able to create a random account number
import uuid

# Create blueprint to create a new bank account
class BankAccount:

    # Create all of the following below
    def __init__(self, full_name, account_number, balance):
        # define the name of the owner of the accounr
        self.full_name = full_name
        # define the unique account number of the owner
        self.account_number = account_number
        # define the balance of money in the account, it should start with 0
        self.balance = balance

    # add money to the account
        # add amount to balance
        # say amount deposited and new balance

    # withdraw money from the account
        # substract ammount from account
        # if amount is more than balance say you have insufficient funds and charge $10 as overdraft fee
            # say new balance
        # say amount withdrawn and new balance

    # get balance
        # say balance
        # give balance

    # add interest
        # add monthly interest to the balance

    # print statement
        # say name, acount number sensitized, routing number, balance in currency format

# create first example acconout

# create second example acconout

# create third example acconout 

# create another account 
    # set his name to Mitchell, and his account number to 03141592

# deposit $400,000 to Mitchell account 

# say his statement

# add interest to his account

# say his statement

# make a withdrawl of $150 from Mitchell's account

# say his statement
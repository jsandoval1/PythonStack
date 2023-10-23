class BankAccount:
    all_instances = []
    
    def __init__(self, username, int_rate, balance=0):
        self.username = username 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        # print(f"{self.username}'s new current balance is 0") ****************** SLASHED THESE OUT BECAUSE IT WAS MESSING WITH USER CLASS
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            # print(f"{self.username} withdrew ${amount}. New balance: ${self.balance}") ****************** SLASHED THESE OUT BECAUSE IT WAS MESSING WITH USER CLASS
        else:
            self.balance -= 5
            print(f"Oh no! Insufficient funds: Charging a $5 fee. New balance: ${self.balance}")
        return self
    
    def display_account_info(self):
        print(f"Username: '{self.username}' has an interest rate of {self.int_rate}% , and balance of ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(f"{self.username}'s current account balance with interest rate of {self.int_rate}% is ${self.balance}")
        else: 
            print(f"{self.username}, your account balance is negative")
        return self

    @classmethod
    def print_instances(cls):
        for instance in cls.all_instances:
            instance.display_account_info()
            print("")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Dictionary to store multiple accounts

    def create_account(self, account_name, int_rate, balance=0):
        self.accounts[account_name] = BankAccount(self.name, int_rate, balance)
        print(f"Account '{account_name}' created for {self.name} with initial balance ${balance}")

    def make_deposit(self, account_name, amount):
            self.accounts[account_name].deposit(amount)
            print(f"{self.name} deposited ${amount} into account '{account_name}'")

    def make_withdrawal(self, account_name, amount):
            self.accounts[account_name].withdraw(amount)
            print(f"{self.name} withdrew ${amount} from account '{account_name}'")

    def display_user_balance(self, account_name):
            print(f"{self.name}'s account balance in account '{account_name}' is ${self.accounts[account_name].balance}")

    def transfer_money(self, amount, other_user, from_account, to_account):
        if from_account in self.accounts and to_account in other_user.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].withdraw(amount)
                other_user.accounts[to_account].deposit(amount)
                print(f"{self.name} transferred ${amount} from account '{from_account}' to {other_user.name}'s account '{to_account}'")
            else:
                print(f"Insufficient funds in account '{from_account}' for {self.name}")

# Creating User instances
user1 = User("Matt Rafferty", "mrafferty@codojo.com")
user2 = User("Dylan Cody", "dcody@codojo.com")
print("")

print("-----------------------------")
# Creating BankAccount instances for users
user1.create_account("Savings", 0.2, 0)
user1.create_account("Checking", 0.5, 0)

user2.create_account("Savings", 0.2, 0)
user2.create_account("Checking", 0.5, 0)
print("")

print("-----------------------------")
# Making deposits and withdrawals for users
    # USER 1
user1.make_deposit("Savings", 100)
user1.make_withdrawal("Savings", 20)
user1.display_user_balance("Savings")
print("")
user1.make_deposit("Checking", 300)
user1.make_withdrawal("Checking", 0)
user1.display_user_balance("Checking")

print("------------------")
    # USER 2
user2.make_deposit("Savings", 100)
user2.make_withdrawal("Savings", 0)
user2.display_user_balance("Savings")
print("")
user2.make_deposit("Checking", 300)
user2.make_withdrawal("Checking", 0)
user2.display_user_balance("Checking")
print("")

print("-----------------------------")
# Transferring money between users from one account to another 
user1.transfer_money(20, user2, "Savings", "Checking") 
print("")

print("-----------------------------")
# Displaying user balances
user1.display_user_balance("Savings")
user1.display_user_balance("Checking")
user2.display_user_balance("Savings")
user2.display_user_balance("Checking")
print("")

# # # Maniupulate Output
# John = BankAccount("JohnSandoval",0.2, 0) 
# Jamie = BankAccount("JamieLian", 0.5, 0)
# Trevor = BankAccount("TrevorHaddad", 0.3, 0)
# # # These lines are to create two instances of the BankAccount class with different usernames, interest rates, and initial balances.
# # # (I started messing around and testing class methods with an extra person.)
# print("-----------Bank Account Print Instances from Class Method---------------")
# print("")

# # # This line is to address the class method
# print("----------------User Example using the methods (defs)-------------------------------")
# print("")
# John.deposit(500).deposit(1000).deposit(500).withdraw(200).yield_interest()
# print("")
# print("----------------User Example using the methods (defs)-------------------------------")
# print("")
# Jamie.deposit(500).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(10000).yield_interest()
# print("")
# print("-----------------------------------------------")


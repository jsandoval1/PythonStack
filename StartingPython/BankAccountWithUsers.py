class BankAccount:
    all_instances = []

    
    def __init__(self, username, int_rate, balance=0):
        self.username = username 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)

    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.username}'s new current balance is {self.balance}")
        return self
    
    
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f"{self.username}'s withdrew ${amount}. New balance: ${self.balance}")
        else:
            self.balance -= 5
            print(f"Oh no! Insufficient funds: Charging a $5 fee. New balance: ${self.balance}")
        return self
    

    def display_account_info(self):
        print(f"Username: '{self.username}' has an interest rate of {self.int_rate}% , and balance of {self.balance}")
        return self
        

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(f"{self.username}'s current account balance with interest rate of {self.int_rate}% is {self.balance}")
        else: 
            print(f"{self.username}, your account balance is negative")
        return self

    @classmethod
    def print_instances(cls):
        for instance in cls.all_instances:
            instance.display_account_info()
            print("")


# Maniupulate Output
John = BankAccount("JohnSandoval",0.2, 0)
Jamie = BankAccount("JamieLian", 0.5, 0)
Trevor = BankAccount("TrevorHaddad", 0.3, 0)
# These lines are to create two instances of the BankAccount class with different usernames, interest rates, and initial balances.
# (I started messing around and testing class methods with an extra person.)
print("-----------Bank Account Print Instances from Class Method---------------")
print("")
BankAccount.print_instances()
# This line is to address the class method
print("----------------User Example using the methods (defs)-------------------------------")
print("")
John.deposit(500).deposit(1000).deposit(500).withdraw(200).yield_interest()
print("")
print("----------------User Example using the methods (defs)-------------------------------")
print("")
Jamie.deposit(500).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(10000).yield_interest()
print("")
print("-----------------------------------------------")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    print(self.account.balance)		# or access its attributes
    pass



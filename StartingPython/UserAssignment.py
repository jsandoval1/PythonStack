class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # the status is set to False by default
        self.is_member = False
        # the count is set to 0 by default
        self.gold_card_points = 0

    def display_info(self):
        print("Name:", self.first_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Member Status:", "Yes" if self.is_member else "No")
        print("Gold Card Points:", self.gold_card_points)
        return self  # Return self for method chaining

    def enroll(self):
        self.is_member = True
        self.gold_card_points = 200
        return self  # Return self for method chaining

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{self.first_name} has {amount} points spent. They have {self.gold_card_points} left over. ")
        else:
            print(f"{self.first_name} wants to spend {amount} but has insufficient points. This user currently has {self.gold_card_points} available points.")
        return self  # Return self for method chaining

# Creating an instance of the User class
user1 = User("John", "Sandoval", "jsandoval@codojo.com", 23)
user2 = User("Trevor", "Haddad", "thaddad@codojo.com", 24)
user3 = User("Matt", "Rafferty", "mrafferty@codojo.com", 24)
user4 = User("Dylan", "Cody", "dcody@codojo.com", 28)

# Signing Up the user and updating the information (This will make "is_member" True and grant 200 points.)
user1.enroll()
user2.enroll()
user3.enroll()
user4.enroll()

# Displaying the user information
# Spending points and updating user information
# user1.display_info()
# user1.spend_points(50)
# print("")
# user2.display_info()
# user2.spend_points(80)
# print("")
# user3.display_info()
# user3.spend_points(40)
# print("")
# user4.display_info()
# user4.spend_points(250)
# print("")

user1.display_info().enroll().spend_points(50)
print("")
user2.display_info().enroll().spend_points(80)
print("")
user3.display_info().enroll().spend_points(40)
print("")
user4.display_info().enroll().spend_points(250)
print("")
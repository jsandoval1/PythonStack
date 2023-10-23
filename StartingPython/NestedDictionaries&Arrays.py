# Part One:
print("")
print("Part One")
print("")
# 1- Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# 2- Change the last_name of the first student from 'Jordan' to 'Bryant'
# 3- In the sports_directory, change 'Messi' to 'Andres'
# 4- Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# print("-------------------------------------")

x[1][0]=15
print(x)

# print("-------------------------------------") 

students[1]['first_name'] = "Bryant"
print(students)

# print("-------------------------------------")

sports_directory ['soccer'][0] = "Andres"
print(sports_directory)

# print("-------------------------------------")

z[0]['y']=30
print(z)

print("-------------------------------------")
print("-------------------------------------")

# Part 2:
print("")
print("Part Two")
print("")
# Create a function iterateDictionary (some_list) that, given a list of 
# dictionaries, the function loops through each dictionary in the list 
# and prints each key and the associated value. For example, given 
# the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - "+students[i]['first_name']+", last_name - "+students[i]['last_name'])
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

print("-------------------------------------")
print("-------------------------------------")

# Part 3:
print("")
print("Part Three")
print("")
# Create a function iterateDictionary2(key_name, some_list) that, given a list 
# of dictionaries and a key name, the function prints the value stored in that 
# key for each dictionary. 
    # For example, iterateDictionary2('first_name', students) should output:
    # Michael
    # John
    # Mark
    # KB
        # And iterateDictionary2('last_name', students) should output:
        # Jordan
        # Rosales
        # Guillen
        # Tonel
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name',students)
# iterateDictionary2('last_name',students)
def iterateDictionary3(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary3('last_name',students)


print("-------------------------------------")
print("-------------------------------------")


# Part4:
print("")
print("Part Four")
print("")
# Create a function printInfo(some_dict) that given a dictionary whose values are 
# all lists, prints the name of each key along with the size of its list, and then 
# prints the associated values within each key's list. 
#     For example:
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for name in some_dict:
        print(len(some_dict[name]),name)
        for i in range(len(some_dict[name])):
            print(some_dict[name][i])
        print("")

printInfo(dojo)
        # output:
        # 7 LOCATIONS
        # San Jose
        # Seattle
        # Dallas
        # Chicago
        # Tulsa
        # DC
        # Burbank
                # 8 INSTRUCTORS
                # Michael
                # Amy
                # Eduardo
                # Josh
                # Graham
                # Patrick
                # Minh
                # Devon


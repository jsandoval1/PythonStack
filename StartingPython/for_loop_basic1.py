# Part 1: Print all integers from 0 to 150.
for number in range(150):
    print(number)

# Part 2: Print all the multiples of 5 from 5 to 1,000
for number in range(5,1500,5):
    print(number)

# Part 3: Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def change_labels():
    for numbers in range (1,100):
        if numbers % 5 == 0:
            print ('Coding')
        if numbers % 10 == 0:
            print ('Dojo')
change_labels()

# Part 4: Add odd integers from 0 to 500,000, and print the final sum.
SumOfOdds = 0
for number in range(0, 500000):
    if(number % 2 != 0):
        print("{0}".format(number))
        SumOfOdds = SumOfOdds + number
print(SumOfOdds)

# Part 5: Print positive numbers starting at 2018, counting down by fours.
for numbers in range(2018, 0, -4):
    print(numbers)

# Part 6:  Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print 
# only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop 
# should print 3, 6, 9 (on successive lines)
def DivisibleByMultCountDown(lowNum, highNum, mult):
    for i in range (lowNum, highNum):
        if i % mult == 0:
            print (i)
DivisibleByMultCountDown(1, 50, 4)
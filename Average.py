average = 0
total = 0
howManyEntered = 0
howMany = int (input("How many testscores would you like to average?"))
while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total= total + testScore
    howManyEntered = howManyEntered +1
average = total/ howManyEntered
print("The average for the test scores you entered is:", average )


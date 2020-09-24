#Exercise 04: Loops
#Author: Marcello Pietro Vendruscolo

def printEvenNumbersBetween(begin, end):
    print("Even numbers between {begin} and {end}:".format(begin=begin, end=end))
    for number in range(begin, end+1, 2):
        if(number != 40):
            print(number, end =" ")
        else:
            print(number)

def printFormattedTableOfNumbersBetween(begin, end):
    print("Numbers {begin} to {end}:".format(begin=begin, end=end))
    while begin <= end:
        for rows in range(1, 11):
            for columns in range (1, 11):
                print('{number:>2}'.format(number=begin), end=" ")
                begin = begin + 1
            print("")
        

def printSquaredNumber():
    number_str = input("Give a number: ")
    number = int(number_str)
    while number != 0:
        print("The square of {input} is {square}".format(input=number, square=number**2))
        number_str = input("Give a number: ")
        number = int(number_str)
    print("You entered zero.")

printEvenNumbersBetween(0,40)
printFormattedTableOfNumbersBetween(1,100)
printSquaredNumber()
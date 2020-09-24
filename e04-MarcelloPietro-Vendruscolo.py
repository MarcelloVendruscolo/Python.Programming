#Exercise 04: Loops
#Author: Marcello Pietro Vendruscolo

def evenNumbersBetween(first_number, last_number):
    print("Even numbers between {begin} and {end}:".format(begin=first_number, end=last_number))
    number = first_number
    if (number % 2 != 0):
        number = number + 1
    while (number <= last_number):
        print(number, end = " ")
        number = number + 2
    print("")

def formattedTableOfNumbersBetween(first_number, last_number):
    print("Numbers {begin} to {end}:".format(begin=first_number, end=last_number))
    ncols = 10
    if ((last_number - first_number + 1) % 2 == 0):
        nrows = last_number // 10
    else:
        nrows = ((last_number - first_number) // 10) + 1
    number = first_number
    for rows in range (1, nrows + 1):
        for columns in range (1, ncols + 1):
            if (number <= last_number):
                print('{number:>2}'.format(number=number), end=" ")
                number = number + 1
        print("")

def squareOf(a_number):
    print("The square of {input} is {square}".format(input=a_number, square=a_number**2))
    
first_number = 0
last_number = 40
evenNumbersBetween(first_number, last_number)

first_number = 1
last_number = 100
formattedTableOfNumbersBetween(first_number, last_number)

input_string = input("Give a number: ")
a_number = int(input_string)
while a_number != 0:
    squareOf(a_number)
    input_string = input("Give a number: ")
    a_number = int(input_string)
print("You entered zero.")
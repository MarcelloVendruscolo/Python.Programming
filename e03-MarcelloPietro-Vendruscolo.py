#Exercise 03: Conditionals
#Author: Marcello Pietro Vendruscolo

def isThisNumberZero(a_number):
    if (a_number == 0):
        print("The number you entered equals zero")
    else:
        print("The number you entered does not equal zero")

def largestOfTwoFloats(first_float, second_float):
    if (first_float >= second_float):
        string_printOut = "{float:f} is the largest".format(float=first_float)
    else:
        string_printOut = "{float:f} is the largest".format(float=second_float)
    print(string_printOut)

def divideIfEvenMultiplyIfOdd(a_integer):
    if (a_integer % 2 == 0):
        a_integer = a_integer // 2
    else:
        a_integer = a_integer * 3
    string_printOut = "Result is: {result}".format(result=a_integer)
    print(string_printOut)

def areThreeNumbersEqual(a_integer, b_integer, c_integer):
    if (a_integer == b_integer or a_integer == c_integer or b_integer == c_integer):
        print("Some numbers are equal")
    else:
        print("All are unique")

def userInputAnInteger():
    input_string = input("Give an integer: ")
    a_number = int(input_string)
    return(a_number)

a_number = userInputAnInteger()
isThisNumberZero(a_number)

input_string = input("Give two floats: ")
a_float = float(input_string.split()[0])
b_float = float(input_string.split()[1])
largestOfTwoFloats(a_float, b_float)

a_number = userInputAnInteger()
divideIfEvenMultiplyIfOdd(a_number)

input_string = input("Give three integers: ")
a_number = int(input_string.split()[0])
b_number = int(input_string.split()[1])
c_number = int(input_string.split()[2])
areThreeNumbersEqual(a_number, b_number, c_number)
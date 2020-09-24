#Exercise 01: Output
#Author: Marcello Pietro Vendruscolo

def printString(a_string):
    print(a_string)

def substractFirstIntFromSecondInt(first_int, second_int):
    difference = first_int - second_int
    str_printOut = "The difference between {first_int} and {second_int} is {result}".format(first_int=first_int, second_int=second_int, result=difference)
    print(str_printOut)

def divideFirstFloatBySecondFloat(first_float, second_float):
    division = first_float / second_float
    str_printOut = "{first_float:f} / {second_float:f} is {result:f}".format(first_float=first_float, second_float=second_float, result=division)
    print(str_printOut)

hardCoded_string = "One half is 50%"
printString(hardCoded_string)

a_integer = 10
b_integer = 3
substractFirstIntFromSecondInt(a_integer, b_integer)

a_float = 1
b_float = 3
divideFirstFloatBySecondFloat(a_float,b_float)

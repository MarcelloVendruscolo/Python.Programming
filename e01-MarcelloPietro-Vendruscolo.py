#Exercise 01: Output
#Author: Marcello Pietro Vendruscolo

def printHardCodedString():
    first_str = "One half is 50%"
    print(first_str)

def printSubstractionTwoIntegers(integer_a, integer_b):
    difference = integer_a - integer_b
    second_str = "The difference between {first_int} and {second_int} is {result}".format(first_int=integer_a, second_int=integer_b, result=difference)
    print(second_str)

def printDivisionTwoFloats(float_a, float_b):
    division = float_a / float_b
    third_str = "{first_float:f} / {second_float:f} is {result:f}".format(first_float=float_a, second_float=float_b, result=division)
    print(third_str)

printHardCodedString()
printSubstractionTwoIntegers(10, 3)
printDivisionTwoFloats(1,3)

#Exercise 02: Input
#Author: Marcello Pietro Vendruscolo

def computeSumOfTwoIntegers(first_int, second_int):
    sum = first_int + second_int
    string_printOut = "You entered {first_int} and {second_int}, their sum is: {result}".format(first_int=first_int, second_int=second_int, result=sum)
    print(string_printOut)

def computeProductOfTwoFloats(first_float, second_float):
    product = first_float * second_float
    string_printOut = "You entered {first_float:f} and {second_float:f}, their product is: {result:f}".format(first_float=first_float, second_float=second_float, result=product)
    print(string_printOut)

def printStringTwice(a_string):
    string_printOut = "{first_rep} {second_rep}".format(first_rep=a_string, second_rep=a_string)
    print(string_printOut)

input_string = input("Give two integers: ")
a_number = int(input_string.split()[0])
b_number = int(input_string.split()[1])
computeSumOfTwoIntegers(a_number, b_number)

input_string = input("Give two floats: ")
a_number = float(input_string.split()[0])
b_number = float(input_string.split()[1])
computeProductOfTwoFloats(a_number, b_number)

input_string = input("Give a word: ")
printStringTwice(input_string)
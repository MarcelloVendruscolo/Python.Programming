#Exercise 03: Conditionals
#Author: Marcello Pietro Vendruscolo


def identifyZeroAsInput():
    integer_inputString = input("Give an integer: ")
    first_integer = int(integer_inputString)
    if (first_integer == 0):
        print("The number you entered equals zero")
    else:
        print("The number you entered does not equal zero")

def largestOfTwoFloats():
    float_inputString = input("Give two floats: ")
    a_float = float(float_inputString.split()[0])
    b_float = float(float_inputString.split()[1])
    if (a_float >= b_float):
        output_string = "{float:f} is the largest".format(float=a_float)
    else:
        output_string = "{float:f} is the largest".format(float=b_float)
    print(output_string)

def divideOrMultipleInteger():
    integer_inputString = input("Give an integer: ")
    first_integer = int(integer_inputString)
    if (first_integer % 2 == 0):
        first_integer = first_integer // 2
    else:
        first_integer = first_integer * 3
    output_string = "Result is: {result}".format(result=first_integer)
    print(output_string)

def identifyIdenticalIntegers():
    input_string1 = input("Give three integers: ")
    a_integer = int(input_string1.split()[0])
    b_integer = int(input_string1.split()[1])
    c_integer = int(input_string1.split()[2])
    if (a_integer == b_integer or a_integer == c_integer or b_integer == c_integer):
        print("Some numbers are equal")
    else:
        print("All are unique")


identifyZeroAsInput()
largestOfTwoFloats()
divideOrMultipleInteger()
identifyIdenticalIntegers()
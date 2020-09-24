#Exercise 02: Input
#Author: Marcello Pietro Vendruscolo

def inputAndPrintSumOfIntegers():
    input_string1 = input("Give two integers: ")
    if (input_string1.split()[0].isdigit()):
        a_integer = int(input_string1.split()[0])
    if (input_string1.split()[1].isdigit()):
        b_integer = int(input_string1.split()[1])
    sum = a_integer + b_integer
    output_string1 = "You entered {first_int} and {second_int}, their sum is: {result}".format(first_int=a_integer, second_int=b_integer, result=sum)
    print(output_string1)

def inputAndPrintProductOfFloats():
    input_string2 = input("Give two floats: ")
    a_float = float(input_string2.split()[0])
    b_float = float(input_string2.split()[1])
    product = a_float * b_float
    output_string2 = "You entered {first_float:f} and {second_float:f}, their sum is: {result:f}".format(first_float=a_float, second_float=b_float, result=product)
    print(output_string2)

def inputAndPrintTwiceAWord():
    input_string3 = input("Give a word: ")
    output_string3 = "{first_rep} {second_rep}".format(first_rep=input_string3, second_rep=input_string3)
    print(output_string3)

inputAndPrintSumOfIntegers()
inputAndPrintProductOfFloats()
inputAndPrintTwiceAWord()
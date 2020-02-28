# declaring variables
a = 5
b = 10

my_variable = 56
any_variable_name = 10

string_variable = "Hello" # doble y simple quotes, there is no differences.

# print command is a method that helps to do sth.
print(my_variable) # print accepst a variable

# printing  value directly
print("hello world")
print(1233)


#  ------- Creating our own METHOD -------
#  def is a keyword of python, then the brackets
# INDENTATION = in python is 4 spaces.. SO IMPORTANT!!!!

def myPrintMethod(argument):
    print("Hello World in a method", my_variable, argument)

# Runnig the method
myPrintMethod("i am Patricia")

def myMultiplyMethod(numOne, numTwo):
    return numOne * numTwo

result = myMultiplyMethod(5, 3)
print("The multiply: ", result)

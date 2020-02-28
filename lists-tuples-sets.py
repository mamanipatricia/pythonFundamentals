# THREE DATATYPES - LIST, TUPLES AND SETS

myVariable = "Hello"

gradeOne = 77
gradeTwo = 88
gradeThree = 99
gradeFour = 100

# calculate of this variables
# adding more grades it is not sustainability
print((gradeOne + gradeTwo + gradeThree + gradeFour) / 4)

# LISTS - mutable
grades = [77, 88, 99, 100] # ordered that it was created the list
grades.append(111)
print(grades)
# ways to add  elements to a list

print(sum(grades)/len(grades)) # len is the longitud
#  SETS - inmutable (means that we cannot increase the size of the tuple) -  cannot be changed
gradesTuple = (77, 88, 99, 100, 299, 445) # inmutable

# SET - unique and unordered
setGrades = {77, 43, 23, 64, 64} # remove 64
print(setGrades)

# --------------------------------

# ADDING
# LIST
grades.append(999)
print("gradesList: ", grades)
# TUPLES - always add the comma i it is just a number to add
gradesTuple = gradesTuple + (999, )
print("gradesTuple: ", gradesTuple)



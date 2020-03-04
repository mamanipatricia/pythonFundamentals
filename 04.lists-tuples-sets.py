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

print("------ ADDING ELEM. TO LIST, TUPLAS AND SETS ------")
# ADDING
# LIST
grades.append(999)
print("gradesList: ", grades)
# TUPLES - always add the comma i it is just a number to add
gradesTuple = gradesTuple + (999, ) # we just add to the top 100
print("gradesTuple: ", gradesTuple)

# ACCEDING AN ELEMENT
# LIST
print(grades[0]) # 0 means the position
# assigning a value in a list grade
grades[0] = 888
print(grades)

# TUPLE
# YOU CANNOT CHANGE THE VALUES AND ADD

# SET
# setGrades[0] = 60 # not accepted!!!
# but wit add method yessss

setGrades.add(60)
setGrades.add(60)
print(setGrades) ## only appears once 60

# --------- ADVANCED SET OPERATIONS ---------
# DEFINITION: SETS is a collection of unique and unordered elements.
print("----SETS OPERATIONS----")
yourLoteryNumber = {1, 2, 3, 4, 5}
winningNumber = {1, 3, 5, 7, 9, 11}

print("INTERSECTION: ", yourLoteryNumber.intersection(winningNumber))

print("UNION: ", yourLoteryNumber.union(winningNumber))

print("DIFERENCE: ", {1, 2, 3, 4}.difference({1, 2}))

# HOMEWORK


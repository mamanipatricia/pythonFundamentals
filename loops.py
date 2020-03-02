my_variable = "hello"

# print(my_variable[0])
# print(my_variable[1])
# print(my_variable[2])
# print(my_variable[3])
# print(my_variable[4])

# iterating "for" loop
#  iterables are strings, lists, sets, tuples, and more
for character in my_variable:
    print(character)

# its a very common mistake call variables that is not declared

my_list = [1, 2, 3, 4, 5]

for number in my_list:
    print(number ** 2)

# WHILE

user_wants_number = True
while user_wants_number == True:
    user_wants_number = False
    print(10)
    user_input = input("Should we print again (y/n) ")
    if user_input =='n':
        user_wants_number = False
        print(10)

# --------------
print("-------------")

know_people = ["John", "Anna", "Mary"]

person = input("Enter the person you know")

if person in know_people:
    print("you know {}!".format(person))
else:
    print("You dont know {}!".format(person))

# if person not in know_people:
#     print("You dont know this person")






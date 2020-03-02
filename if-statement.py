know_people = ["John", "Anna", "Mary"]

person = input("Enter the person you know")

if person in know_people:
    print("you know {}!".format(person))
else:
    print("You dont know {}!".format(person))

# if person not in know_people:
#     print("You dont know this person")


print("--------------")

# Exercise

def who_do_you_know():
    # Ask the user for a list of people they know
    # people = input("Enter the names of people you know, separated by commas: ")# John, Rolf, Anna
    # split the string into a list
    # people_list = people.split(",") # ["John", "Rolf", "Anna", "GReg"]
    # return that list#
    # arrayPerson = []
    # for person in people_list:
    #     arrayPerson.append(person.strip())
    # print("arrayPerson : ", arrayPerson)
    # strip = remove spaces at the beginning and at the end
    # OTHER WAY to simplify the code
    # people_list = [person.strip() for person in people.split(',')]
    return [person.strip() for person in input("Enter the names of people you know, separated by commas: ").split(',')]
    # return people_list

def ask_user():
    person = input("Enter a name of someone you know")
    # ask user for a name
    people = who_do_you_know()
    #  see if their  name is the list of people they  know[person.strip() for person in input(people.split(','))])

    if person in people:
    # print out that they know the person
        print("You know {} ".format(person))
    else:
        print("You do not know {} ".format(person))


ask_user()
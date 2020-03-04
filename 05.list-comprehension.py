my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in my_list]

multiply_list = [x * 3 for x in my_list]
multiply_list = [x * 3 for x in range(len(my_list))]
print(an_equal_list)
print(multiply_list)

print([n for n in range(2, 10) if n% 2 == 0])

people_you_know = ["Rolf", "John", "anna", 'GREG']

# NORMALIZE
normalized_people = [person.strip().lower() for person in people_you_know]
print(normalized_people)



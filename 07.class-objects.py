lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
    # dict cannot do any operations
}

class LotteryPlayer:

    def __init__(self, name):
        self.name = name,
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('john') # This creates an object from this class
player_two = LotteryPlayer('Rolf')
# when we create an object, that object is self, it has name and numbers

player_one.numbers = (1, 2, 3, 4, 5) # we have not change the tuple, it was removed and put it in
print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)


# a student example

class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # def go_to_school(self):
    #     print("I am going to going to school" school")
    @classmethod
    # when you want to have a method that is global..
    def go_to_school(cls):
        print("I am going to school")
        print("I am a {}".format(cls))

    @staticmethod
    # when you want to have a method that it is global..
    def go_to_school():
        print("I am going to school")

anna = Student("Anna", 'MIT')
rolf = Student("rolf", 'Oxford')

anna.marks.append(56)
anna.marks.append(71)

anna.go_to_school()

Student.go_to_school() # this can be declared with both @classmethod and @staticmethod
# all objects ANNA, ROLF share the same method go_to_school

print(anna.marks)
print(anna.average())
# anna.go_to_school() = object.method
# Class method and static method

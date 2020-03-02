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

anna = Student("Anna", 'MIT')
anna.marks.append(56)
anna.marks.append(71)

print(anna.marks)
print(anna.average())

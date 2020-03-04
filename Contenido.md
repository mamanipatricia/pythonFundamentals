### Variables, have to be descriptive


## HOMEWORK:

1. VARIABLES:

- 1. Create two variables, var1 and var2 , both with the same value, it ca be anything you want.
- 2. Create two variables, num1 and num2 , that multiply together to give 16.

Solution:
```python
var1 = "Hello"
var2 = "Hello"

num1 = 4
num2 = 4
```
2. METHODS:

- 1. Complete the method return_42(), by making it return 42.
- 2. Create a method, which must be called my_method() , which takes two arguments and returns the result of its two arguments multiplied together.

<!-- Complete the method by making sure it returns 42. -->
```python
def return_42():
    pass # 'pass' just means "do nothing". Make sure to delete this!
```

```python
def return_42():
    return 42

def my_method():
    return arg1 * arg2
```

# LISTS, TUPLES AND SETS

This coding exercise requires you to complete three steps"
- 1. Create a list, called my_list , with three numbers. Total of the numbers added together should be 100.
- 2. Create a tuple, called my_tuple , with a single value in it.
- 3. MOdify the variable set2 so that set1.intersection(set2) returns {5, 77, 9, 12}

SOLUTION:

```python
1.
my_list = [1, 2, 98]
my_list = [100, 0, 0]
2.
my_tuple = (15) # signify a mathematical operator   X
my_tuple = (15,) _/
my_tuple = 15,  _/
3.
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}
<!-- SOLUTION -->
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
```

### FLOW CONTROL - LOOPS AND IFS

This coding exercise has two steps.
- 1. Modify the method even_numbers() so that it only returns a list of even numbers (2, 4, 6, etc...)
- 2. Modify the method user_menu(choise) so that if choise is "q" . It returns Quit" . Make sure that if choise is "a" it still returns "Add"
```python
numbers = [1, 2, 3, 4 , 5, 6, 7, 8, 9]
```
<!-- modify the method below to make sure only even numbers are returned -->
```python
def even_numbers():
evens = []
for number in numbers:
    evens.append(number)
return evens

<!-- Modify the below method so that "Quit" is returned if the choice parameter is "q". -->
<!-- Do not remove the existing code -->

def user_menu(choise):
if choice == "a":
    return "Add"
```
----------------

SOL:
```python
def even_numbers():
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
return evens
```
#### use elif because always one of them is gonna run

```python
def user_menu(choise):
if choice == "a":
    return "Add"
elif choice == "q"
    return "Quit"

```
### DICTIONARIES

The conding exercise has three parts. See them outlined in detail the coding exercise, as comments

- Create a dictionary variable, called 'student'
- modify a variable, 'grades', so it contains the value of a dictionaries key
- implement a function calculating a total average grade for a class of students.
```python
student =

def average_grade(data):
    grades =
    return sum(grades) / len(grades)

def average_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        ### implement here

    return total / count
```
SOLUTION:

```python
student = {'name': 'jose', 'school': 'computing, 'grades': (66, 77, 88)}

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

def average_all_students(student_list):
    total = 0 # sum all the grades
    count = 0 # amount of grades
    for student in student_list:
        total += sum(student['grades']) # a shortcut +=
        <!-- total = total + sum(student['grades']) -->
        count = count + len(student['grades'])

    return total / count
```
### CLASSES AND OBJECTS
This coding exercise requires you to complete an implementation of three methods of a class:

1. The '__init__' method, which should take an argument, 'name'. It should initialize 'self.name' to be the argument, and 'self.items' to be an empty list.

2. The 'add_item' method, which should append a dictionary representing an item to the store's 'items' property. The dictionary should have keys 'name' and 'price'.
3. The 'stock_price' method. which should add up each item price inside 'self.item' to come up with a total, and return that.

GOOD LUCK!
```python
class Store:
    def __init__(self):
        pass
    def add_item(self, name, price):
        pass
    def stock_price(self):
        pass
```
SOLUTION:
```python
class Store:
    def __init__(self, name):
        # two arguments
        self.name = name
        self.items = []
    def add_item(self, name, price):
        item = {'name': name,'price': price}
        self.items.append(item)
    def stock_price(self):
        total = 0
    return sum([item['price'] for item in self.items]) # [] we are creating a list
```

### @CLASSMETHOD AND @STATICMETHOD

1. This 'franchise' method, which akes in a store argument + " - franchise".

2. The 'store_detail' method, with also takes in a store as argument. It should return a string representing the argument.

a few examples:

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store) # returns a Store with name "Test" - franchise"
Store.franchise(store2) # returns "Stock" with name "Amazon - franchise"

Store.store_details(store) # returns "Test", total stock price: 0
Store.store_details(store2) # returns "Amazon", total stock price: 160

When completing the "store_detail" method you may need to convert the output of "store.stock_price" to an integer. You can do this like so: int(store.stock_price).
GOOD LUCK!

```python
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
    self.items.append({
        'name': name
        'price': price
    })

    def stock_price(self):
        total = 0
        for item in self.items:

    @classmethod
    def franchise(cls, store):
        ## returns another store, with the same as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        ## return a string representing  the argument
        ## it should be the format 'NAME', total stock price: 'TOTAL'
```
SOLUTION:
```python
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
    self.items.append({
        'name': name
        'price': price
    })

    def stock_price(self):
        total = 0
        for item in self.items:

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))
```

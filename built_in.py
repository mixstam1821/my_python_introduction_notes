numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5

for num in range(5):
    print(num)  # Output: 0, 1, 2, 3, 4

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

names = ["Karaiskakis", "Botsaris", "Kolokotronis"]
ages = [25, 30, 35]
for person in zip(names, ages):
    print(person)  # Output: ("Karaiskakis", 25), ("Botsaris", 30), ("Kolokotronis", 35)

names = ["Karaiskakis", "Botsaris", "Kolokotronis"]
for index, name in enumerate(names):
    print(f"Person {index + 1}: {name}")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

values = [True, False, True, True]
print(any(values))  # Output: True
print(all(values))  # Output: False

x = -10
print(abs(x))  # Output: 10

pi = 3.14159
print(round(pi, 2))  # Output: 3.14

print(chr(65))  # Output: 'A'
print(ord('A'))  # Output: 65

x = 10
print(type(x))  # Output: <class 'int'>

my_list = [1, 2, 3]
print(dir(my_list))  # Output: ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

name = input("Enter your name: ")
print(f"Hello, {name}!")

result = eval("3 + 5")
print(result)  # Output: 8

name = "Karaiskakis"
age = 25
print("Hello, my name is {} and I am {} years old.".format(name, age))

file = open("example.txt", 'r')
content = file.read()
file.close()

print("Hello, World!")

x = 10
print(isinstance(x, int))  # Output: True

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

x = -10
print(abs(x))  # Output: 10

result = pow(2, 3)
print(result)  # Output: 8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = slice(2, 7, 2)
print(numbers[s])  # Output: [3, 5, 7]

result = format(123.456, '.2f')
print(result)  # Output: '123.46'

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1

names = ["Karaiskakis", "Botsaris", "Kolokotronis"]
ages = [25, 30, 35]
for person in zip(names, ages):
    print(person)  # Output: ("Karaiskakis", 25), ("Botsaris", 30), ("Kolokotronis", 35)

result = round(3.14159, 2)
print(result)  # Output: 3.14



x = 10
def modify():

    global x
    x=3


modify()
print(x) # Output: 3




# Function	Description https://www.w3schools.com/python/python_ref_functions.asp
# abs()	Returns the absolute value of a number
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	Returns the binary version of a number
# bool()	Returns the boolean value of the specified object
# bytearray()	Returns an array of bytes
# bytes()	Returns a bytes object
# callable()	Returns True if the specified object is callable, otherwise False
# chr()	Returns a character from the specified Unicode code.
# classmethod()	Converts a method into a class method
# compile()	Returns the specified source as an object, ready to be executed
# complex()	Returns a complex number
# delattr()	Deletes the specified attribute (property or method) from the specified object
# dict()	Returns a dictionary (Array)
# dir()	Returns a list of the specified object's properties and methods
# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	Evaluates and executes an expression
# exec()	Executes the specified code (or object)
# filter()	Use a filter function to exclude items in an iterable object
# float()	Returns a floating point number
# format()	Formats a specified value
# frozenset()	Returns a frozenset object
# getattr()	Returns the value of the specified attribute (property or method)
# globals()	Returns the current global symbol table as a dictionary
# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# hash()	Returns the hash value of a specified object
# help()	Executes the built-in help system
# hex()	Converts a number into a hexadecimal value
# id()	Returns the id of an object
# input()	Allowing user input
# int()	Returns an integer number
# isinstance()	Returns True if a specified object is an instance of a specified object
# issubclass()	Returns True if a specified class is a subclass of a specified object
# iter()	Returns an iterator object
# len()	Returns the length of an object
# list()	Returns a list
# locals()	Returns an updated dictionary of the current local symbol table
# map()	Returns the specified iterator with the specified function applied to each item
# max()	Returns the largest item in an iterable
# memoryview()	Returns a memory view object
# min()	Returns the smallest item in an iterable
# next()	Returns the next item in an iterable
# object()	Returns a new object
# oct()	Converts a number into an octal
# open()	Opens a file and returns a file object
# ord()	Convert an integer representing the Unicode of the specified character
# pow()	Returns the value of x to the power of y
# print()	Prints to the standard output device
# property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	Returns a readable version of an object
# reversed()	Returns a reversed iterator
# round()	Rounds a numbers
# set()	Returns a new set object
# setattr()	Sets an attribute (property/method) of an object
# slice()	Returns a slice object
# sorted()	Returns a sorted list
# staticmethod()	Converts a method into a static method
# str()	Returns a string object
# sum()	Sums the items of an iterator
# super()	Returns an object that represents the parent class
# tuple()	Returns a tuple
# type()	Returns the type of an object
# vars()	Returns the __dict__ property of an object
# zip()	Returns an iterator, from two or more iterators


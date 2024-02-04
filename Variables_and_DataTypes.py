# Variables
x = 5
name = "Kseniia"
# Integers
age = 25
quantity = 10

# Floats
pi = 3.14
temperature = 98.6


# Converting to integer
x = int(3.14)

# Converting to float
y = float(5)

# Converting to string
z = str(10)


# Using type() function to check the data type
print(type(10))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>

x = 5
x = x + 1  # Reassigning the variable

# Convention for constants (although Python doesn't have true constants)
PI = 3.14
MAX_SIZE = 1000


# Data Types
number = 10
decimal = 3.14
is_valid = True


message = "Hello, World!"
name = 'Kseniia'
multiline_string = '''
This is a 
multiline
string
'''
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
name = "Kseniia"
age = 30
message = "Hello, my name is {} and I am {} years old".format(name, age)

# Converting to uppercase
message = "hello"
uppercase_message = message.upper()  # Output: "HELLO"

# Converting to lowercase
shout = "STOP SHOUTING!"
quiet = shout.lower()  # Output: "stop shouting!"

# Splitting a string
sentence = "This is a sentence."
words = sentence.split()  # Output: ['This', 'is', 'a', 'sentence.']

# Joining strings
words = ["Hello", "World"]
greeting = " ".join(words)  # Output: "Hello World"
message = "Hello, World!"
print(message[0])  # Output: "H"
print(message[7:])  # Output: "World!"
# Using escape characters
path = "C:\\folder\\file.txt"
multiline = "This is a\nmultiline\nstring"
name = "Kseniia"
age = 25
message = f"Hello, my name is {name} and I am {age} years old"
message = "Hello, World!"
length = len(message)  # Output: 13
message = "Hello, World!"
print("Hello" in message)  # Output: True
print("Python" not in message)  # Output: True
# Using comparison operators
str1 = "apple"
str2 = "banana"
print(str1 == str2)  # Output: False
print(str1 < str2)  # Output: True
symbol = "-"
line = symbol * 10  # Output: "----------"
text = "   Hello, World!   "
trimmed_text = text.strip()  # Output: "Hello, World!"
file_path = r'C:\folder\file.txt'
name = "Kseniia"
age = 25
message = "Hello, my name is {} and I am {} years old".format(name, age)




numbers = [1, 2, 3, 4, 5]
names = ["Kseniia", "Michael", "Fluffy"]
mixed_list = [1, "Kseniia", True, 3.14]
numbers = [1, 2, 3, 4, 5]

# Adding elements
numbers.append(6)  # Output: [1, 2, 3, 4, 5, 6]
numbers.insert(2, 2.5)  # Output: [1, 2, 2.5, 3, 4, 5, 6]

# Removing elements
numbers.remove(3)  # Output: [1, 2, 2.5, 4, 5, 6]
popped = numbers.pop()  # Output: 6, numbers: [1, 2, 2.5, 4, 5]

# Reversing the list
numbers.reverse()  # Output: [5, 4, 2.5, 2, 1]
colors = ["red", "green", "blue", "yellow", "orange"]
print(colors[0])  # Output: "red"
print(colors[2:4])  # Output: ["blue", "yellow"]
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Output: [1, 4, 9, 16, 25]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  # Output: [1, 2, 3, 4, 5, 6]
repeated = list1 * 3  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Output: True
print(6 not in numbers)  # Output: True
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
numbers = [1, 2, 3, 4, 2, 3, 2, 5]
print(numbers.count(2))  # Output: 3
print(numbers.index(4))  # Output: 3
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))  # Output: 4
list1 = [1, 2, 3]
list2 = list1  # list2 is an alias for list1
list3 = list1[:]  # list3 is a clone of list1
numbers = [1, 2, 3]
first, second, third = numbers
print(first)  # Output: 1


point = (3, 4)
dimensions = (800, 600)
# Tuple packing
person = "Kseniia", 25, "Thessaloniki"

# Tuple unpacking
name, age, city = person

coordinates = (3, 5, 7)
print(coordinates[1])  # Output: 5
print(coordinates[0:2])  # Output: (3, 5)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)
repeated = tuple1 * 3  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

numbers = (1, 2, 3, 4, 5)
print(3 in numbers)  # Output: True
print(6 not in numbers)  # Output: True

coordinates = (3, 5, 7)
print(len(coordinates))  # Output: 3
coordinates = (3, 5, 7)
x, y, z = coordinates
print(y)  # Output: 5



person = {"name": "Kseniia", "age": 25, "is_student": False}
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

person = {"name": "Kseniia", "age": 25, "city": "Thessaloniki"}
print(len(person))  # Output: 3

person = {"name": "Kseniia", "age": 25}
print(person.get("city", "Unknown"))  # Output: "Unknown"

numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


dict1 = {"a": 1, "b": 2}
dict2 = dict1  # dict2 is an alias for dict1
dict3 = dict1.copy()  # dict3 is a clone of dict1


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # Output: {"a": 1, "b": 3, "c": 4}

person = {"name": "Kseniia", "age": 25, "city": "Thessaloniki"}
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(person.values())  # Output: dict_values(['Kseniia', 25, 'Thessaloniki'])

person = {"name": "Kseniia", "age": 25, "city": "Thessaloniki"}
for key in person:
    print(key, person[key])  # Output: name Kseniia, age 25, city Thessaloniki

person = {"name": "Kseniia", "age": 25, "city": "Thessaloniki"}
del person["age"]  # Removes the "age" key and its value
person.clear()  # Removes all items from the dictionary

original = {"a": 1, "b": 2}
copy1 = original.copy()
copy2 = dict(original)

person = {"name": "Kseniia", "age": 25}
age = person.setdefault("age", 30)  # Output: 25 (existing value)
city = person.setdefault("city", "Thessaloniki")  # Output: "Thessaloniki" (new key-value pair)

person = {"name": "Kseniia", "age": 25, "city": "Thessaloniki"}
age = person.pop("age")  # Removes the "age" key and returns its value
city = person.pop("city", "Unknown")  # Removes the "city" key and returns its value, or "Unknown" if key not found
keys = ["a", "b", "c"]
default_value = 0
new_dict = dict.fromkeys(keys, default_value)  # Output: {"a": 0, "b": 0, "c": 0}

numbers = [1, 2, 3, 4, 5]
squared_even_dict = {x: x**2 for x in numbers if x % 2 == 0}  # Output: {2: 4, 4: 16}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}  # Output: {"a": 1, "b": 3, "c": 4}




is_valid = True
is_ready = False
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
x = 10
y = []
print(bool(x))  # Output: True
print(bool(y))  # Output: False
age = 25
print(age == 25)  # Output: True
print(age < 18)   # Output: False
a = True
b = False
result = a or some_function()  # If a is True, some_function() will not be called
print(bool(0))      # Output: False
print(bool(10))     # Output: True
print(bool("hello"))  # Output: True
print(int(True))   # Output: 1
print(int(False))  # Output: 0


result = None



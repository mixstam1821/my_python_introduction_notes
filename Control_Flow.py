age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


if 5>0:
    if 3>4:
        print(3)
    else:
        print(4)





x = 10
result = "even" if x % 2 == 0 else "odd"

for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop body for i=2
    if i == 4:
        break  # Exit the loop when i=4

try:
    # Code that may raise an exception
except SomeException:
    # Handle the exception


with open('file.txt', 'r') as file:
    data = file.read()


for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(num, letter)

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
for number, name in pairs:
    print(f"The number {number} is written as {name}")

while True:
    # Do something indefinitely

numbers = [1, 2, 3, 4, 5]
squared_even = [x**2 for x in numbers if x % 2 == 0]

numbers = [1, 2, 3, 4, 5]
squared = (x**2 for x in numbers)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for char in "hello":
    print(char)

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)


my_list = [1, 2, 3, 4, 5]
target = 6
for item in my_list:
    if item == target:
        print("Item found")
        break
else:
    print("Item not found")


my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key, my_dict[key])

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)

my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(index, value)

fruits = ["apple", "banana", "cherry"]
prices = [1.00, 0.75, 1.50]
for fruit, price in zip(fruits, prices):
    print(fruit, price)

my_list = [1, 2, 3, 4, 5]
for item in reversed(my_list):
    print(item)




coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"X: {x}, Y: {y}")


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Print a new line after each row

my_string = "hello, world!"
char_count = {}
for char in my_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

for i in range(0, 10, 2):  # Start at 0, end at 10 (exclusive), step by 2
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)




squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # Output: [0, 1, 4, 9, 16]

squares = [i ** 2 for i in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

words = ["apple", "banana", "cherry"]
word_lengths = [len(word) for word in words]
print(word_lengths)  # Output: [5, 6, 6]

even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}


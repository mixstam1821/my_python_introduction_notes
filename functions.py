def greet(name):
    print("Hello, " + name + "!")

greet("Kanaris")


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Katsantonis")  # Output: Hello, Katsantonis!
greet("Kanaris", "Good morning")  # Output: Good morning, Kanaris!

def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total

result = sum_values(1, 2, 3, 4, 5)
print(result)  # Output: 15

def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_values(name="Katsantonis", age=25, city="Agrafa")
# Output:
# name: Katsantonis
# age: 25
# city: Agrafa

def min_max(values):
    return min(values), max(values)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = min_max(numbers)
print(min_value, max_value)  # Output: 1 9

double = lambda x: x * 2
print(double(5))  # Output: 10

def apply_operation(operation, x, y):
    return operation(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 3, 4)
print(result)  # Output: 7



def compute_statistics_low_level(data):
    n = len(data)
    
    # Compute average
    total = 0
    for value in data:
        total += value
    average = total / n

    # Compute variance
    sum_squared_diff = 0
    for value in data:
        sum_squared_diff += (value - average) ** 2
    variance = sum_squared_diff / n

    # Compute standard deviation
    std_deviation = variance ** 0.5

    # Compute median
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]

    return {
        "average": average,
        "std_deviation": std_deviation,
        "variance": variance,
        "median": median
    }

# Example usage:
data = [1, 2, 3, 4, 5]
result = compute_statistics_low_level(data)
print(result)
# Output: {'average': 3.0, 'std_deviation': 1.4142135623730951, 'variance': 2.0, 'median': 3}



def calculate_mode(data):
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_frequency = max(frequency.values())
    mode = [key for key, val in frequency.items() if val == max_frequency]

    return mode

# Example usage:
data = [1, 2, 3, 3, 4, 4, 4, 5]
result = calculate_mode(data)
print(result)
# Output: [4]


# Define a list of numerical data
data = [1, 2, 3, 4, 5]

# Calculate average using a lambda expression
average = lambda x: sum(x) / len(x)
print("Average:", average(data))  # Output: 3.0

# Calculate standard deviation using a lambda expression
std_deviation = lambda x: (sum((i - average(x)) ** 2 for i in x) / len(x)) ** 0.5
print("Standard Deviation:", std_deviation(data))  # Output: 1.4142135623730951


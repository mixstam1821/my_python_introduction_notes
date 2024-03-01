# TODO 1 Making Add, Subtract, Multiply, and Divide Functions

def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


# TODO 2 Making a user input Function

def recursiveCalculator(result):
    number1 = int(input("Input number 1\n"))
    choice = input("+ Addition \n- Subtraction\n* Multiplication\n/ Division")
    if choice == "+":
        result = add(result, number1)
    elif choice == "-":
        result = subtract(result, number1)
    elif choice == "*":
        result = multiply(result, number1)
    else:
        result = divide(result, number1)

    print(f"Result is :{result}")


def userInteraction():
    result = 0
    number1 = int(input("Input number 1\n"))
    number2 = int(input("Input number 2\n"))
    choice = input("+ Addition \n- Subtraction\n* Multiplication\n/ Division")
    if choice == "+":
        result = add(number1, number2)
    elif choice == "-":
        result = subtract(number1, number2)
    elif choice == "*":
        result = multiply(number1, number2)
    else:
        result = divide(number1, number2)

    print(f"Result is :{result}")

    recursion = input("Do you want to calculate again? Y|N").lower()

    while recursion == "y":
        recursiveCalculator(result)
        recursion = input("Do you want to calculate again? Y|N").lower()

# TODO 3 Making a recursion for calculator

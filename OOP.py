# Object-Oriented Programming (OOP) is funny and really usefull <3

# Class definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Object instantiation
my_dog = Dog("Fluffy", 3)

# Accessing attributes and calling methods
print(my_dog.name)
my_dog.bark()



class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def compute_average(self):
        return sum(self.data) / len(self.data)

    def compute_std_deviation(self):
        average = self.compute_average()
        return (sum((x - average) ** 2 for x in self.data) / len(self.data)) ** 0.5

# gmail usage:
data = [1, 2, 3, 4, 5]
calculator = StatisticsCalculator(data)
print("Average:", calculator.compute_average())  # Output: 3.0
print("Standard Deviation:", calculator.compute_std_deviation())  # Output: 1.4142135623730951

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_positive_numbers(self):
        return [x for x in self.data if x > 0]

    def calculate_sum(self):
        return sum(self.data)

# gmail usage:
data = [1, -2, 3, -4, 5]
processor = DataProcessor(data)
positive_numbers = processor.filter_positive_numbers()
print("Positive Numbers:", positive_numbers)  # Output: [1, 3, 5]
print("Sum of Data:", processor.calculate_sum())  # Output: 3


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_full_name(self):
        return f"{self.year} {self.make} {self.model}"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Create an instance of the Car class
my_car = Car("Tesla", "Model S", 2022)
print(my_car.get_full_name())  # Output: 2022 Tesla Model S
my_car.update_odometer(100)
my_car.increment_odometer(50)
print("Odometer Reading:", my_car.odometer_reading)  # Output: 150


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

# Create an instance of the Dog class
my_dog = Dog("Fluffy", 3)
print(f"{my_dog.name} is {my_dog.age} years old.")  # Output: Fluffy is 3 years old
my_dog.sit()  # Output: Fluffy is now sitting.
my_dog.roll_over()  # Output: Fluffy rolled over!


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Create an instance of the BankAccount class
my_account = BankAccount("123456789", 1000)
print("Initial Balance:", my_account.balance)  # Output: 1000
my_account.deposit(500)
my_account.withdraw(200)
print("Updated Balance:", my_account.balance)  # Output: 1300


class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

    def take_exam(self, subject):
        print(f"{self.name} is taking an exam in {subject}.")

# Create an instance of the Student class
my_student = Student("Kseniia", 20, "Computer Science")
print(f"{my_student.name} is {my_student.age} years old and majoring in {my_student.major}.")  # Output: Kseniia is 20 years old and majoring in Computer Science
my_student.study("Python programming")
my_student.take_exam("Data Structures")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of the Rectangle class
my_rectangle = Rectangle(5, 7)
print("Area:", my_rectangle.area())  # Output: 35
print("Perimeter:", my_rectangle.perimeter())  # Output: 24


class EmailMessage:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self):
        print(f"Email sent from {self.sender} to {self.recipient} with subject: {self.subject}")

# Create an instance of the EmailMessage class
email = EmailMessage("sender@gmail.com", "recipient@gmail.com", "Hello", "Just saying hi!")
email.send()  # Output: Email sent from sender@gmail.com to recipient@gmail.com with subject: Hello


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius

# Create an instance of the Circle class
my_circle = Circle(5)
print("Area:", my_circle.area())  # Output: 78.53975
print("Circumference:", my_circle.circumference())  # Output: 31.4159

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}, Email: {self.email}")

# Create an instance of the User class
user1 = User("mike_stam", "mixstam1453@gmail.com")
user1.display_info()  # Output: Username: mike_stam, Email: mixstam1453@gmail.com





class BankCustomer:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Create an instance of the BankCustomer class
customer = BankCustomer("Kseniia", "123456789", 1500)
print(f"Customer: {customer.name}, Account Number: {customer.account_number}, Balance: {customer.balance}")  # Output: Customer: Kseniia, Account Number: 123456789, Balance: 1500
customer.deposit(500)
customer.withdraw(200)
print(f"Updated Balance: {customer.balance}")  # Output: Updated Balance: 1800

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

# Create an instance of the Product class
product1 = Product("Laptop", 1200, 3)
print(f"Product: {product1.name}, Total Price: ${product1.calculate_total_price()}")  # Output: Product: Laptop, Total Price: $3600



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022, 4)
my_car.display_info()  # Output: Vehicle: 2022 Toyota Camry, Doors: 4

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

class DVD(LibraryItem):
    def __init__(self, title, author, release_date):
        super().__init__(title, author)
        self.release_date = release_date

class LibraryCatalog:
    def __init__(self):
        self.catalog = []

    def add_item(self, item):
        self.catalog.append(item)

# Create instances of the Book, DVD, and LibraryCatalog classes
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
dvd1 = DVD("Inception", "Christopher Nolan", "2010-07-16")
library = LibraryCatalog()
library.add_item(book1)
library.add_item(dvd1)




class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, transaction_fee=1.5):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self.balance -= self.transaction_fee

# Create instances of the SavingsAccount and CheckingAccount classes
savings_account = SavingsAccount("12345", 1000)
savings_account.deposit(500)
savings_account.add_interest()
print("Savings Account Balance:", savings_account.balance)  # Output: Savings Account Balance: 1520.0

checking_account = CheckingAccount("67890", 2000)
checking_account.withdraw(500)
checking_account.deduct_transaction_fee()
print("Checking Account Balance:", checking_account.balance)  # Output: Checking Account Balance: 1498.5


class Property:
    def __init__(self, address, square_feet, price):
        self.address = address
        self.square_feet = square_feet
        self.price = price

class RealEstateAgent:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

# Create instances of the Property and RealEstateAgent classes
property1 = Property("123 Main St", 2000, 500000)
property2 = Property("456 Elm St", 1500, 350000)
agent = RealEstateAgent("Kseniia")
agent.add_property(property1)
agent.add_property(property2)



class Emperor:
    def __init__(self, name, reign_start, reign_end):
        self.name = name
        self.reign_start = reign_start
        self.reign_end = reign_end

    def rule_length(self):
        return self.reign_end - self.reign_start

class ByzantineEmpire:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.emperors = []

    def add_emperor(self, emperor):
        self.emperors.append(emperor)

# Create instances of the Emperor and ByzantineEmpire classes
justinian = Emperor("Justinian I", 527, 565)
theodora = Emperor("Theodora", 527, 548)
byzantium = ByzantineEmpire("Byzantine Empire", 330)
byzantium.add_emperor(justinian)
byzantium.add_emperor(theodora)

for emperor in byzantium.emperors:
    print(f"{emperor.name} ruled for {emperor.rule_length()} years.")


class ByzantineEmperor:
    def __init__(self, name, reign_start, reign_end, notable_achievements):
        self.name = name
        self.reign_start = reign_start
        self.reign_end = reign_end
        self.notable_achievements = notable_achievements

    def rule_length(self):
        return self.reign_end - self.reign_start

class ByzantineCapital:
    def __init__(self, name, foundation_year, location):
        self.name = name
        self.foundation_year = foundation_year
        self.location = location

class ByzantineMilitaryCampaign:
    def __init__(self, campaign_name, start_year, end_year, description):
        self.campaign_name = campaign_name
        self.start_year = start_year
        self.end_year = end_year
        self.description = description

# Create instances of the ByzantineEmperor, ByzantineCapital, and ByzantineMilitaryCampaign classes
justinian = ByzantineEmperor("Justinian I", 527, 565, "Legal reforms, construction of Hagia Sophia")
constantinople = ByzantineCapital("Constantinople", 330, "Modern-day Istanbul")
persian_campaign = ByzantineMilitaryCampaign("Byzantine-Persian War", 602, 628, "Struggle between the Byzantine Empire and the Sassanian Persian Empire")

print(f"{justinian.name} ruled for {justinian.rule_length()} years and is known for {justinian.notable_achievements}.")
print(f"{constantinople.name} was founded in {constantinople.foundation_year} and is located in {constantinople.location}.")
print(f"The {persian_campaign.campaign_name} took place from {persian_campaign.start_year} to {persian_campaign.end_year}.")
print(f"Description: {persian_campaign.description}")



class ByzantineCity:
    def __init__(self, name, foundation_year, location, important_sites):
        self.name = name
        self.foundation_year = foundation_year
        self.location = location
        self.important_sites = important_sites

    def __str__(self):
        return f"{self.name} - Founded: {self.foundation_year}, Location: {self.location}, Important Sites: {', '.join(self.important_sites)}"

# Create instances of the ByzantineCity class
constantinople = ByzantineCity("Constantinople", 330, "Modern-day Istanbul", ["Hagia Sophia", "Great Palace of Constantinople", "Hippodrome of Constantinople"])
thessaloniki = ByzantineCity("Thessaloniki", 315, "Modern-day Thessaloniki", ["Arch of Galerius and Rotunda", "Church of St. Demetrios", "White Tower of Thessaloniki"])
antioch = ByzantineCity("Antioch", 300, "Modern-day Antakya", ["Church of St. Peter", "Antioch mosaics", "Caves of Antioch"])

# Display information about the Byzantine cities
print(constantinople)
print(thessaloniki)
print(antioch)


class GreekRevolution:
    def __init__(self, start_year, end_year, key_figures, major_events):
        self.start_year = start_year
        self.end_year = end_year
        self.key_figures = key_figures
        self.major_events = major_events

    def duration(self):
        return self.end_year - self.start_year

    def list_events(self):
        event_list = "\n".join(self.major_events)
        return event_list

# Create an instance of the GreekRevolution class
greek_independence = GreekRevolution(1821, 1830, ["Theodoros Kolokotronis", "Laskarina Bouboulina", "Alexander Ypsilantis"], 
                                     ["Declaration of the Greek War of Independence", "Massacre of Chios", "Battle of Navarino"])

# Display information about the Greek Revolution of 1821
print(f"The Greek War of Independence lasted for {greek_independence.duration()} years.")
print("Key Figures:")
for figure in greek_independence.key_figures:
    print(f"- {figure}")
print("Major Events:")
print(greek_independence.list_events())



# Inheritance in Python allows a class to inherit attributes and methods from another class.

# SINGLE INHERITANCE
# Single Inheritance: A child class inherits from one parent class.

# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Child class
class Car(Vehicle):
    def __init__(self, brand, model, airbags):
        super().__init__(brand, model)  # Call the parent class constructor
        self.airbags = airbags

    def display_car_info(self):
        self.display_info()  # Call the parent class method
        print(f"Airbags: {self.airbags}")

# Example usage
car1 = Car("Toyota", "Corolla", 6)
car1.display_car_info()
'''
Key Points:
super():

Used to call methods or constructors of the parent class.
Example: super().__init__(brand, model).
Method Overriding:

A child class can override methods of the parent class.

EXAMPLE:
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

obj = Child()
obj.show()  # Output: Child method

'''

# MULTIPLE INHERITANCE
# Multiple Inheritance: A child class inherits from multiple parent classes.

# Parent class 1
class Engine:
    def engine_type(self):
        print("Engine type: Petrol")

# Parent class 2
class Wheels:
    def wheel_count(self):
        print("Number of wheels: 4")

# Child class
class Car(Engine, Wheels):
    def car_info(self):
        print("Car details:")
        self.engine_type()
        self.wheel_count()

# Example usage
car1 = Car()
car1.car_info()


# MULTILEVEL INHERITANCE
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.

# Grandparent class
class Vehicle:
    def vehicle_type(self):
        print("Vehicle type: Car")

# Parent class
class Car(Vehicle):
    def brand(self):
        print("Brand: Toyota")

# Child class
class Model(Car):
    def model_name(self):
        print("Model: Corolla")

# Example usage
model1 = Model()
model1.vehicle_type()
model1.brand()
model1.model_name()

# HIERARCHICAL INHERITANCE
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"Brand: {self.brand}")

# Child class 1
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        print(f"Car Model: {self.model}")

# Child class 2
class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def display_info(self):
        print(f"Bike Type: {self.type}")

# Example usage
car1 = Car("Toyota", "Corolla")
bike1 = Bike("Yamaha", "Sport")

car1.display_brand()  # Output: Brand: Toyota
car1.display_info()   # Output: Car Model: Corolla

bike1.display_brand()  # Output: Brand: Yamaha
bike1.display_info()   # Output: Bike Type: Sport


# HYBRID INHERITANCE
# Hybrid Inheritance: A combination of two or more types of inheritance.

# Parent class
class Engine:
    def engine_type(self):
        print("Engine type: Petrol")

# Intermediate class (Single Inheritance)
class Vehicle(Engine):
    def vehicle_type(self):
        print("Vehicle type: Car")

# Child class 1 (Hierarchical Inheritance)
# This is actually a multilevel inheritance example 
class Car(Vehicle):
    def brand(self):
        print("Brand: Toyota")

# Child class 2 (Hierarchical Inheritance)
class Bike(Vehicle):
    def brand(self):
        print("Brand: Yamaha")

# Example usage
car1 = Car()
bike1 = Bike()

car1.engine_type()  # Output: Engine type: Petrol
car1.vehicle_type()  # Output: Vehicle type: Car
car1.brand()         # Output: Brand: Toyota

bike1.engine_type()  # Output: Engine type: Petrol
bike1.vehicle_type()  # Output: Vehicle type: Car
bike1.brand()         # Output: Brand: Yamaha
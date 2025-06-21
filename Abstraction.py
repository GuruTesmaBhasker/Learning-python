# Abstraction 

"""
Abstraction is a fundamental concept in object-oriented programming that focuses on 
hiding implementation details and exposing only the essential features of an object. 
It allows you to work with high-level interfaces without worrying about the underlying complexity.

Abstract Classes:

Abstract classes are classes that cannot be instantiated directly.
They serve as blueprints for other classes.
Abstract classes are created using the abc (Abstract Base Class) module.
Abstract Methods:

Abstract methods are methods that are declared but not implemented in an abstract class.
Any subclass inheriting from an abstract class must implement all its abstract methods.


"""
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method (no implementation)

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method (no implementation)

# Subclass 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Subclass 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
# Example usage

shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

'''
Rectangle1 = Rectangle(4, 5)
Circle1 = Circle(3)
print("Rectangle Area:", Rectangle1.area())
print("Rectangle Perimeter:", Rectangle1.perimeter())
print("Circle Area:", Circle1.area())
print("Circle Perimeter:", Circle1.perimeter())

'''
"""
# Polymorphism

Polymorphism is a concept in object-oriented programming that allows objects of 
different classes to be treated as objects of a common superclass. 
It enables the same method name to behave differently based on the object calling it.

Types of Polymorphism:

1. Compile-time Polymorphism (Method Overloading):
   - This occurs when multiple methods have the same name but different parameters.
   - Python does not support method overloading in the traditional sense, but you can achieve similar behavior using default arguments or variable-length arguments.

2. Runtime Polymorphism (Method Overriding):
   - This occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
   - The method in the subclass overrides the method in the superclass.

"""

# Example of Compile-time Polymorphism using default arguments (Method Overloading)

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example usage
calc = Calculator()
print(calc.add(5))         # Output: 5 (only one argument)
print(calc.add(5, 10))     # Output: 15 (two arguments)
print(calc.add(5, 10, 15)) # Output: 30 (three arguments)
# If we give more than 3 arguments, it will throw an error.

"""
In this case there are 3 arguments, but you don't know how many arguments you will get.
so we use other methods to achieve this, like *args or **kwargs.

what is *args and **kwargs?
*args is like a tuple, It stores and then we can traverse it.
**kwargs is like a dictionary, It stores key-value pairs.
So, we use *args and **kwargs to achieve this.

"""
# Example of method overloading using *args

class Calculator:
    def add(self, *args):
        return sum(args) #sum(args) → Python’s built-in sum() function adds up all the numbers in the tuple.

# Example usage
calc = Calculator()
print(calc.add(5))         # Output: 5 (only one argument)
print(calc.add(5, 10))     # Output: 15 (two arguments)
print(calc.add(5, 10, 15)) # Output: 30 (three arguments)
print(calc.add(1, 2, 3, 4, 5)) # Output: 15 (five arguments)
# In this case, we can pass any number of arguments to the add method, and it will return the sum of all the arguments.

"""
This is only way to use method overloading in Python. Because Python is a dynamically typed language, 
it does not support method overloading in the traditional sense like some other languages (e.g., Java or C++).

LET'S SEE AN EXAMPLE OF RUNTIME POLYMORPHISM (METHOD OVERRIDING) in java:
public class Calculator {

    // Method with 2 int parameters
    public int add(int a, int b) {
        return a + b;
    }

    // Overloaded method with 3 int parameters
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Overloaded method with 2 double parameters
    public double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println("Add 2 ints: " + calc.add(5, 10));         // 15
        System.out.println("Add 3 ints: " + calc.add(1, 2, 3));       // 6
        System.out.println("Add 2 doubles: " + calc.add(2.5, 3.5));   // 6.0
    }
}

"""

# METHOD OVERRIDING IN PYTHON
# In Python, method overriding is achieved by defining a method in a child class that has the same name as a method in its parent class.

# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Example usage
animals = [Dog(), Cat()]



for animal in animals:
    animal.speak()  # Output: Dog barks, Cat meows


# Myexample 
class father:

    def __init__(self):
        print("father constructor")
    
    def sayhello(self):
        print("hello from father")
        
class child(father):

    def __init__(self):
        print("child constructor")

    def sayhello(self, name):
        print ("Hello from child",name)

child1 = child()
child1.sayhello("guru") # If we don't pass any argument, it will throw an error. because we overridden the method sayhello in child class.
 # Output: Hello from child guru
father1 = father()
father1.sayhello() # Output: hello from father

"""
# If we want to call the parent class method, we can use super() function.
class child(father):

    def __init__(self):
        print("child constructor")

    def sayhello(self, name):
        super().sayhello()  # Call the parent class method
        print ("Hello from child",name)
"""

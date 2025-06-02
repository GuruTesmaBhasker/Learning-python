"""Syntax of the User Defined Functions
def function_name(parameters):
    # code block
    return something (optional)
"""
#Void Functions, Doesn't return a value
def greet_user(name):
    print("Hello", name)  # No return statement → void function

greet_user("Guru")

#Non-void Functions, retuns a value 
def add_numbers(a, b):
    result = a + b
    return result  # This returns a value → non-void function

sum = add_numbers(10, 5)
print("Sum is:", sum)

#Example 1
# Void Function Example
def welcome_message():
    print("Welcome to Python functions!")

# Non-Void Function Example
def multiply(x, y):
    return x * y

# Calling the functions
welcome_message()  # This is a void function

product = multiply(float(input("Enter first number: ")), float(input("Enter second number: ")))
print("The product is:", product)

# Example 2
# Function with multiple return values
def res(a, b):
    return (a + b, a - b, a * b, a/b, a%b) # This is parameters 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = res(a, b) # This is arguments
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Divide:", result[3])
print("Modulus:", result[4])

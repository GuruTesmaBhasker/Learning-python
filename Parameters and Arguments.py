# Parameters and Arguments Example

# Parameters are the variables defined in the function definition
def greet_user(name):  # 'name' is a parameter
    print("Hello,", name)

# Arguments are the actual values passed to the function when calling it
greet_user("Alice")  # "Alice" is an argument
greet_user("Bob")    # "Bob" is another argument


# Another Example: Function with multiple parameters
def add_numbers(a, b):  # 'a' and 'b' are parameters
    return a + b

# Passing arguments to the function
result = add_numbers(10, 5)  # 10 and 5 are arguments
print("Sum is:", result)  # Output: Sum is: 15

#Types of Arguments
# 1. Positional Arguments: The order of arguments matters
# 2. Keyword Arguments: You can specify the parameter names
# 3. Default Arguments: You can provide default values for parameters
# 4. Variable-length Arguments: You can pass a variable number of arguments


# Example of Positional Arguments
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user("Alice", 25)  # Positional arguments: "Alice" → name, 25 → age
#Mostly this is used when we have a fixed number of parameters and we know the order of the parameters.


#example of keyword arguments
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user(age=25, name="Alice")  # Keyword arguments: age=25, name="Alice"
#Incase i have many parameters and I dont remember the order of the parameters, I can use keyword arguments to specify the parameter names explicitly.


# Example of Default Arguments
def greet_user(name, age=18):  # Default value for age is 18
    print(f"Hello {name}, you are {age} years old.")

greet_user("Alice")  # Output: Hello Alice, you are 18 years old.
greet_user("Bob", 25)  # Output: Hello Bob, you are 25 years old.
# In this case, if I don't provide the age argument, it will take the default value of 18.


# Example of Variable-length Arguments
# Using *args
def add_numbers(*args):#This collects all the value passed 
    # Collects extra positional arguments as a tuple.
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10

# Using **kwargs
def print_user_info(**kwargs):# This collects all the keyword arguments
    # Collects extra keyword arguments as a dictionary.
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

#Using all types of arguments together
def greet_user(name, age=18, *args, **kwargs):
    print(f"Hello {name}, you are {age} years old.")
    print("Additional arguments:", args)
    print("Keyword arguments:", kwargs)
greet_user("Alice", 25, "Engineer", "New York", city="New York", country="USA")
# Output:
# Hello Alice, you are 25 years old.
# Additional arguments: ('Engineer', 'New York')
# Keyword arguments: {'city': 'New York', 'country': 'USA'}
# In this example, we have a function that takes a name, an optional age, variable-length positional arguments, and variable-length keyword arguments.

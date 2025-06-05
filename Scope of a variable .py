#Scope of the variable
#There are two types of variable scopes in Python: local and global.
# 1. Local variables, which are defined within a function and can only be accessed within that function.
def my_function():
    x = 10  # Local variable
    print("Inside the function, x =", x)

my_function()
# print(x)  # This will raise an error because x is not accessible outside the function

# 2. Global variables, which are defined outside of any function and can be accessed from anywhere in the code.
x = 20  # Global variable

def my_function():
    print("Inside the function, x =", x)

my_function()
print("Outside the function, x =", x)

# Modifying a global variable inside a function
x = 30  # Global variable

def my_function():
    global x
    x = 40  # Modifying the global variable
    print("Inside the function, x =", x)

my_function()
print("Outside the function, x =", x)


# Example 2
x=10
def xxx():
    global x
    x=20
    print(x)

print(x) #10
xxx() #20

def outer_function():
    x = 50  # Enclosing variable

    def inner_function():
        nonlocal x # Used as Global but for function loop 
        x = 60  # Modifying the enclosing variable
        print("Inside inner_function, x =", x)

    inner_function()
    print("Inside outer_function, xx =", x)

outer_function()
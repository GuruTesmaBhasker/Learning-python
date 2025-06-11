#Using the module created in the previous step
# Importing the module
import Module
#you can also do like this 
from Module import add, subtract, multiply, divide #In this case, you can use the functions directly without prefixing them with the module name.
#for example:
# print(add(5,3))
# Now you can use the functions defined in the module

# Or you can just import all functions from the module
from Module import *
#this will import all functions from the module, and you can use them directly without prefixing them with the module name.
# Example usage of the functions in the module


# Using the functions from the module
print(Module.add(5,3))
#output: 8 

print(Module.subtract(5,3))
#output: 2

print(Module.multiply(5,3))
#output: 15

print(Module.divide(5,3))
#output: 1.6666666666666667

print(Variable1,"this is a variable from the \"module\"(another file)")
print(Variable2,"this is a variable from the \"module\"(another file)")

# Using the built-in module , math, OS, Random, sys, datetime
import math
# Example usage of the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793
import os
# Example usage of the os module
print(os.getcwd())  # Output: Current working directory
print(os.listdir())  # Output: List of files and directories in the current directory
import random
# Example usage of the random module
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
import sys
# Example usage of the sys module
print(sys.version)  # Output: Python version
import datetime
# Example usage of the datetime module
print(datetime.datetime.now())  # Output: Current date and time
# Example usage of the datetime module

# Dynamic Typing
x = 10              # x is an integer
print(x, type(x))

x = "Hello Python"  # x is now a string!
print(x, type(x))

# Mutability
my_list = [1, 2, 3]       # Lists are mutable
print("Before change:", my_list)

my_list[0] = 99           # Modify the first element
print("After change:", my_list)

my_string = "Immutable"   # Strings are immutable
# my_string[0] = "i"      # This will cause an error if uncommented
print("String is immutable:", my_string)

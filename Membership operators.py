# String example
print("a" in "apple")        # True
print("z" not in "apple")    # True

# List example
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     # True
print("cherry" not in fruits)  # false

#Numbers example

# Using a list
numbers = [10, 20, 30, 40]

print(20 in numbers)       # True → 20 is in the list
print(50 in numbers)       # False → 50 is not in the list
print(30 not in numbers)   # False → 30 is in the list

# Using a tuple
nums_tuple = (1, 2, 3)
print(2 in nums_tuple)     # True

# Using a set
nums_set = {100, 200, 300}
print(100 in nums_set)     # True
print(400 not in nums_set) # True


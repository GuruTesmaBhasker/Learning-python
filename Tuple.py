# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana", 3.14)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 3.14

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 'apple')

# Checking length
print(len(my_tuple))  # Output: 6

# Iterating through a tuple
for item in my_tuple:
    print(item)

#tuple indexing
print(my_tuple[2])  # Output: 3 (indexing)

# Tuple methods
print(my_tuple.count(3))  # Output: 2 (counts occurrences of 3) 

# Nested tuple
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])  # Output: (2, 3) 

# Changing a tuple
# Tuples are immutable, so we cannot change them directly
# However, we can convert to a list, modify, and convert back
temp_list = list(my_tuple)  # Convert to list
temp_list[0] = 10  # Modify the list
my_tuple = tuple(temp_list)  # Convert back to tuple
print(my_tuple)  # Output: (10, 2, 3, 'apple', 'banana', 3.14)
# Output: (10, 2, 3, 'apple', 'banana', 3.14)



# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]

# Accessing elements
print(fruits[0])  # Output: apple (first element)
print(fruits[-1])  # Output: apple (last element)

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'apple']

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'apple', 'orange']

# Removing elements
fruits.remove("apple")  # Removes the first occurrence of 'apple'
print(fruits)  # Output: ['blueberry', 'cherry', 'apple', 'orange']

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Checking length
print(len(fruits))  # Output: 4

# List slicing
print(fruits[1:3])  # Output: ['cherry', 'apple'] (elements from index 1 to 2)  

# List comprehension
squares = [x**2 for x in range(10)]  # List of squares from 0 to 9
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List methods
fruits.sort()  # Sorts the list in ascending order
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# List methods
fruits.reverse()  # Reverses the list
print(fruits)  # Output: ['orange', 'cherry', 'blueberry', 'apple']

# List methods
fruits.clear()  # Clears the list
print(fruits)  # Output: [] (empty list)

# Extending a list
fruits.extend(["orange", "grape"])  # Adds multiple elements

# Copying a list
fruits_copy = fruits.copy()  # Creates a shallow copy of the list
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']

# Inserting elements
fruits.insert(1, "kiwi")  # Inserts 'kiwi' at index 1
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry'] 

# Counting occurrences
fruits.count("apple")  # Counts occurrences of 'apple'
# Output: 1 (occurrences of 'apple')

# Finding index 
fruits.index("banana")  # Finds index of 'banana'
# Output: 2 (index of 'banana')

# Finding minimum and maximum values
numbers = [1, 2, 3, 4, 5]
print(min(numbers))  # Output: 1 (minimum value)
print(max(numbers))  # Output: 5 (maximum value)
 
# Finding sum
print(sum(numbers))  # Output: 15 (sum of all elements) 


# Using pop to remove and return the last element
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)  # Output: ['apple', 'banana'] (last element removed)

# Using pop to remove and return an element at a specific index
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)  # Removes the element at index 1
print(fruits)  # Output: ['apple', 'cherry'] (element at index 1 removed)

# Using del to remove an element at a specific index
fruits = ["apple", "banana", "cherry"]
del fruits[1]  # Removes the element at index 1
print(fruits)  # Output: ['apple', 'cherry'] (element at index 1 removed)

#nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 

print(nested_list[0])  # Output: [1, 2, 3] (first sublist)
print(nested_list[1][2])  # Output: 6 (element at row 1, column 2)

#changing a list to tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)  # Convert list to tuple
print(my_tuple)  # Output: (1, 2, 3, 4) (tuple created from list)

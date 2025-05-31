# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "marks": 85
}

# Accessing values
print(student["name"])  # Output: Alice

# Adding a new key-value pair
student["grade"] = "A"

# Modifying a value
student["marks"] = 90

# Removing a key-value pair
del student["age"]

# Iterating through keys and values
# dict.items() – Returns all key-value pairs as tuples
for key, value in student.items():
    print(key, ":", value)

# Checking if a key exists
if "marks" in student:
    print("Marks are present.")

# Getting all keys and values
print(student.keys())    # Output: dict_keys(['name', 'marks', 'grade'])
print(student.values())  # Output: dict_values(['Alice', 90, 'A'])

#Nested dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "courses": {
        "math": 90,
        "science": 85
    }
}

# Accessing nested dictionary values
print(student["courses"]["math"])  # Output: 90
  
